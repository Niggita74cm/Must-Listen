from typing import List

from pydantic import BaseModel


class TrackSearched(BaseModel):
    TrackName: str

# используется для формирования вывода в личном кабинете пользователя
class LKTrack(BaseModel):
    track_id: int
    TrackName: str
    ratingSelf: int
    ratingService: float
    AlbumName: str
    artists: str
    date: str
    type: str


# используется для вывода результата поиска
class SearchResults(BaseModel):
    track_id: int
    track_name: str
    album_name: str
    artists: str
    rating: float
    popularity: int




class TrackComments(BaseModel):
    comment_id: int
    user_name: str
    time: str
    text_comment: str
class SelectedTrack(BaseModel):
    track_id: int
    track_name: str
    album_name: str
    artists: str
    rating: float
    userRating: int
    popularity: int
    duratind_ms: int
    url_images: str
    username: str
    track_comments: List[TrackComments]
    NumberPrivileges: str

class FormPostRatingComment(BaseModel):
    track_id: int
    rating: int
    comment: str
    command: str
    comment_id: int
class FormPostResponse(BaseModel):
    errors: str
    date: str
    comment_rating_id: int