import pytest
from cameia_lite.t11 import ContadorReintentos
def test_red_no_cuenta():
    c = ContadorReintentos()
    for _ in range(5):
        c.registrar_fallo("RED")
    c.registrar_fallo("IA"); c.registrar_fallo("IA")
    assert c.puede_reintentar()
def test_reiniciar():
    c = ContadorReintentos()
    for _ in range(3):
        c.registrar_fallo("IA")
    c.reiniciar()
    assert c.puede_reintentar()
def test_tipo_invalido():
    with pytest.raises(ValueError):
        ContadorReintentos().registrar_fallo("OTRO")
