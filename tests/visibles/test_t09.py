from cameia_lite.t09 import nivel_log
def test_500():
    assert nivel_log(500) == "ERROR"
def test_404():
    assert nivel_log(404) == "INFO"
