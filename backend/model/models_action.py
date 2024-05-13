from pydantic import BaseModel


# class ActionComment(BaseModel):
#     text: str
#     setting: bool = False
#     close: bool = False
#     track_id: int = -1
#     rating: float
#     ...
# данные необходимые для формироывния вывода
class ShowTrack(BaseModel):
    TrackSorting: str = "date_down"  # может быть "date_up" - вначале ранее, "date_down", "type", "RatingServer_up", "RatingServer_down" , "RatingSelf_up", "RatingSelf_down" (по умолчанию по дате сортировка)
    TrackName: str  # используется для поиска, либо глобального, либо по личным трекам
    SearchIndic: bool  # переход на режим поиска true- поиск, false- работа с личными треками
    Setting: bool  # переход на страницу настройки пользователя
    NumberPage: int = 1  # страница личных треков, треки разделены по 20 штук на страницу
    #ClickTrack: bool = False # если true- переход на страницу треков, false- другая работа(не понятно нужно ли это)


# используется для формирования вывода в личном кабинете пользователя
class LKTrack(BaseModel):
    TrackName: str
    ratingSelf: int
    ratingService: float
    date: str
    type: str


# используется для вывода результата поиска
class SearchResults(BaseModel):
    track_id: int
    track_name: str
    album_name: str
    artists: str
    rating: float
