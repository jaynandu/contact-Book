import sqlite3

class Database:
    def __init__(self, db_name="contacts.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.create_table()

    def create_table(self):
        """Creates the contacts table if it does not exist."""
        query = """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def fetch_contacts(self):
        """Fetches all contacts from the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM contacts")
        return [
            {"id": row[0], "name": row[1], "email": row[2], "phone": row[3]}
            for row in cursor.fetchall()
        ]

    def add_contact(self, name, email, phone):
        """Adds a new contact to the database."""
        query = "INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)"
        self.connection.execute(query, (name, email, phone))
        self.connection.commit()
