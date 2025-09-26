from .database import Base, engine
from .models import User, Video

Base.metadata.create_all(bind=engine)
print("Tables created!")
