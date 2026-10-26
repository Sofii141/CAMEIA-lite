import uuid
from cameia_lite.t18 import request_id
def test_minusculas():
    assert request_id("123E4567-E89B-12D3-A456-426614174000") == "123e4567-e89b-12d3-a456-426614174000"
def test_inyeccion():
    r = request_id("123e4567-e89b-12d3-a456-426614174000\nADMIN=1")
    assert "\n" not in r and "ADMIN" not in r
    uuid.UUID(r)
def test_basura():
    r = request_id("hola"); uuid.UUID(r)
    assert r != "hola" and request_id("") != ""
