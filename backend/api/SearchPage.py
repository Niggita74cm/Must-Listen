from typing import List

from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request, Cookie
from sqlalchemy.orm import Session
from backend.model.models_action import SearchResults
router = APIRouter()

#даже не знаю как сюда передовать, это может на фронте скорее всего делатся
@router.get("/app/SearchResults", response_model=List[SearchResults])
def get_search_results(request: Request, tracks: List[SearchResults], db: Session = Depends(get_db), cookie_value: str = Cookie(None)):
    print(f"Полученное значение cookie: {cookie_value}")
    return tracks


# @router.post("/app/SearchResults", response_model=ClickTrack)
# def get_search_results(request: Request, tracks: ClickTrack, db: Session = Depends(get_db), cookie_value: src = Cookie(None)):
#     return tracks
