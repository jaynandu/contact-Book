import json
from handler import get_contacts, add_contact

def test_get_contacts():
    event = {"headers": {"Authorization": "Bearer valid-token"}}
    response = get_contacts(event, None)
    assert response["statusCode"] == 200

def test_add_contact():
    event = {
        "headers": {"Authorization": "Bearer valid-token"},
        "body": json.dumps({"name": "John Doe", "email": "john@example.com", "phone": "+1234567890"})
    }
    response = add_contact(event, None)
    assert response["statusCode"] == 200
