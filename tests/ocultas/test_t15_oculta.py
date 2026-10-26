import pytest
from cameia_lite.t15 import catalogo_roles
R = [{"id": 1, "activo": True, "es": "Desarrollador", "en": "Developer"},
     {"id": 2, "activo": False, "es": "Analista", "en": "Analyst"}]
def test_inactivo_fuera_y_en():
    assert catalogo_roles(R, "en") == [{"id": 1, "nombre": "Developer"}]
def test_none_es_espanol():
    assert catalogo_roles(R, None)[0]["nombre"] == "Desarrollador"
def test_idioma_no_soportado():
    with pytest.raises(ValueError):
        catalogo_roles(R, "fr")
