from cameia_lite.t05 import validar_celular
def test_limites():
    assert validar_celular("+123456") and not validar_celular("+12345") and not validar_celular("+1" + "2" * 15)
def test_cero_y_espacios():
    assert not validar_celular("+0573001") and not validar_celular("+57 300 123")
def test_digitos_no_ascii():
    assert not validar_celular("+\u0665\u0665\u0665\u0665\u0665\u0665")
