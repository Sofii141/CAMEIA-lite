from cameia_lite.t01 import normalizar_texto
def test_recorta():
    assert normalizar_texto("  Ana  ") == "Ana"
def test_nfc():
    assert normalizar_texto("e\u0301") == "\u00e9"
