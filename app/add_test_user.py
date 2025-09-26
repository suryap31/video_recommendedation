# add_test_user.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the User model (adjust if your project already has one)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Add a test user
db = SessionLocal()
test_user = User(username="testuser", email="testuser@example.com")
db.add(test_user)
db.commit()
db.close()

print("Test user added: username='testuser', email='testuser@example.com'")
