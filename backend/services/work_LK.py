from backend.database.work_db_user_track import get_user_track
from backend.database.work_db_track import get_track
from backend.model.models_action import LKTrack
from sqlalchemy.orm import Session
#Организация деления на страницы
def TracksOnPage(page: int, list_tracks: list) -> list:
    ...
#Организация сортировки в соответствии с  TrackSorting
def SortingTrackUser(IndSorting: str, list_tracks: list) -> list:
    ...

# перевод данных в состояние которое можно выводить на фронт
def OrganizationTrackUser(db: Session, user_id: int )-> list:
    user_tracks = get_user_track(db, user_id)
    ShowTrackUser = []
    for track_data in user_tracks:
        track = get_track(db, track_data.track_id)
        need_data = LKTrack(
            TrackName=track.track_name,
            ratingSelf=track_data.ratingSelf,
            ratingService=track.rating,
            date=track_data.date,
            type=""

        )
        ShowTrackUser.append(need_data)
    return ShowTrackUser