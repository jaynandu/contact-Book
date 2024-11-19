from models import init_db, SessionLocal, Contact

def seed_data():
    """Seeds the database with initial contact data."""
    session = SessionLocal()

    contacts = [
        {"name": "Alice Smith", "email": "alice@example.com", "phone": "+123456789"},
        {"name": "Bob Johnson", "email": "bob@example.com", "phone": "+987654321"},
        {"name": "Charlie Brown", "email": "charlie@example.com", "phone": "+192837465"}
    ]

    for contact in contacts:
        existing_contact = session.query(Contact).filter(Contact.email == contact["email"]).first()
        if not existing_contact:
            session.add(Contact(**contact))

    session.commit()
    session.close()
    print("Sample data seeded successfully.")

if __name__ == "__main__":
    init_db()  # Ensures database tables are created
    seed_data()
