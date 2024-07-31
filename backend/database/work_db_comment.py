from backend.database.models import Comment
from backend.model.models_track import CommentTrack
from sqlalchemy.orm import Session
from sqlalchemy import update

# Use with database Comment
def create_comment(db: Session, create_comment: CommentTrack):
    comment = Comment(
        user_id  = create_comment.user_id,
        track_id = create_comment.track_id,
        comment = create_comment.comment,
        date= create_comment.date
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment
def get_comments_user(db: Session, user_id: int):
    get_comment = db.query(Comment).filter(Comment.user_id == user_id).all()
    return get_comment

def update_comment(db: Session, comment_update: CommentTrack):
    print(f"update_comment user_id: {comment_update}")
    all_comment = get_comments_user(db, comment_update.user_id)
    for comment in all_comment:
        print(comment.date)
        print(f"comment_update.date:{comment_update.date}")

        if (comment.track_id == comment_update.track_id) and (str(comment.date) == str(comment_update.date)):
            print(f"UPDATE comment.id:{comment.id}")
            db.execute(update(Comment).where(Comment.id == comment.id).values(comment=comment_update.comment))
            db.commit()
            up_comment = db.query(Comment).filter(Comment.id == comment.id).first()
            db.refresh(up_comment)
            return up_comment

def get_all_comments(db: Session, track_id: int):
    all_data = db.query(Comment).filter(Comment.track_id == track_id).all()
    return all_data

def delete_all_comments_user(db: Session, user_id: int):
    delete_tracks = db.query(Comment).filter(Comment.user_id == user_id).all()
    db.delete(delete_tracks)
    db.commit()

# def delete_comment(db: Session, user_id: int, track_id: int, comment_text: src):
#     all_comment = get_comments_for_user(db, user_id)
#     for comment in all_comment:
#         if comment.track_id == track_id and comment.comment == comment_text:
#             db.delete(comment)
#             db.commit()
#             break
