from cameia_lite.t20 import origen_permitido
P = ["https://cameia.app", "http://localhost:5173"]
def test_subdominio_trampa():
    assert not origen_permitido("https://cameia.app.evil.com", P) and not origen_permitido("https://evil-cameia.app", P)
def test_mayusculas_y_barra():
    assert origen_permitido("HTTPS://Cameia.App", P) and not origen_permitido("https://cameia.app/", P)
def test_puerto_y_none():
    assert not origen_permitido("http://localhost:3000", P) and not origen_permitido(None, P) and not origen_permitido("", P)
