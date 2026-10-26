# Tareas de CAMEIA-lite

Cada tarea es una regla **real** del backlog de CAMEIA, aislada como función y sin infraestructura.
Tamaño: S ≈ 15–25 min · M ≈ 25–45 min · L ≈ 45–70 min (estimado; lo real lo dirá el cronómetro).

| ID | Tarea | Tamaño | Difícil | Origen en CAMEIA | Ya la implementó en CAMEIA |
|---|---|---|---|---|---|
| t01 | Normalizar texto | S |  | CM-36 |  |
| t02 | Contar caracteres | S |  | CM-36 |  |
| t03 | Validar nombre | M | ⚠️ sí | CM-36 |  |
| t04 | Validar correo | S |  | CM-36 |  |
| t05 | Validar celular | S |  | CM-36 |  |
| t06 | Política de contraseñas | M |  | CM-36 |  |
| t07 | Fecha de nacimiento | M | ⚠️ sí | CM-279 |  |
| t08 | Cupo de perfiles por plan | M | ⚠️ sí | CM-271 |  |
| t09 | Nivel de log por estado HTTP | S |  | CM-184 |  |
| t10 | Mensajes de error por campo | M |  | CM-336 / CM-298 | Juan José |
| t11 | Contador de reintentos | M |  | CM-217 | Juan José |
| t12 | Crear una sola vez (doble clic) | L | ⚠️ sí | CM-270 | Juan José |
| t13 | Eliminar rol objetivo | M | ⚠️ sí | CM-71 / CM-271 |  |
| t14 | Sustituir rol conservando su lugar | S |  | CM-72 |  |
| t15 | Catálogo de roles por idioma | S |  | CM-82 / CM-72 | Ana Sofía |
| t16 | Fechas de formación | M |  | CM-271 |  |
| t17 | Expectativa salarial | S |  | CM-271 |  |
| t18 | Propagar X-Request-Id | M | ⚠️ sí | CM-279 / CM-104 |  |
| t19 | Limpiar cabeceras de identidad | M | ⚠️ sí | CM-104 |  |
| t20 | Origen permitido (CORS) | S | ⚠️ sí | CM-162 |  |
| t21 | Perfil de arranque y emulador | M | ⚠️ sí | CM-190 / CM-191 / CM-175 |  |
| t22 | Registro idempotente (Idempotency-Key) | L | ⚠️ sí | CM-340 |  |
| t23 | Progreso de la entrevista | S |  | CM-217 | Juan José |
| t24 | Enmascarar correo en logs | S |  | CM-271 (registro sin datos personales) |  |

## t01 · Normalizar texto (S)

Archivo: `src/cameia_lite/t01.py` · Firma: `def normalizar_texto(s: str) -> str`

Quitar espacios al inicio y al final (incluye tabulaciones, saltos de línea y el espacio duro `\u00a0`) y devolver el texto en forma Unicode **NFC**.
- CA1: `"  Ana  "` → `"Ana"`.
- CA2: `"e\u0301"` (e + tilde combinante) → `"é"` (un solo carácter).
- CA3: los espacios internos no se tocan.

## t02 · Contar caracteres (S)

Archivo: `src/cameia_lite/t02.py` · Firma: `def contar_caracteres(s: str) -> int`

Contar los caracteres como los ve una persona: **puntos de código después de normalizar a NFC** (no bytes).
- CA1: `"Ana"` → 3.
- CA2: `"Jose\u0301"` → 4.
- CA3: un emoji simple como `"😀"` cuenta 1.

## t03 · Validar nombre (M)

Archivo: `src/cameia_lite/t03.py` · Firma: `def validar_nombre(s: str) -> bool`

Un nombre o apellido es válido si, **después de normalizar (recortar + NFC)**:
- CA1: no queda vacío y tiene **al menos una letra**;
- CA2: solo contiene letras de cualquier idioma, marcas combinantes, espacio, apóstrofo recto `'`, apóstrofo tipográfico `’` y guion `-`;
- CA3: números, `@`, `_` y emojis lo hacen inválido.
- Ejemplos válidos: `"José"`, `"O’Connor"`, `"Ana-María"`, `"Zoë"`. Inválidos: `"---"`, `"Ana3"`, `""`.

## t04 · Validar correo (S)

Archivo: `src/cameia_lite/t04.py` · Firma: `def validar_correo(s: str) -> bool`

Validación básica de correo:
- CA1: exactamente una `@`, con texto antes y después;
- CA2: el dominio tiene al menos un punto, y no empieza ni termina con punto;
- CA3: sin espacios y con máximo **254** caracteres.

## t05 · Validar celular (S)

Archivo: `src/cameia_lite/t05.py` · Firma: `def validar_celular(s: str) -> bool`

Formato E.164 simplificado:
- CA1: empieza con `+`, seguido **solo de dígitos**;
- CA2: entre **6 y 15** dígitos;
- CA3: el primer dígito no puede ser `0`.

## t06 · Política de contraseñas (M)

Archivo: `src/cameia_lite/t06.py` · Firma: `def validar_contrasena(pwd: str, comunes: list[str]) -> list[str]`

Devolver la lista de códigos de error (vacía si es válida), **en este orden**:
- CA1: `"TOO_SHORT"` si tiene menos de 8 caracteres (puntos de código NFC);
- CA2: `"TOO_LONG"` si tiene más de 64;
- CA3: `"COMMON"` si, recortada, en minúsculas y en NFC, está en la lista `comunes` (que también se compara normalizada).

## t07 · Fecha de nacimiento (M)

Archivo: `src/cameia_lite/t07.py` · Firma: `def validar_nacimiento(nacimiento: date, hoy: date) -> str`

Devolver `"FUTURE"` si la fecha es posterior a `hoy`, `"OUT_OF_RANGE"` si la persona tiene **más de 110 años cumplidos**, y `"OK"` en otro caso.
- CA1: los años cumplidos se cuentan por cumpleaños (no por año calendario).
- CA2: quien nació un **29 de febrero** cumple años el **1 de marzo** en los años no bisiestos.
- CA3: exactamente 110 años cumplidos es `"OK"`.

## t08 · Cupo de perfiles por plan (M)

Archivo: `src/cameia_lite/t08.py` · Firma: `def puede_crear_perfil(plan: str, vence: date | None, hoy: date, perfiles_actuales: int) -> tuple[int, str | None]`

Decidir si se puede crear un perfil más:
- CA1: plan `"FREE"` permite 1 perfil; `"PREMIUM"` permite 3.
- CA2: un PREMIUM **vencido** (`vence` anterior a `hoy`) se comporta como FREE. El día del vencimiento todavía es válido.
- CA3: si se puede → `(201, None)`; si el cupo está agotado → `(403, "PLAN_LIMIT")`.
- CA4: un plan desconocido lanza `ValueError`.

## t09 · Nivel de log por estado HTTP (S)

Archivo: `src/cameia_lite/t09.py` · Firma: `def nivel_log(status: int) -> str | None`

- CA1: 5xx → `"ERROR"`.
- CA2: 404 → `"INFO"`; cualquier otro 4xx → `"WARN"`.
- CA3: el resto (1xx, 2xx, 3xx) → `None`.

## t10 · Mensajes de error por campo (M)

Archivo: `src/cameia_lite/t10.py` · Firma: `def mensajes_por_campo(problem: dict) -> dict[str, str]`

Recibe un ProblemDetail del backend, como `{"detail": "...", "errors": [{"field": "empresa", "code": "COMPANY_INVALID_CHARACTERS"}]}`, y devuelve `{campo: mensaje}` usando el diccionario `CATALOGO` del archivo.
- CA1: cada error con un código del catálogo produce su mensaje bajo su campo.
- CA2: si algún código no está en el catálogo, o no hay `errors`, se devuelve `{"_general": MENSAJE_GENERICO}` (y solo eso).
- CA3: **nunca** se muestra el texto `detail` del servidor.

## t11 · Contador de reintentos (M)

Archivo: `src/cameia_lite/t11.py` · Firma: `class ContadorReintentos`

Clase con tres métodos:
- `registrar_fallo(tipo: str)` con `tipo` en `{"IA", "RED", "VALIDACION"}`; otro tipo lanza `ValueError`.
- `puede_reintentar() -> bool`.
- `reiniciar()`.
- CA1: **solo los fallos `"IA"`** cuentan para el tope.
- CA2: se puede reintentar mientras haya menos de 3 fallos de IA.
- CA3: `reiniciar()` vuelve el contador a cero.

## t12 · Crear una sola vez (doble clic) (L)

Archivo: `src/cameia_lite/t12.py` · Firma: `class CreadorUnaVez`

Evita la doble creación de un perfil por doble clic. `CreadorUnaVez(fn)` envuelve una función sin argumentos.
- CA1: `crear()` llama a `fn` y devuelve su resultado.
- CA2: si varios hilos llaman a `crear()` **mientras una creación está en curso**, `fn` se ejecuta **una sola vez** y todos reciben el mismo resultado.
- CA3: cuando la creación termina, una llamada posterior vuelve a ejecutar `fn`.
- CA4: si `fn` lanza una excepción, quienes esperaban reciben la misma excepción y la siguiente llamada puede reintentar.

## t13 · Eliminar rol objetivo (M)

Archivo: `src/cameia_lite/t13.py` · Firma: `def eliminar_rol(perfil: dict, rol_id: str) -> int`

`perfil = {"estado": "DRAFT" | "COMPLETED", "roles": [ids]}`. Devuelve un código HTTP y modifica `perfil["roles"]` solo si elimina.
- CA1: si el rol no está en el perfil → `404` (**esta regla se evalúa primero**).
- CA2: eliminar el **último** rol de un perfil `COMPLETED` → `409`, sin cambiar nada.
- CA3: en `DRAFT` sí se puede eliminar el último rol.
- CA4: si elimina → `204`.

## t14 · Sustituir rol conservando su lugar (S)

Archivo: `src/cameia_lite/t14.py` · Firma: `def sustituir_rol(roles: list[str], viejo: str, nuevo: str) -> list[str]`

Devolver una **nueva** lista donde `nuevo` ocupa la posición de `viejo`.
- CA1: el orden de los demás se conserva.
- CA2: si `viejo` no está, o `nuevo` ya está en la lista → `ValueError`.
- CA3: la lista original no se modifica.

## t15 · Catálogo de roles por idioma (S)

Archivo: `src/cameia_lite/t15.py` · Firma: `def catalogo_roles(roles: list[dict], lang: str | None) -> list[dict]`

Cada rol es `{"id": ..., "activo": bool, "es": "...", "en": "..."}`. Devolver `[{"id": ..., "nombre": ...}]`.
- CA1: solo los roles **activos**, en el orden recibido.
- CA2: `lang` puede ser `"es"` o `"en"`; `None` equivale a `"es"`.
- CA3: cualquier otro idioma → `ValueError`.

## t16 · Fechas de formación (M)

Archivo: `src/cameia_lite/t16.py` · Firma: `def validar_formacion(inicio: str, fin: str | None) -> list[str]`

Las fechas vienen como `"AAAA-MM"`; `fin = None` significa "en curso". Devolver la lista de errores (vacía si todo está bien):
- CA1: `"INVALID_FORMAT"` si alguna fecha no es exactamente 4 dígitos, guion y mes `01`–`12`.
- CA2: `"YEAR_ZERO"` si algún año es `0000`.
- CA3: `"END_BEFORE_START"` si `fin` es anterior a `inicio` (solo se revisa si ambas tienen formato válido).
- Cada código aparece como máximo una vez.

## t17 · Expectativa salarial (S)

Archivo: `src/cameia_lite/t17.py` · Firma: `def validar_salario(valor: str) -> bool`

El salario llega como texto.
- CA1: solo dígitos, con parte decimal opcional de 1 o 2 dígitos separada por punto (`"2500000.50"`).
- CA2: la parte entera tiene como máximo **13** dígitos.
- CA3: no se admiten negativos, signo `+`, comas ni espacios.

## t18 · Propagar X-Request-Id (M)

Archivo: `src/cameia_lite/t18.py` · Firma: `def request_id(entrante: str | None) -> str`

Decidir qué identificador de petición usar:
- CA1: si `entrante` es un UUID canónico (36 caracteres `8-4-4-4-12` hexadecimales), devolverlo en **minúsculas**.
- CA2: si no viene, está vacío o no es válido, generar un `uuid4` nuevo.
- CA3: nunca devolver un valor que contenga saltos de línea u otro texto añadido (evita la inyección en los logs).

## t19 · Limpiar cabeceras de identidad (M)

Archivo: `src/cameia_lite/t19.py` · Firma: `def limpiar_cabeceras(headers: dict[str, str], identidad: dict[str, str]) -> dict[str, str]`

El gateway debe ser la **única** fuente de identidad hacia los microservicios.
- CA1: eliminar toda cabecera entrante cuyo nombre empiece por `x-user-`, **sin importar mayúsculas** (`X-User-Id`, `x-USER-roles`…).
- CA2: luego agregar `X-User-Id` y `X-User-Email` con los valores de `identidad["id"]` e `identidad["email"]`.
- CA3: las demás cabeceras se conservan tal cual, y no se modifica el diccionario recibido.

## t20 · Origen permitido (CORS) (S)

Archivo: `src/cameia_lite/t20.py` · Firma: `def origen_permitido(origen: str | None, permitidos: list[str]) -> bool`

- CA1: solo se permite un origen que esté **exactamente** en la lista (sin comodines ni coincidencias parciales).
- CA2: `None` o vacío → `False`.
- CA3: la comparación del esquema y el host no distingue mayúsculas (`HTTPS://Cameia.App` equivale a `https://cameia.app`), pero una barra final o un puerto distinto lo hacen otro origen.

## t21 · Perfil de arranque y emulador (M)

Archivo: `src/cameia_lite/t21.py` · Firma: `def perfil_activo(env: dict[str, str]) -> str`

Decidir con qué perfil arranca un servicio, según las variables de entorno:
- CA1: es un **despliegue** si existe la variable `K_SERVICE` (**aunque esté vacía**) o si `PERFIL == "production"`.
- CA2: en un despliegue, si existe `FIREBASE_AUTH_EMULATOR_HOST` (**aunque esté vacía**), lanzar `RuntimeError` (el servicio se niega a arrancar); si no existe, devolver `"production"`.
- CA3: fuera de un despliegue, si `FIREBASE_AUTH_EMULATOR_HOST` tiene un valor no vacío → `"local-emulador"`; si no → `"local"`.
- Ojo: el perfil se llama `"production"`, no `"prod"`. `PERFIL == "prod"` **no** es un despliegue.

## t22 · Registro idempotente (Idempotency-Key) (L)

Archivo: `src/cameia_lite/t22.py` · Firma: `class RegistroIdempotente`

Registrar respuestas de entrevista sin duplicarlas cuando el navegador reintenta. Método `registrar(clave: str, cuerpo: dict) -> tuple[int, dict | None]`:
- CA1: clave vacía o en blanco → `(400, None)`.
- CA2: primera vez con esa clave → guarda y devuelve `(201, {"id": n})`, con `n` consecutivo desde 1.
- CA3: misma clave y **mismo** cuerpo → `(200, <la misma respuesta de antes>)`, sin crear otro registro.
- CA4: misma clave con un cuerpo **distinto** → `(422, None)`.
- `total()` devuelve cuántos registros reales se crearon.

## t23 · Progreso de la entrevista (S)

Archivo: `src/cameia_lite/t23.py` · Firma: `def progreso(k: int, total: int) -> str`

- CA1: devuelve `"Pregunta k de total"`, por ejemplo `"Pregunta 2 de 5"` (con "P" mayúscula y el resto en minúscula).
- CA2: si `total < 1`, o `k` está fuera de `1..total` → `ValueError`.

## t24 · Enmascarar correo en logs (S)

Archivo: `src/cameia_lite/t24.py` · Firma: `def enmascarar_correo(correo: str) -> str`

Para no escribir datos personales en los logs:
- CA1: conservar la primera letra de la parte local y reemplazar el resto por `*` (misma longitud). El dominio se conserva: `"ana@cameia.co"` → `"a**@cameia.co"`.
- CA2: una parte local de 1 carácter queda como `"*"`: `"a@c.co"` → `"*@c.co"`.
- CA3: si no tiene exactamente una `@` o la parte local está vacía → `"***"`.
