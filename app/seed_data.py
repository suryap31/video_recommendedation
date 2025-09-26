from .database import SessionLocal, engine, Base
from .models import User, Video

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Clear existing data (optional, for fresh start)
db.query(Video).delete()
db.query(User).delete()
db.commit()

# Create multiple users
users = [
    User(username="tom"),
    User(username="alice"),
    User(username="bob"),
    User(username="charlie")
]

db.add_all(users)
db.commit()

# Refresh to get IDs
for user in users:
    db.refresh(user)

# Add videos for each user
videos = [
    # testuser
    Video(title="Funny Cats", category="Comedy", owner_id=users[0].id),
    Video(title="Python Tutorial", category="Education", owner_id=users[0].id),
    Video(title="AI Basics", category="Education", owner_id=users[0].id),

    # alice
    Video(title="Travel Vlog", category="Travel", owner_id=users[1].id),
    Video(title="Yoga for Beginners", category="Health", owner_id=users[1].id),
    Video(title="Standup Comedy", category="Comedy", owner_id=users[1].id),

    # bob
    Video(title="Football Highlights", category="Sports", owner_id=users[2].id),
    Video(title="Basketball Tutorial", category="Sports", owner_id=users[2].id),
    Video(title="Python Advanced", category="Education", owner_id=users[2].id),

    # charlie
    Video(title="Cooking Pasta", category="Food", owner_id=users[3].id),
    Video(title="AI Basics", category="Education", owner_id=users[3].id),
    Video(title="Travel Vlog Europe", category="Travel", owner_id=users[3].id),
]

db.add_all(videos)
db.commit()
db.close()

print("Multiple users and videos added!")
