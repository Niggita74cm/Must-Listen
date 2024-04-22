from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from backend.model.models_user import UserSetting, UserSettingPassword
from backend.database.work_user_db import delete_user, delete_user_data, get_user_id
from backend.database.work_db_track import delete_all_track_users
from backend.database.work_user_db import (update_user_auth, update_user_login,
                                           update_user_email, update_user_password,
                                           update_user_data_name, update_user_data_surname)
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER
from backend.security_util.hashing import Hasher
router = APIRouter()


#удаление себя
#смена логина/пароля/почты
#выход из учетной записи
#включение двуфакторной аутентификации
#Изменение имени/фамилии

@router.get("/app/LK/setting")
async def menu_setting(request: Request, db: Session = Depends(get_db)):
    return {"message": "menu_setting"}
@router.get("/app/LK/setting/passwd")
async def list_up_password(request: Request, db: Session = Depends(get_db)):
    return {"message": "list_up_password"}

@router.post("/app/LK/setting", response_model=UserSetting)
async def main_setting(request: Request, user_action: UserSetting, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    response = RedirectResponse(url="/app/LK/setting", status_code=HTTP_303_SEE_OTHER)
    if user_action.delete_user == True:
        print("delete user")
        delete_user(user_id=user_id, db=db)
        delete_user_data(user_id=user_id, db=db)
        delete_all_track_users(db=db, user_id=user_id)
    if user_action.exit_user == True:
        print("exit user")
        request.cookies.clear()
        response = RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    if user_action.up_auth2 == True:
        print("update auth2")
        update_user_auth(user_id=user_id, up_data=user_action.auth2, db=db)
    if user_action.up_name == True:
        print("update name")
        update_user_data_name(user_id=user_id, up_data=user_action.name, db=db)
    if user_action.up_surname == True:
        print("update surname")
        update_user_data_surname(user_id=user_id, up_data=user_action.surname, db=db)
    if user_action.up_email == True:
        print("update email")
        update_user_email(user_id=user_id, up_data=user_action.email, db=db)
    if user_action.up_login == True:
        print("update login")
        update_user_login(user_id=user_id, up_data=user_action.login, db=db)
    if user_action.close == True:
        print("close")
        response = RedirectResponse(url="/app/LK", status_code=HTTP_303_SEE_OTHER)
    return response

@router.post("/app/LK/setting/passwd", response_model=UserSettingPassword)
async def up_password(request: Request, user_action: UserSettingPassword, db: Session = Depends(get_db)):
    user_id = request.cookies.get("user_id")
    response = RedirectResponse(url="/app/LK/setting/passwd", status_code=HTTP_303_SEE_OTHER)
    if user_action.close == True:
        print("close")
        response = RedirectResponse(url="/app/LK/setting", status_code=HTTP_303_SEE_OTHER)
    else:
        user_info = get_user_id(user_id, db)
        if Hasher.verify_password(user_info.password, user_action.password_valid):
            print("update password")
            update_user_password(user_id=user_id, up_data=user_action.password, db=db)
    return response