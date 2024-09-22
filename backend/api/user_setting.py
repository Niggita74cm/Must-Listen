from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from backend.model.models_user import UserInfo, ConfigurationOptions, SettingsPostResponse
from backend.database.work_user_db import get_user_id
from backend.services.check_admin_user import check_on_admin
from backend.services.realization_settings import RealizationSettings, RealizationAdminSettings
router = APIRouter()

#удаление себя
#смена логина/пароля/почты
#выход из учетной записи
#включение двуфакторной аутентификации
#Изменение имени/фамилии

@router.get("/api/SettingsF", response_model=UserInfo)
async def menu_setting(request: Request, db: Session = Depends(get_db)):
    print("Get menu_setting")
    user_id = int(request.cookies.get("user_id"))
    print(f"user_id: {user_id}")
    user = get_user_id(db=db, user_id=user_id)
    if check_on_admin(db=db, user_id=user_id):
        print("admin user")
        return UserInfo(
            username=user.login,
            email=user.email,
            second_factor= user.auth2,
            NumberPrivileges="admin"
        )
    return UserInfo(
            username=user.login,
            email=user.email,
            second_factor=user.auth2,
            NumberPrivileges="user"
    )





@router.post("/api/SettingsF", response_model=SettingsPostResponse)
async def main_setting(request: Request, user_action: ConfigurationOptions, db: Session = Depends(get_db)):
    print("Post main_setting")
    user_id = int(request.cookies.get("user_id"))
    print(f"user_id: {user_id}")

    realization_settings = RealizationSettings(db=db, user_id=user_id)
    if user_action.SettingsCommand == 'UpdateUsername':
        print("update login")
        res = realization_settings.UpdateUsername(NewUsername=user_action.NewData)
        print(f"res: {res}")
        return res
    if user_action.SettingsCommand == 'UpdateEmail':
        print("update email")
        return realization_settings.UpdateEmail(user_action.NewData)
    if user_action.SettingsCommand == 'UpdatePassword':
        print("update password")
        return realization_settings.UpdatePassword(user_action.NewData, user_action.OldData)
    if user_action.SettingsCommand == 'UpdateSecondFactor':
        print("update second-factor")
        return realization_settings.UpdateSecondFactor(user_action.NewData)
    if user_action.SettingsCommand == 'DeleteYourself':
        print("delete yourself")
        return realization_settings.DeleteYourself()
    if user_action.SettingsCommand == 'LogOutAccount':
        print("Log out of your account")
        return realization_settings.LogOutAccount(request=request)


    if check_on_admin(db, user_id):
        realization_admin_settings = RealizationAdminSettings(db=db, user_id=user_id)
        if user_action.SettingsCommand == 'DeleteUser':
            print("delete user")
            return realization_admin_settings.DeleteUser(UsersUsername=user_action.NewData)
        if user_action.SettingsCommand == 'AddTracks':
            print("add tracks")
            return realization_admin_settings.AddTracks(NameDatabaseTracks=user_action.NewData)
        if user_action.SettingsCommand == 'DeleteComments':
            ...
