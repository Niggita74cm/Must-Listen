from typing import List
from datetime import datetime
from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request, Cookie
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER
from backend.model.models_track import RatingTrack, CommentTrack, RatingComment, SaveTrack
from backend.database.work_db_track import get_track, update_rating, update_num_rating
from backend.database.work_db_comment import create_comment, update_comment
from backend.database.work_db_user_track import create_user_track, update_user_track,get_track_rating
router = APIRouter()

# вот это просто в оприори доделать
# def delete_comment(db: Session, text: str):
#     ...
# def update_comment(db: Session, text: str):
#     ...
#
# def check_on_admin(db: Session, user_id):
#     return True

def update_rating_track(rating: RatingTrack, db: Session):
    track = get_track(db, rating.track_id)
    if rating.rating_old != -1:
        old_rating = track.rating
        number_rating = track.number_rating
        new_rating = ((old_rating*number_rating) - old_rating + rating.rating)/number_rating
        print(new_rating)
        update_rating(db, rating.track_id,new_rating)
        return new_rating
    old_rating = track.rating
    number_rating = track.number_rating
    new_rating = ((old_rating * number_rating) + rating.rating) / (number_rating+1)
    number_rating += 1
    update_rating(db, rating.track_id, new_rating)
    update_num_rating(db, rating.track_id, number_rating)

    return new_rating

def create_comment_track(comment: CommentTrack, db: Session):
    create_comment(db, comment)

def update_comment_track(comment: CommentTrack, db: Session):
    create_comment(db, comment)
@router.get("/app/LK/track")
async def track_page(request: Request, db: Session = Depends(get_db)):
    ...

@router.post("/app/LK/track", response_model=RatingComment)
async def WritingCommentRating(request: Request, rating_comment: RatingComment, db: Session = Depends(get_db)):
    current_datetime = datetime.now()
    timestamp_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    user_id = int(request.cookies.get("user_id"))
    print("TrackRating")
    print(f"rating:{rating_comment}")
    print(f"request.cookies.get(user_id): {request.cookies.get("user_id")}")
    if rating_comment.commentInd == 0:
        print("RatingInd")
        rating_old  =get_track_rating(db, user_id, rating_comment.track_id)
        rating = RatingTrack(
            track_id=rating_comment.track_id,
            rating=rating_comment.rating,
            rating_old=rating_old
        )
        print("RatingInd2")
        update_rating_track(rating, db)
        save_track = SaveTrack(
            track_id=rating.track_id,
            rating=rating_comment.rating,
            user_id=user_id,
            date=timestamp_str
        )
        if rating_old == -1:
            create_user_track(db, save_track)
        else:
            update_user_track(db, save_track)
    else:
        comment = CommentTrack(
            track_id=rating_comment.track_id,
            comment=rating_comment.comment,
            user_id=user_id,
            date=timestamp_str
        )
        if rating_comment.commentInd == 1:
            create_comment_track(comment, db)
        elif rating_comment.commentInd == 2:
            update_comment(db, comment)
    return rating_comment

