from cameia_lite.t09 import nivel_log
def test_otros_4xx():
    assert nivel_log(400) == "WARN" and nivel_log(499) == "WARN"
def test_bordes_5xx():
    assert nivel_log(599) == "ERROR" and nivel_log(600) is None
def test_exito():
    assert nivel_log(200) is None and nivel_log(302) is None
