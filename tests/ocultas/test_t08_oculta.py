from datetime import date
import pytest
from cameia_lite.t08 import puede_crear_perfil
HOY = date(2026, 10, 26)
def test_vencido_es_free():
    assert puede_crear_perfil("PREMIUM", date(2026, 10, 25), HOY, 1) == (403, "PLAN_LIMIT")
def test_vence_hoy_vale():
    assert puede_crear_perfil("PREMIUM", HOY, HOY, 2) == (201, None)
def test_desconocido_y_tope():
    assert puede_crear_perfil("PREMIUM", None, HOY, 3) == (403, "PLAN_LIMIT")
    with pytest.raises(ValueError):
        puede_crear_perfil("GOLD", None, HOY, 0)
