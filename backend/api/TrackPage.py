from typing import List

from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request, Cookie
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER
from backend.model.models_track import RatingTrack, CommentTrack, RatingComment
from backend.database.work_db_track import get_track, update_rating, update_num_rating
router = APIRouter()

# вот это просто в оприори доделать
# def create_comment(db: Session, text: str):
#     ...
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
        new_rating = ((old_rating*number_rating) - rating.rating_old+ rating.rating)/number_rating
        update_rating(db, rating.track_id,new_rating)
        return new_rating
    old_rating = track.rating
    number_rating = track.number_rating
    new_rating = ((old_rating * number_rating) + rating.rating) / (number_rating+1)
    number_rating += 1
    update_rating(db, rating.track_id, new_rating)
    update_rating(db, rating.track_id, number_rating)
    return new_rating

@router.get("/app/LK/track")
async def track_page(request: Request, db: Session = Depends(get_db)):
    ...

@router.post("/app/LK/track", response_model=RatingComment)
async def WritingCommentRating(request: Request, rating_comment: RatingComment, db: Session = Depends(get_db)):
    print("TrackRating")
    print(f"rating:{rating_comment}")
    print(f"request.cookies.get(user_id): {request.cookies.get("user_id")}")
    if rating_comment.commentInd == False:
        rating = RatingTrack(
            track_id=rating_comment.track_id,
            rating=rating_comment.rating
        )

    else:
        comment = CommentTrack(
            track_id=rating_comment.track_id,
            comment=rating_comment.comment
        )

    return rating_comment

