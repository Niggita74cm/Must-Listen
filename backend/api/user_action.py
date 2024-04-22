from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from backend.model.models_action import ActionMain, ActionComment
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER
from backend.database.work_db_track import get_all_track, get_user_track
#вот эту фигню надо исправить
from backend.api.admin import find_similar_strings
router = APIRouter()

# вот это просто в оприори доделать
def create_comment(db: Session, text: str):
    ...
def delete_comment(db: Session, text: str):
    ...
def update_comment(db: Session, text: str):
    ...

def check_on_admin(db: Session, user_id):
    return True

find_str = [None]
@router.get("/app/LK")
async def main_LK(request: Request, db: Session = Depends(get_db)):
    if find_str[0] is None:
        ...
    return {"message": "main_LK"}

@router.get("/app/LK/track")
async def track_list(request: Request, db: Session = Depends(get_db)):
    ...

#для кнопок
@router.post("/app/LK", response_model=ActionMain)
async def main_LK(request: Request, action: ActionMain, db: Session = Depends(get_db)):
    if await action.setting == False:
        if action.track_id != -1:
            response = RedirectResponse(url=f"/app/LK/admin", status_code=HTTP_303_SEE_OTHER)
            response.set_cookie(key="track_id", value = action.track_id, secure=True)
        else:
            response = RedirectResponse(url=f"/app/LK", status_code=HTTP_303_SEE_OTHER)
            find_str[0] = find_similar_strings(action.text, find_str[0], "name")
            ...
    else:
        if check_on_admin(db) == True:
            response = RedirectResponse(url=f"/app/LK/admin", status_code=HTTP_303_SEE_OTHER)
        else:
            response = RedirectResponse(url=f"/app/LK/setting", status_code=HTTP_303_SEE_OTHER)
    return response

@router.post("/app/LK/track", response_model=ActionComment)
async def track_list(request: Request, db: Session = Depends(get_db)):
    ...


