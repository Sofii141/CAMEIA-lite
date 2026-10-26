from cameia_lite.t24 import enmascarar_correo
def test_ok():
    assert enmascarar_correo("ana@cameia.co") == "a**@cameia.co"
