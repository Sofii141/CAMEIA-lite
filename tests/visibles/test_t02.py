from cameia_lite.t02 import contar_caracteres
def test_simple():
    assert contar_caracteres("Ana") == 3
def test_combinante():
    assert contar_caracteres("Jose\u0301") == 4
