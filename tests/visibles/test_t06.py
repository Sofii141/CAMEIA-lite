from cameia_lite.t06 import validar_contrasena
def test_ok():
    assert validar_contrasena("Cameia#2026", []) == []
def test_corta():
    assert validar_contrasena("abc", []) == ["TOO_SHORT"]
