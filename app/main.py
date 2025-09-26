from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import random
from .database import SessionLocal, engine
from . import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from localhost (your frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for simplicity
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Video Recommendation Engine is running!"}

@app.get("/feed")
def get_feed(username: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not user.videos:
        return {"username": username, "videos": []}

    # Count category preference
    category_count = {}
    for video in user.videos:
        category_count[video.category] = category_count.get(video.category, 0) + 1

    # Pick top category
    top_category = max(category_count, key=category_count.get)

    # Recommend 2 random videos from that category
    recommended = (
        db.query(models.Video)
        .filter(models.Video.category == top_category)
        .all()
    )

    recommended_titles = [v.title for v in random.sample(recommended, min(2, len(recommended)))]
    
    return {
        "username": username,
        "recommended_category": top_category,
        "videos": recommended_titles
    }
