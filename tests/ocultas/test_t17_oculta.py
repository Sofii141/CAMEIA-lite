from cameia_lite.t17 import validar_salario
def test_14_digitos():
    assert validar_salario("9" * 13) and not validar_salario("9" * 14)
def test_formatos_raros():
    assert not validar_salario("1,000") and not validar_salario("+5") and not validar_salario(" 5") and not validar_salario("5.")
def test_decimales():
    assert not validar_salario("10.123") and validar_salario("10.1")
