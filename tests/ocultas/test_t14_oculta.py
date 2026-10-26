import pytest
from cameia_lite.t14 import sustituir_rol
def test_no_muta():
    r = ["a", "b"]; sustituir_rol(r, "a", "z")
    assert r == ["a", "b"]
def test_viejo_ausente():
    with pytest.raises(ValueError):
        sustituir_rol(["a"], "q", "z")
def test_nuevo_duplicado():
    with pytest.raises(ValueError):
        sustituir_rol(["a", "b"], "a", "b")
