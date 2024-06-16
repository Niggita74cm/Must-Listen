from pydantic import BaseModel
from typing import List
class CommentTrack(BaseModel):
    comment: str
    track_id: int
    user_id: int
    date: str

class RatingTrack(BaseModel):
    track_id: int
    rating: int
    rating_old: int
class SaveTrack(BaseModel):
    track_id: int
    rating: int
    user_id: int
    date:str
class RatingComment(BaseModel):
    track_id: int
    rating: int
    comment: str
    commentInd: int #0-проставляется рейтинг, 1-новый комментарий, 2-обновление комментария
    date: str #не пустое если действие: обновление комментария

class SendComments(BaseModel):
    login: str
    comment: str
class SendTrack(BaseModel):
    track_id: int
    rating: int
    comments: List[SendComments]
