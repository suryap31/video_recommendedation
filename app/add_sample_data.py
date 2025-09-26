from database import SessionLocal
from models import User, Video

db = SessionLocal()

# Add users
user1 = User(username="testuser")
db.add(user1)
db.commit()

# Add videos
video1 = Video(title="video1", user_id=user1.id)
video2 = Video(title="video2", user_id=user1.id)
db.add_all([video1, video2])
db.commit()
db.close()
