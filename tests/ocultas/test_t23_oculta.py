import pytest
from cameia_lite.t23 import progreso
def test_bordes():
    assert progreso(1, 1) == "Pregunta 1 de 1" and progreso(5, 5) == "Pregunta 5 de 5"
def test_fuera():
    for k, t in [(0, 5), (6, 5), (1, 0)]:
        with pytest.raises(ValueError):
            progreso(k, t)
