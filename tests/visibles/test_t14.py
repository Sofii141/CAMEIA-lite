from cameia_lite.t14 import sustituir_rol
def test_lugar():
    assert sustituir_rol(["a", "b", "c"], "b", "x") == ["a", "x", "c"]
