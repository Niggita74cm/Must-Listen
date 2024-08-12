from datetime import datetime
from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from backend.model.models_track import RatingTrack, CommentTrack, SaveTrack
from backend.database.work_db_track import get_track, update_rating, update_num_rating
from backend.database.work_db_comment import create_comment, update_comment, get_all_comments, delete_comment
from backend.database.work_db_user_track import create_user_track, update_user_track,get_track_rating
from backend.database.work_user_db import get_user_id
from backend.model.models_action import SelectedTrack, TrackComments, FormPostRatingComment, FormPostResponse
router = APIRouter()
from backend.services.check_admin_user import check_on_admin





def update_rating_track(rating: RatingTrack, db: Session):
    track = get_track(db, rating.track_id)
    print(f'RatingTrack: {rating}')
    if rating.rating_old != 0:
        old_rating = track.rating
        number_rating = track.number_rating
        new_rating = ((old_rating*number_rating) - rating.rating_old + rating.rating)/number_rating
        print(f'new_rating: {new_rating}')
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
    comment = create_comment(db, comment)
    return comment

def delete_user_comment(db: Session, comment_id: int):
    delete_comment(db=db, comment_id=comment_id)
def update_comment_track(comment: CommentTrack, db: Session):
    create_comment(db, comment)

#так не понятно как получать id трека(в теории через url параметр)
@router.get("/MusicPage", response_model=SelectedTrack)
async def track_page(request: Request, track_id: int, db: Session = Depends(get_db)):
    print("Getting track page")
    user_id = int(request.cookies.get("user_id"))
    userInfo = get_user_id(db=db, user_id=user_id)
    track = get_track(db, track_id)
    print(f'track_id: {track_id}')
    print(f'user_id: {user_id}')
    user_track_rating = get_track_rating(db=db, track_id=track_id, user_id=user_id)
    print(f'user_track_rating: {user_track_rating}')
    comments_track = get_all_comments(db, track_id)
    print(f'comments_track: {comments_track}')
    send_comment = []
    for comment in comments_track:
        print(f'comment.user_id: {comment.user_id}')
        users = get_user_id(user_id=comment.user_id, db=db)
        print(f'users.login: {users.login}')
        print(f'comment_id: {comment.id}')
        print(f'time: {str(comment.date)}')
        print(f'text_comment: {comment.comment}')
        CommentForm = TrackComments(
            comment_id=comment.id,
            user_name=users.login,
            time=str(comment.date),
            text_comment=comment.comment
        )
        print(f'send_comment: {send_comment}')
        send_comment.append(CommentForm)
    NumberPrivileges = ''
    if check_on_admin(db=db, user_id=user_id):
        NumberPrivileges = 'admin'
    else:
        NumberPrivileges = 'user'
    print(f'NumberPrivileges: {NumberPrivileges}')
    return SelectedTrack(
        track_id=track_id,
        track_name=track.track_name,
        album_name=track.album_name,
        artists=track.artists,
        rating=track.rating,
        popularity=track.popularity,
        duratind_ms=track.duration_ms,
        url_images=track.picture_track,
        track_comments=send_comment,
        userRating=user_track_rating,
        username=userInfo.login,
        NumberPrivileges=NumberPrivileges
    )

@router.post("/MusicPage", response_model=FormPostResponse)
async def SetRatingAndWritingComment(request: Request, rating_comment: FormPostRatingComment, db: Session = Depends(get_db)):
    current_datetime = datetime.now()
    timestamp_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    user_id = int(request.cookies.get("user_id"))
    if rating_comment.command == "Set Rating":
        print("Set rating")
        print(f"track_id: {rating_comment.track_id}")
        rating_old = get_track_rating(db, user_id, rating_comment.track_id)
        print(f"rating_old: {rating_old}")
        rating = RatingTrack(
            track_id=rating_comment.track_id,
            rating=rating_comment.rating,
            rating_old=rating_old
        )
        update_rating_track(rating, db)
        save_track = SaveTrack(
            track_id=rating.track_id,
            rating=rating_comment.rating,
            user_id=user_id,
            date=timestamp_str
        )
        if rating_old == 0:
            print("Creating new Rating")
            create_user_track(db, save_track)
        else:
            print("Updating Rating")
            update_user_track(db, save_track)
        return FormPostResponse(
            errors='',
            date=timestamp_str,
            comment_rating_id=rating_comment.track_id
        )
    elif rating_comment.command == "Writing Comment":
        print("Writing Comment")
        comment = CommentTrack(
            track_id=rating_comment.track_id,
            comment=rating_comment.comment,
            user_id=user_id,
            date=timestamp_str
        )
        created_comment = create_comment_track(comment, db)
        print(f'created_comment: {created_comment.id}')
        return FormPostResponse(
            errors='',
            date=timestamp_str,
            comment_rating_id=created_comment.id
        )
    elif rating_comment.command == "Delete Comment":
        print("Delete Comment")
        print(f"Deleted comment_id:{rating_comment.comment_id}")
        delete_user_comment(db=db, comment_id=rating_comment.comment_id)
        return FormPostResponse(
            errors='',
            date=timestamp_str,
            comment_rating_id=rating_comment.comment_id
        )
    elif rating_comment.command == "Update Comment":
        print("Update Comment")
        #update_comment(db, comment)
    return "Rating"

