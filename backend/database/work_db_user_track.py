from sqlalchemy import false, update
from backend.database.models import User_track
from sqlalchemy.orm import Session
# Use with database User_track
def get_user_track(db: Session, user_id: int):
    user_track = db.query(User_track).filter(User_track.user_id == user_id).all()
    return user_track
def create_user_track(db: Session, user_track: User_track):
    create_user_track = User_track(
        user_id = user_track.user_id,
        track_id = user_track.track_id,
        rating = user_track.rating
    )
    db.add(create_user_track)
    db.commit()
    db.refresh(create_user_track)
    return create_user_track

def delete_track_users(db: Session, user_id: int):
    delete_track = db.query(User_track).filter(User_track.user_id == user_id).all()
    db.delete(delete_track)
    db.commit()
