from datetime import date
from cameia_lite.t07 import validar_nacimiento
def test_ok():
    assert validar_nacimiento(date(2000, 5, 1), date(2026, 10, 26)) == "OK"
def test_futuro():
    assert validar_nacimiento(date(2027, 1, 1), date(2026, 10, 26)) == "FUTURE"
