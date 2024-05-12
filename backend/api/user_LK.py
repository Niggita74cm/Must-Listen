from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request
from sqlalchemy.orm import Session

from backend.services.search import search_tracks
from backend.services.work_LK import TracksOnPage, SortingTrackUser, OrganizationTrackUser

from fastapi.responses import Response
from starlette.status import HTTP_303_SEE_OTHER
from backend.model.models_action import ShowTrack
from backend.database.work_db_track import get_all_track

router = APIRouter()



#так это страница личного кабинета здесь отсылка данных о треках пользователя идет, ну и отрисовка самого фронта
@router.get("/app/LK")
async def main_LK(request: Request, db: Session = Depends(get_db)):
    print("Get main_LK")
    user_id = request.cookies.get("user_id")
    user_track = OrganizationTrackUser(db=db, user_id=int(user_id))
    page = 1
    Sorting = "date"
    for cookie_name in request.cookies.keys():
        if cookie_name == "Sorting":
            Sorting = request.cookies.get("Sorting")
        if cookie_name == "Page":
            page = request.cookies.get("Page")
    print(f'Sorting: {Sorting}')
    print(f'Page: {page}')
    user_track = TracksOnPage(page, user_track)
    user_track = SortingTrackUser(Sorting, user_track)
    return user_track

@router.post("/app/LK", response_model=ShowTrack)
async def main_LK(request: Request, response: Response, action: ShowTrack, db: Session = Depends(get_db)):
    if await action.SearchIndic == True:
        all_track = get_all_track(db)
        found_tracks = search_tracks(action.TrackName, all_track)
        cookie_value = request.cookies.get("user_id")
        response.set_cookie(key="my_cookie", value=cookie_value)

        return found_tracks
        ...
    if await action.Setting == True:
        ...
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








