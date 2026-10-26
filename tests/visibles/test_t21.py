from cameia_lite.t21 import perfil_activo
def test_local():
    assert perfil_activo({}) == "local"
def test_despliegue():
    assert perfil_activo({"K_SERVICE": "cameia-perfil"}) == "production"
