from models import SessionLocal, Contact

def clean_database():
    """Deletes all data from the contacts table."""
    session = SessionLocal()
    session.query(Contact).delete()
    session.commit()
    session.close()
    print("Database cleaned successfully.")

if __name__ == "__main__":
    clean_database()
