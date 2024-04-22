from sqlalchemy import false, update
from backend.security_util.hashing import Hasher
from backend.database.models import User, Track, User_track, Comment
from backend.model.models_auth import UserCreate, UserDataCreate, UserGet
from sqlalchemy.orm import Session
# Use with database Track
def get_all_track(db: Session):
    all_data = db.query(Track).all()
    return all_data
def delete_track(db: Session, id_track: int):
    track = db.query(Track).filter(Track.id == id_track).all()
    db.delete(track)
    db.commit()
def create_track(db: Session, track: Track):
    create_track = Track(
        name = track.name,
        type_track = track.type_track,
        data_track = track.data_track
    )
    db.add(create_track)
    db.commit()
    db.refresh(create_track)
    return create_track


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
def delete_track_for_user(db: Session, track_id: int):
    delete_track = db.query(Track).filter(Track.track_id == track_id).all()
    db.delete(delete_track)
    db.commit()
def delete_all_track_users(db: Session, user_id: int):
    delete_track = db.query(User_track).filter(User_track.user_id == user_id).all()
    db.delete(delete_track)
    db.commit()

# Use with database Comment
def create_comment(db: Session, create_comment: Comment):
    comment = Comment(
        user_id  = create_comment.user_id,
        track_id = create_comment.track_id,
        comment = create_comment.comment
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_all_comments(db: Session):
    all_data = db.query(Comment).all()
    return all_data
def get_comments_for_user(db: Session, user_id: int):
    get_comment = db.query(Comment).filter(Comment.user_id == user_id).all()
    return get_comment
def delete_all_comments_user(db: Session, user_id: int):
    delete_tracks = db.query(Comment).filter(Comment.user_id == user_id).all()
    db.delete(delete_tracks)
    db.commit()
def delete_comment(db: Session, user_id: int, track_id: int, comment_text: str):
    all_comment = get_comments_for_user(db, user_id)
    for comment in all_comment:
        if comment.track_id == track_id and comment.comment == comment_text:
            db.delete(comment)
            db.commit()
            break
def update_comment(db: Session, user_id: int, track_id: int, comment_text: str, up_text: str):
    all_comment = get_comments_for_user(db, user_id)
    for comment in all_comment:
        if comment.track_id == track_id and comment.comment == comment_text:
            db.execute(update(Comment).where(Comment.id == comment.id).values(comment = up_text))
            db.commit()
            up_comment = db.query(Comment).filter(Comment.id == comment.id).all()
            db.refresh(up_comment)
            return up_comment