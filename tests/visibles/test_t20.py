from cameia_lite.t20 import origen_permitido
P = ["https://cameia.app", "http://localhost:5173"]
def test_ok():
    assert origen_permitido("https://cameia.app", P)
def test_otro():
    assert not origen_permitido("https://otro.com", P)
