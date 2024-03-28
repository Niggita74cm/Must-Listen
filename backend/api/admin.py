from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.model.models_admin import ChooseAction, UserCreateAdmin, DataForAdmin

from backend.database.work_user_db import create_new_user
from backend.api.form.form_identific import UserCreateForm, filling_user
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER
from sqlalchemy.exc import IntegrityError
router = APIRouter()


#Админ роль
# Удалять коменты пользователей
# Удалять юзеров
# Создавать пользователя

@router.get("/app/LK/admin")
async def get_admin_menu():
    print("Get_admin_menu")
    return {"admin_menu": "List menu"}
@router.get("/app/LK/admin/create_user")
async def get_admin_create_user():
    print("get_admin_create_user")
    return {"admin_user": "List create user"}
@router.get("/app/LK/admin/delete_comment")
async def get_admin_delete_comment():
    print("get_admin_delete_comment")
    return {"admin_comment": "List delete comment"}
@router.get("/app/LK/admin/delete_user")
async def get_admin_delete_user():
    print("get_admin_create_user")
    return {"admin_comment": "List create user"}

#{
#choose_create_user:bool
#choose_delete_user:bool
#choose_delete_coment:bool
#close:bool
#}
#UserCreate
@router.post("/app/LK/admin", response_model=ChooseAction )
async def choose_menu(action: ChooseAction, db: Session = Depends(get_db)):
    if action.choose_create_user:
        print("choose_create_user")
    elif action.choose_delete_comment:
        print("choose_delete_comment")
    elif action.choose_delete_user:
        print("choose_delete_user")
    else:
        print("close")
    return choose_menu(action, db)

#UserCreate
@router.post("/app/LK/admin/create_user", response_model=UserCreateAdmin)
async def create_user(current_user: UserCreateAdmin, db: Session = Depends(get_db)):
    if current_user.close == False:
        form = UserCreateForm(current_user)
        await form.load_data()
        if await form.is_valid():
            user, user_data = filling_user(form)
            try:
                print("trying login")
                user_ = create_new_user(user_Create=user, db=db, user_data=user_data)
            except IntegrityError:
                print("Error: create_new_user")
    response = RedirectResponse(url="/app/LK/admin", status_code=HTTP_303_SEE_OTHER)
    return response


@router.delete("/app/LK/admin/delete_comment", response_model=DataForAdmin)
async def delete_comment(data: DataForAdmin, db: Session = Depends(get_db)):
    return await delete_comment(data, db)
@router.delete("/app/LK/admin/delete_user", response_model=DataForAdmin)
async def delete_user(data: DataForAdmin, db: Session = Depends(get_db)):
    if data.delete == False:
        try:
            print("trying delete")
            user = create_new_user(user_Create=user, db=db, user_data=user_data)
        except IntegrityError:
            print("Error: delete_user")
    response = RedirectResponse(url="/app/LK/admin", status_code=HTTP_303_SEE_OTHER)
    return await delete_user(db)
