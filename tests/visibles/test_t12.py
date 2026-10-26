from cameia_lite.t12 import CreadorUnaVez
def test_simple():
    assert CreadorUnaVez(lambda: 42).crear() == 42
