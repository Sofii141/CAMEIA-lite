from cameia_lite.t04 import validar_correo
def test_ok():
    assert validar_correo("ana@cameia.co")
def test_sin_arroba():
    assert not validar_correo("ana.cameia.co")
