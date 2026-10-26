from cameia_lite.t23 import progreso
def test_ok():
    assert progreso(2, 5) == "Pregunta 2 de 5"
