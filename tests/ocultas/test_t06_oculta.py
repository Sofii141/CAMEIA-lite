from cameia_lite.t06 import validar_contrasena
def test_comun_normalizada():
    assert validar_contrasena("  PASSWORD123 ", ["password123"]) == ["COMMON"]
def test_lista_sin_normalizar():
    assert validar_contrasena("contraseña1", ["  Contrasen\u0303a1"]) == ["COMMON"]
def test_larga_y_orden():
    assert validar_contrasena("a" * 65, []) == ["TOO_LONG"]
    assert validar_contrasena("abc", ["abc"]) == ["TOO_SHORT", "COMMON"]
