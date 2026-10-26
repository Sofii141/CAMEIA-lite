from cameia_lite.t10 import mensajes_por_campo, CATALOGO
def test_un_campo():
    p = {"errors": [{"field": "empresa", "code": "COMPANY_INVALID_CHARACTERS"}]}
    assert mensajes_por_campo(p) == {"empresa": CATALOGO["COMPANY_INVALID_CHARACTERS"]}
