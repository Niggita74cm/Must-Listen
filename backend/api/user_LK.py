from typing import List
from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from backend.services.work_LK import TracksOnPage, SortingTrackUser, GetCorrectUserTracks, LKTrack
from starlette.responses import Response
router = APIRouter()



#так это страница личного кабинета здесь отсылка данных о треках пользователя идет, ну и отрисовка самого фронта
@router.get("/api/MainPage", response_model=List[LKTrack])
async def main_LK(request: Request,response: Response, NumberPage: int, TypeSorting: str, db: Session = Depends(get_db)):
    print("Get main_LK")
    user_id = request.cookies.get("user_id")
    # print(f"user_id: {user_id}")
    user_track = GetCorrectUserTracks(db=db, user_id=int(user_id))
    # print(user_track)
    # print(f'Sorting: {TypeSorting}')
    # print(f'Page: {NumberPage}')
    user_track = SortingTrackUser(TypeSorting, user_track)
    user_track = TracksOnPage(NumberPage, user_track)
    response.headers["X-Frame-Options"] = "DENY"
    return user_track
