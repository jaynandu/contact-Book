from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy Base
Base = declarative_base()

# SQLAlchemy Engine and Session
DATABASE_URL = "sqlite:///contacts.db"  # Update this for production, e.g., DynamoDB or PostgreSQL
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Contact Model
class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)

    def __repr__(self):
        return f"<Contact(name={self.name}, email={self.email}, phone={self.phone})>"

# Create Tables
def init_db():
    """Initializes the database and creates tables."""
    Base.metadata.create_all(bind=engine)
