from cameia_lite.t10 import mensajes_por_campo, MENSAJE_GENERICO
def test_desconocido():
    p = {"errors": [{"field": "empresa", "code": "COMPANY_INVALID_CHARACTERS"}, {"field": "x", "code": "RARO"}]}
    assert mensajes_por_campo(p) == {"_general": MENSAJE_GENERICO}
def test_sin_errors_no_filtra_detail():
    r = mensajes_por_campo({"detail": "SQL error at line 3"})
    assert r == {"_general": MENSAJE_GENERICO}
def test_varios():
    p = {"errors": [{"field": "cargo", "code": "POSITION_INVALID_CHARACTERS"}, {"field": "titulo", "code": "DEGREE_INVALID_CHARACTERS"}]}
    assert set(mensajes_por_campo(p)) == {"cargo", "titulo"}
