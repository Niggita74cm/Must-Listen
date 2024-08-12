from sqlalchemy import update
from backend.database.models import User_track
from sqlalchemy.orm import Session
from backend.model.models_track import SaveTrack
# Use with database User_track
def get_user_track(db: Session, user_id: int):
    user_track = db.query(User_track).filter(User_track.user_id == user_id).all()
    return user_track

def get_track_rating(db: Session, user_id: int, track_id: int):
    tracks = get_user_track(db, user_id)
    for track in tracks:
        if track.track_id == track_id:
            return track.ratingSelf
    return 0
def create_user_track(db: Session, user_track: SaveTrack):
    print(user_track)
    create_user_track = User_track(
        user_id = user_track.user_id,
        track_id = user_track.track_id,
        ratingSelf = user_track.rating,
        date = user_track.date
    )
    db.add(create_user_track)
    db.commit()
    db.refresh(create_user_track)
    return create_user_track

def update_user_track(db: Session, user_track: SaveTrack):
    tracks = get_user_track(db, user_track.user_id)

    for track in tracks:
        if track.track_id == user_track.track_id:
            print(f"update rating track: {track.ratingSelf}")
            db.execute(update(User_track).where(User_track.id == track.id).values(ratingSelf=user_track.rating))
            db.execute(update(User_track).where(User_track.id == track.id).values(date=user_track.date))
            db.commit()
            up_rating = db.query(User_track).filter(User_track.id == track.id).first()
            print(up_rating.ratingSelf)
            db.refresh(up_rating)
            return up_rating
#
def delete_tracks_users(db: Session, user_id: int):
    delete_tracks = db.query(User_track).filter(User_track.user_id == user_id).all()
    for track in delete_tracks:
        db.delete(track)
    db.commit()
