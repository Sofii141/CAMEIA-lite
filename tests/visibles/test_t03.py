from cameia_lite.t03 import validar_nombre
def test_validos():
    assert validar_nombre("José") and validar_nombre("Ana-María")
def test_numero():
    assert not validar_nombre("Ana3")
