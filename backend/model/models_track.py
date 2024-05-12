from pydantic import BaseModel

class CommentTrack(BaseModel):
    comment: str
    track_id: int
class RatingTrack(BaseModel):
    track_id: int
    rating: int
    rating_old: int
class RatingComment(BaseModel):
    track_id: int
    rating: int
    comment: str
    commentInd: bool
    rating_old: int