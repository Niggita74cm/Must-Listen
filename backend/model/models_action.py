from pydantic import BaseModel

class ActionMain(BaseModel):
    setting: bool = False
    find_string: str
    track_id: int = -1
    type: str
    ...

class ActionComment(BaseModel):
    text: str
    setting: bool = False
    close: bool = False
    track_id: int = -1
    rating: float
    ...
