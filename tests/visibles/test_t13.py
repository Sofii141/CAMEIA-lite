from cameia_lite.t13 import eliminar_rol
def test_elimina():
    p = {"estado": "COMPLETED", "roles": ["a", "b"]}
    assert eliminar_rol(p, "a") == 204 and p["roles"] == ["b"]
def test_ultimo_completed():
    p = {"estado": "COMPLETED", "roles": ["a"]}
    assert eliminar_rol(p, "a") == 409 and p["roles"] == ["a"]
