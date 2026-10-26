from cameia_lite.t16 import validar_formacion
def test_en_curso():
    assert validar_formacion("2023-08", None) == []
def test_formato():
    assert validar_formacion("20201-01", None) == ["INVALID_FORMAT"]
    assert validar_formacion("2020-13", None) == ["INVALID_FORMAT"]
    assert validar_formacion("2020-1", "2021-01") == ["INVALID_FORMAT"]
def test_anio_cero():
    assert validar_formacion("0000-05", "2020-01") == ["YEAR_ZERO"]
