from middleware import authenticate, cors_headers

@authenticate
def get_contacts(event, context):
    contacts = db.fetch_contacts()
    response = {
        "statusCode": 200,
        "body": json.dumps(contacts)
    }
    return cors_headers(response)
import json
from database import Database
from auth import decode_token
from validation import validate_email, validate_phone
from middleware import authenticate, cors_headers

db = Database()

@authenticate
def get_contacts(event, context):
    """Fetch all contacts from the database."""
    contacts = db.fetch_contacts()
    response = {
        "statusCode": 200,
        "body": json.dumps(contacts)
    }
    return cors_headers(response)

@authenticate
def add_contact(event, context):
    """Add a new contact to the database."""
    try:
        data = json.loads(event['body'])
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        # Validate inputs
        if not name or not email or not phone:
            raise ValueError("Name, email, and phone are required.")
        validate_email(email)
        validate_phone(phone)

        # Add contact
        db.add_contact(name, email, phone)
        response = {
            "statusCode": 200,
            "body": json.dumps({"message": "Contact added successfully."})
        }
    except ValueError as e:
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal Server Error", "details": str(e)})
        }
    return cors_headers(response)
