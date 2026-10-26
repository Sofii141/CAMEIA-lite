"""Demo de CAMEIA-lite: un backend mínimo (solo librería estándar) que usa las funciones de las tareas.

Toda la validación vive aquí: la página `index.html` no valida nada, solo muestra lo que responde el backend.
Si una tarea todavía no está implementada, su campo responde "tarea tNN pendiente" en vez de romper.

Uso:  python demo/servidor.py   →  abrir http://localhost:8000
"""
import json
import sys
import uuid
from datetime import date
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from cameia_lite import t01, t03, t04, t05, t06, t07, t09, t16, t17, t18, t24  # noqa: E402

COMUNES = ["password123", "12345678", "qwerty123", "cameia2026"]
MENSAJES = {
    "INVALID_NAME": "Solo letras, espacios, apóstrofo y guion.",
    "INVALID_EMAIL": "Escribe un correo válido.",
    "INVALID_PHONE": "Usa el formato internacional, por ejemplo +573001234567.",
    "TOO_SHORT": "La contraseña debe tener al menos 8 caracteres.",
    "TOO_LONG": "La contraseña no puede superar 64 caracteres.",
    "COMMON": "Esa contraseña es demasiado común.",
    "FUTURE": "La fecha de nacimiento no puede estar en el futuro.",
    "OUT_OF_RANGE": "Revisa la fecha de nacimiento.",
    "INVALID_DATE": "Usa el formato AAAA-MM-DD.",
    "INVALID_SALARY": "Solo números, con máximo 2 decimales y 13 dígitos enteros.",
    "INVALID_FORMAT": "Usa el formato AAAA-MM.",
    "YEAR_ZERO": "El año no puede ser 0000.",
    "END_BEFORE_START": "La fecha de fin no puede ser anterior a la de inicio.",
}


def _seguro(tarea, fn, *args):
    """Ejecuta una función de tarea; si aún no está implementada, lo dice en vez de fallar."""
    try:
        return fn(*args), None
    except NotImplementedError:
        return None, f"tarea {tarea} pendiente"


def _errores(campo, codigos, errores):
    for c in codigos:
        errores.setdefault(campo, []).append(MENSAJES.get(c, c))


def validar_registro(d):
    errores = {}
    for campo in ("nombre", "apellido"):
        texto, pend = _seguro("t01", t01.normalizar_texto, d.get(campo, ""))
        ok, pend2 = _seguro("t03", t03.validar_nombre, texto if texto is not None else d.get(campo, ""))
        if pend or pend2:
            errores[campo] = [pend or pend2]
        elif not ok:
            _errores(campo, ["INVALID_NAME"], errores)
    for campo, tarea, fn, codigo in (("correo", "t04", t04.validar_correo, "INVALID_EMAIL"),
                                     ("celular", "t05", t05.validar_celular, "INVALID_PHONE")):
        ok, pend = _seguro(tarea, fn, d.get(campo, ""))
        if pend:
            errores[campo] = [pend]
        elif not ok:
            _errores(campo, [codigo], errores)
    codigos, pend = _seguro("t06", t06.validar_contrasena, d.get("contrasena", ""), COMUNES)
    if pend:
        errores["contrasena"] = [pend]
    else:
        _errores("contrasena", codigos, errores)
    try:
        nac = date.fromisoformat(d.get("nacimiento", ""))
        r, pend = _seguro("t07", t07.validar_nacimiento, nac, date.today())
        if pend:
            errores["nacimiento"] = [pend]
        elif r != "OK":
            _errores("nacimiento", [r], errores)
    except ValueError:
        _errores("nacimiento", ["INVALID_DATE"], errores)
    return errores


def validar_perfil(d):
    errores = {}
    ok, pend = _seguro("t17", t17.validar_salario, d.get("salario", ""))
    if pend:
        errores["salario"] = [pend]
    elif not ok:
        _errores("salario", ["INVALID_SALARY"], errores)
    codigos, pend = _seguro("t16", t16.validar_formacion, d.get("inicio", ""), d.get("fin") or None)
    if pend:
        errores["formacion"] = [pend]
    else:
        _errores("formacion", codigos, errores)
    return errores


RUTAS = {"/api/registro": validar_registro, "/api/perfil": validar_perfil}


class Manejador(BaseHTTPRequestHandler):
    def _responder(self, status, cuerpo, tipo="application/json; charset=utf-8"):
        datos = cuerpo if isinstance(cuerpo, bytes) else json.dumps(cuerpo, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", tipo)
        self.send_header("X-Request-Id", self.rid)
        self.end_headers()
        self.wfile.write(datos)
        self._log(status)

    def _log(self, status):
        nivel, _ = _seguro("t09", t09.nivel_log, status)
        correo = getattr(self, "correo", None)
        if correo:
            correo, pend = _seguro("t24", t24.enmascarar_correo, correo)
            correo = "***" if pend else correo
        print(f"[{nivel or 'INFO'}] {self.command} {self.path} -> {status} rid={self.rid}" + (f" correo={correo}" if correo else ""), flush=True)

    def _preparar(self):
        rid, pend = _seguro("t18", t18.request_id, self.headers.get("X-Request-Id"))
        self.rid = str(uuid.uuid4()) if pend else rid

    def log_message(self, *args):  # silencia el log por defecto; usamos _log
        pass

    def do_GET(self):
        self._preparar()
        if self.path in ("/", "/index.html"):
            self._responder(200, (Path(__file__).parent / "index.html").read_bytes(), "text/html; charset=utf-8")
        else:
            self._responder(404, {"code": "ROUTE_NOT_FOUND"})

    def do_POST(self):
        self._preparar()
        fn = RUTAS.get(self.path)
        if not fn:
            return self._responder(404, {"code": "ROUTE_NOT_FOUND"})
        try:
            d = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        except json.JSONDecodeError:
            return self._responder(400, {"code": "INVALID_JSON"})
        self.correo = d.get("correo")
        errores = fn(d)
        if errores:
            self._responder(422, {"code": "VALIDATION_FAILED", "errors": errores})
        else:
            self._responder(201, {"ok": True})


if __name__ == "__main__":
    puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"CAMEIA-lite demo en http://localhost:{puerto}  (Ctrl+C para salir)", flush=True)
    ThreadingHTTPServer(("127.0.0.1", puerto), Manejador).serve_forever()
