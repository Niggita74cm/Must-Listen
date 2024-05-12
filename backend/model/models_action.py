from pydantic import BaseModel

# class ActionMain(BaseModel):
#     setting: bool = False
#     find_string: str
#     track_id: int = -1
#     type: str
#     ...
#
# class ActionComment(BaseModel):
#     text: str
#     setting: bool = False
#     close: bool = False
#     track_id: int = -1
#     rating: float
#     ...

class ShowTrack(BaseModel):
    TrackSorting: str = "date" #может быть "date", "type", "RatingServer", "RatingSelf" (по умолчанию по дате сортировка)
    TrackName: str #используется для поиска, либо глобального, либо по личным трекам
    SearchIndic: bool #переход на режим поиска true- поиск, false- работа с личными треками
    Setting: bool #переход на страницу настройки пользователя
    NumberPage: int = 1 #страница личных треков, треки разделены по 20 штук на страницу

#используется для формирования вывода в личном кабинете пользователя
class LKTrack(BaseModel):
    TrackName: str
    ratingSelf: int
    ratingService: float
    date: str
    type: str

#используется для вывода результата поиска
class SearchResults(BaseModel):
    track_id: int
    track_name: str
    album_name: str
    artists: str
    rating: float

class ClickTrack(BaseModel):
    track_id: int
    TrackName: str
