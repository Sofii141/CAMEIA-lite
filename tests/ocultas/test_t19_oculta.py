from cameia_lite.t19 import limpiar_cabeceras
I = {"id": "u1", "email": "a@c.co"}
def test_mayusculas_mezcladas():
    r = limpiar_cabeceras({"x-USER-roles": "admin", "x-user-id": "x"}, I)
    assert "x-USER-roles" not in r and "x-user-id" not in r and r["X-User-Id"] == "u1"
def test_no_muta():
    h = {"X-User-Id": "x"}; limpiar_cabeceras(h, I)
    assert h == {"X-User-Id": "x"}
def test_parecidas_se_conservan():
    r = limpiar_cabeceras({"X-Username-Hint": "k", "X-Request-Id": "r"}, I)
    assert r["X-Username-Hint"] == "k" and r["X-Request-Id"] == "r"
