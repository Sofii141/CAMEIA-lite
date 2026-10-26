from cameia_lite.t19 import limpiar_cabeceras
def test_reemplaza():
    h = {"X-User-Id": "atacante", "Accept": "json"}
    r = limpiar_cabeceras(h, {"id": "u1", "email": "a@c.co"})
    assert r == {"Accept": "json", "X-User-Id": "u1", "X-User-Email": "a@c.co"}
