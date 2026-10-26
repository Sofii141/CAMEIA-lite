import threading, time
import pytest
from cameia_lite.t12 import CreadorUnaVez
def test_concurrente_una_vez():
    llamadas = []
    def fn():
        llamadas.append(1); time.sleep(0.2); return "perfil-1"
    c = CreadorUnaVez(fn); res = []
    hs = [threading.Thread(target=lambda: res.append(c.crear())) for _ in range(5)]
    [h.start() for h in hs]; [h.join() for h in hs]
    assert len(llamadas) == 1 and res == ["perfil-1"] * 5
def test_secuencial_vuelve_a_ejecutar():
    n = []
    c = CreadorUnaVez(lambda: n.append(1) or len(n))
    assert c.crear() == 1 and c.crear() == 2
def test_error_y_reintento():
    estado = {"fallar": True}
    def fn():
        if estado["fallar"]:
            raise RuntimeError("caido")
        return "ok"
    c = CreadorUnaVez(fn)
    with pytest.raises(RuntimeError):
        c.crear()
    estado["fallar"] = False
    assert c.crear() == "ok"
