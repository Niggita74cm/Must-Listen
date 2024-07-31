from backend.database.work_db_user_track import get_user_track
from backend.database.work_db_track import get_track
from backend.model.models_action import LKTrack
from sqlalchemy.orm import Session
from datetime import datetime
#Организация деления на страницы
def TracksOnPage(page: int, list_tracks: list) -> list:
    page = page * 20
    if len(list_tracks) <= page:
        return list_tracks[page-20:]
    else:
        return list_tracks[page-20:page]

#
def SortingByDate(list_tracks: list[LKTrack], direction: str ) -> list:
    sorted_tracks = {}
    result_list = []
    for i in range(len(list_tracks)):
        sorted_tracks[i] = datetime.strptime(list_tracks[i].date, '%Y-%m-%d %H:%M:%S')
        result_list.append(None)
    if direction == "date_down":
        date_pairs = list(sorted_tracks.items())
        date_pairs.sort(key=lambda x: x[1])
    else:
        date_pairs = list(sorted_tracks.items())
        date_pairs.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(list_tracks)):
        result_list[i] = list_tracks[date_pairs[i][0]]
    return result_list

#
def SortingByRatingServer(list_tracks: list[LKTrack], direction: str ) -> list:
    sorted_tracks = {}
    result_list = []
    for i in range(len(list_tracks)):
        sorted_tracks[i] = list_tracks[i].ratingService
        result_list.append(None)
    print(sorted_tracks)
    if direction == "RatingServer_down":
        date_pairs = list(sorted_tracks.items())
        date_pairs.sort(key=lambda x: x[1])
    else:
        date_pairs = list(sorted_tracks.items())
        date_pairs.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(list_tracks)):
        result_list[i] = list_tracks[date_pairs[i][0]]
    return result_list

#
def SortingByRatingSelf(list_tracks: list[LKTrack], direction: str ) -> list:
    sorted_tracks = {}
    result_list = []
    for i in range(len(list_tracks)):
        sorted_tracks[i] = list_tracks[i].ratingSelf
        result_list.append(None)
    if direction == "RatingSelf_down":
        date_pairs = list(sorted_tracks.items())
        date_pairs.sort(key=lambda x: x[1])
    else:
        date_pairs = list(sorted_tracks.items())
        date_pairs.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(list_tracks)):
        result_list[i] = list_tracks[date_pairs[i][0]]
    return result_list

#Организация сортировки в соответствии с  TrackSorting
def SortingTrackUser(IndSorting: str, list_tracks: list) -> list:
    if "date" in IndSorting:
        list_tracks = SortingByDate(list_tracks, IndSorting)
    elif "RatingServer" in IndSorting:
        list_tracks = SortingByRatingServer(list_tracks, IndSorting)
    elif "RatingSelf" in IndSorting:
        list_tracks = SortingByRatingSelf(list_tracks, IndSorting)
    elif IndSorting == "type":
        #эм в бд нет типа))))
        ...
    return list_tracks

# перевод данных в состояние которое можно выводить на фронт
def GetCorrectUserTracks(db: Session, user_id: int)-> list:
    user_tracks = get_user_track(db, user_id)
    ShowTrackUser = []
    for track_data in user_tracks:
        track = get_track(db, track_data.track_id)
        print(track.track_name)
        need_data = LKTrack(
            TrackName=track.track_name,
            ratingSelf=track_data.ratingSelf,
            ratingService=track.rating,
            date=str(track_data.date),
            type=""

        )
        ShowTrackUser.append(need_data)
    return ShowTrackUser