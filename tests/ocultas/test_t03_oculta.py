from cameia_lite.t03 import validar_nombre
def test_apostrofos():
    assert validar_nombre("O'Brien") and validar_nombre("O\u2019Connor")
def test_solo_simbolos():
    assert not validar_nombre("---") and not validar_nombre("   ")
def test_unicode_y_combinante():
    assert validar_nombre("Zoe\u0308") and validar_nombre("Łukasz") and not validar_nombre("Ana😀")
