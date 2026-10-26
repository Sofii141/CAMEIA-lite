import pytest
from cameia_lite.t21 import perfil_activo
def test_k_service_vacio_es_despliegue():
    assert perfil_activo({"K_SERVICE": ""}) == "production"
def test_emulador_vacio_en_despliegue():
    with pytest.raises(RuntimeError) as e:
        perfil_activo({"PERFIL": "production", "FIREBASE_AUTH_EMULATOR_HOST": ""})
    assert not isinstance(e.value, NotImplementedError)
def test_prod_no_es_production_y_emulador_local():
    assert perfil_activo({"PERFIL": "prod"}) == "local"
    assert perfil_activo({"FIREBASE_AUTH_EMULATOR_HOST": "localhost:9099"}) == "local-emulador"
    assert perfil_activo({"FIREBASE_AUTH_EMULATOR_HOST": ""}) == "local"
