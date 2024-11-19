from models import init_db

def initialize_database():
    """Initializes the database and creates all tables."""
    init_db()
    print("Database initialized successfully.")

if __name__ == "__main__":
    initialize_database()
