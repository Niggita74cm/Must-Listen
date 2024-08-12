from typing import List
from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from backend.services.work_LK import TracksOnPage, SortingTrackUser, GetCorrectUserTracks, LKTrack
router = APIRouter()



#так это страница личного кабинета здесь отсылка данных о треках пользователя идет, ну и отрисовка самого фронта
@router.get("/MainPage", response_model=List[LKTrack])
async def main_LK(request: Request, NumberPage: int, TypeSorting: str, db: Session = Depends(get_db)):
    print("Get main_LK")
    user_id = request.cookies.get("user_id")
    print(f"user_id: {user_id}")
    user_track = GetCorrectUserTracks(db=db, user_id=int(user_id))
    print(user_track)
    print(f'Sorting: {TypeSorting}')
    print(f'Page: {NumberPage}')
    user_track = SortingTrackUser(TypeSorting, user_track)
    user_track = TracksOnPage(NumberPage, user_track)
    return user_track
#
# @router.post("/MainPage", response_model=ShowTrack)
# async def main_LK(request: Request, response: Response, action: ShowTrack, db: Session = Depends(get_db)):
#     if action.SearchIndic == True:
#         all_track = get_all_track(db)
#         found_tracks = search_tracks(action.TrackName, all_track)
#         print(found_tracks)#то что на фронт передается
#         cookie_value = request.cookies.get("user_id")
#         response.set_cookie(key="user_id", value=cookie_value)
#         return action#надо чтоб сдесь было, то что надо передать
#     else:
#         cookie_value = request.cookies.get("user_id")
#         response.set_cookie(key="Sorting", value=action.TrackSorting)
#         response.set_cookie(key="Page", value=action.NumberPage)
#         response.set_cookie(key="user_id", value=cookie_value)
#
#         return response
    #if action.Setting == True:
    #    ...
    # if await action.setting == False:
    #     if action.track_id != -1:
    #         response = RedirectResponse(url=f"/app/LK/admin", status_code=HTTP_303_SEE_OTHER)
    #         response.set_cookie(key="track_id", value = action.track_id, secure=True)
    #     else:
    #         response = RedirectResponse(url=f"/app/LK", status_code=HTTP_303_SEE_OTHER)
    #         find_str[0] = find_similar_strings(action.text, find_str[0], "name")
    #         ...
    # else:
    #     if check_on_admin(db) == True:
    #         response = RedirectResponse(url=f"/app/LK/admin", status_code=HTTP_303_SEE_OTHER)
    #     else:
    #         response = RedirectResponse(url=f"/app/LK/setting", status_code=HTTP_303_SEE_OTHER)
    # return response








