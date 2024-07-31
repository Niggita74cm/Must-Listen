from pydantic import BaseModel

# class ChooseAction(BaseModel):
#     choose_create_user: bool
#     choose_delete_user: bool
#     choose_delete_comment: bool
#     close: bool
#
# class UserCreateAdmin(BaseModel):
#     login: src
#     email: src
#     password: src
#     name: src
#     surname: src
#     confirmPassword: src
#     close: bool
#
# class DataForDeleteUser(BaseModel):
#     user_id: int
#     login: src
#     email: src
#     login_ind: bool
#     email_ind: bool
#     close: bool
#
#
# #переделать
# class DataForDeleteComment(BaseModel):
#     user_id: int
#     track_id: bool
#     text: src
#     text_ind: bool
#     login: src
#     login_ind: bool
#     close: bool

class NameDB(BaseModel):
    name_database: str
class LoadTrack(BaseModel):
    track_name: str
    artists: str
    album_name: str
    popularity: int
    duration_ms: int
    explicit: bool
    danceability: float
    energy: float
    key: int
    loudness: float
    mode: int
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    time_signature: int
    track_genre: str
    picture_track: str