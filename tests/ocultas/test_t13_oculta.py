from cameia_lite.t13 import eliminar_rol
def test_404_antes_que_409():
    p = {"estado": "COMPLETED", "roles": ["a"]}
    assert eliminar_rol(p, "z") == 404
def test_draft_ultimo():
    p = {"estado": "DRAFT", "roles": ["a"]}
    assert eliminar_rol(p, "a") == 204 and p["roles"] == []
def test_404_no_modifica():
    p = {"estado": "DRAFT", "roles": ["a", "b"]}
    eliminar_rol(p, "c")
    assert p["roles"] == ["a", "b"]
