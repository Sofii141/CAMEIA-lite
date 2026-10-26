from cameia_lite.t05 import validar_celular
def test_ok():
    assert validar_celular("+573001234567")
def test_sin_mas():
    assert not validar_celular("573001234567")
