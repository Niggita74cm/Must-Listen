from typing import List

from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.database.work_db_track import get_all_track, search_track
from backend.services.search import search_tracks
from backend.model.models_action import SearchResults
router = APIRouter()

#даже не знаю как сюда передовать, это может на фронте скорее всего делатся
@router.get("/SearchResults", response_model=List[SearchResults])
def get_search_results(NameTrack: str,   db: Session = Depends(get_db)):
    print("get_search_results")
    print(f"NameTrack: {NameTrack}")
    search_all_track = search_track(db=db, name_track=NameTrack, albums_track=NameTrack, artists_track=NameTrack)
    found_tracks = search_tracks(NameTrack, search_all_track)
    print(found_tracks)
    return found_tracks


# @router.post("/app/SearchResults", response_model=ClickTrack)
# def get_search_results(request: Request, tracks: ClickTrack, db: Session = Depends(get_db), cookie_value: src = Cookie(None)):
#     return tracks
