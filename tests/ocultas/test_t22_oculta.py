from cameia_lite.t22 import RegistroIdempotente
def test_cuerpo_distinto():
    r = RegistroIdempotente(); r.registrar("k1", {"texto": "hola"})
    assert r.registrar("k1", {"texto": "chao"}) == (422, None) and r.total() == 1
def test_clave_vacia():
    r = RegistroIdempotente()
    assert r.registrar("", {}) == (400, None) and r.registrar("  ", {}) == (400, None) and r.total() == 0
def test_mutar_cuerpo_despues_no_engana():
    r = RegistroIdempotente(); c = {"texto": "hola"}; r.registrar("k", c)
    c["texto"] = "cambiado"
    assert r.registrar("k", {"texto": "hola"}) == (200, {"id": 1})
    assert r.registrar("k2", {"x": 1}) == (201, {"id": 2})
