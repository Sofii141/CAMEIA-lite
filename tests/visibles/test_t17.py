from cameia_lite.t17 import validar_salario
def test_ok():
    assert validar_salario("2500000") and validar_salario("2500000.50")
def test_negativo():
    assert not validar_salario("-100")
