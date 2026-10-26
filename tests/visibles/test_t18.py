import uuid
from cameia_lite.t18 import request_id
def test_conserva_valido():
    assert request_id("123e4567-e89b-12d3-a456-426614174000") == "123e4567-e89b-12d3-a456-426614174000"
def test_genera():
    uuid.UUID(request_id(None))
