from cameia_lite.t15 import catalogo_roles
R = [{"id": 1, "activo": True, "es": "Desarrollador", "en": "Developer"}]
def test_es():
    assert catalogo_roles(R, "es") == [{"id": 1, "nombre": "Desarrollador"}]
