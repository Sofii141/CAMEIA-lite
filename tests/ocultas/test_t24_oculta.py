from cameia_lite.t24 import enmascarar_correo
def test_un_caracter():
    assert enmascarar_correo("a@c.co") == "*@c.co"
def test_invalidos():
    assert enmascarar_correo("sinarroba") == "***" and enmascarar_correo("@c.co") == "***" and enmascarar_correo("a@b@c") == "***"
def test_largo():
    assert enmascarar_correo("juanjose@x.co") == "j*******@x.co"
