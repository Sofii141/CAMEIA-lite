from datetime import date
from cameia_lite.t08 import puede_crear_perfil
HOY = date(2026, 10, 26)
def test_free():
    assert puede_crear_perfil("FREE", None, HOY, 0) == (201, None)
    assert puede_crear_perfil("FREE", None, HOY, 1) == (403, "PLAN_LIMIT")
def test_premium():
    assert puede_crear_perfil("PREMIUM", date(2027, 1, 1), HOY, 2) == (201, None)
