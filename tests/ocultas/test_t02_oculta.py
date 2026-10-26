from cameia_lite.t02 import contar_caracteres
def test_emoji():
    assert contar_caracteres("😀") == 1
def test_vacio():
    assert contar_caracteres("") == 0
def test_ene():
    assert contar_caracteres("n\u0303an\u0303u") == 4
