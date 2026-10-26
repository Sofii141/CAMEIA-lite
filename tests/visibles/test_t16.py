from cameia_lite.t16 import validar_formacion
def test_ok():
    assert validar_formacion("2020-02", "2024-11") == []
def test_al_reves():
    assert validar_formacion("2024-01", "2020-01") == ["END_BEFORE_START"]
