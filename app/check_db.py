from .database import SessionLocal
from .models import User, Video

def main():
    db = SessionLocal()

    print("\nUSERS:")
    users = db.query(User).all()
    for user in users:
        print(f"{user.id} - {user.username}")

    print("\nVIDEOS:")
    videos = db.query(Video).all()
    for video in videos:
        print(f"{video.id} - {video.title} (user_id={video.user_id})")

    db.close()

if __name__ == "__main__":
    main()
