from cameia_lite.t01 import normalizar_texto
def test_espacio_duro_y_tabs():
    assert normalizar_texto("\u00a0\tJosé\n") == "José"
def test_internos_intactos():
    assert normalizar_texto(" Ana  María ") == "Ana  María"
def test_vacio():
    assert normalizar_texto("   ") == ""
