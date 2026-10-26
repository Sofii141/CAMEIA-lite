from cameia_lite.t04 import validar_correo
def test_dos_arrobas_y_espacio():
    assert not validar_correo("a@b@c.co") and not validar_correo("a na@c.co")
def test_dominio():
    assert not validar_correo("ana@co") and not validar_correo("ana@.co") and not validar_correo("ana@c.co.")
def test_largo():
    assert validar_correo("a" * 245 + "@c.co") and not validar_correo("a" * 250 + "@c.co")
