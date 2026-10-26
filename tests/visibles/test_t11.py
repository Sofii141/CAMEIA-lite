from cameia_lite.t11 import ContadorReintentos
def test_tope_ia():
    c = ContadorReintentos()
    for _ in range(3):
        c.registrar_fallo("IA")
    assert not c.puede_reintentar()
