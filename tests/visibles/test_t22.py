from cameia_lite.t22 import RegistroIdempotente
def test_primera_y_repetida():
    r = RegistroIdempotente()
    assert r.registrar("k1", {"texto": "hola"}) == (201, {"id": 1})
    assert r.registrar("k1", {"texto": "hola"}) == (200, {"id": 1})
