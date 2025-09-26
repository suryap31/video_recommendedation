from app.database import SessionLocal
from app.models import User

# Create a new session
db = SessionLocal()

# Add a test user
test_user = User(username="testuser")
db.add(test_user)
db.commit()
db.close()

print("Test user inserted!")
