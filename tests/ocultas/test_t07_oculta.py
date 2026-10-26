from datetime import date
from cameia_lite.t07 import validar_nacimiento
def test_limite_110():
    assert validar_nacimiento(date(1916, 10, 26), date(2026, 10, 26)) == "OK"
    assert validar_nacimiento(date(1915, 10, 26), date(2026, 10, 26)) == "OUT_OF_RANGE"
def test_antes_del_cumple():
    assert validar_nacimiento(date(1915, 10, 27), date(2026, 10, 26)) == "OK"
def test_29_febrero():
    assert validar_nacimiento(date(1916, 2, 29), date(2027, 2, 28)) == "OK"
    assert validar_nacimiento(date(1916, 2, 29), date(2027, 3, 1)) == "OUT_OF_RANGE"
