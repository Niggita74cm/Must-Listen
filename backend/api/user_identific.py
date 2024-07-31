from backend.database.work_user_db import create_new_user
from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from backend.model.models_auth import UserCreateFormPost, UserCreate
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER
from backend.api.form.form_identific import UserCreateForm

router = APIRouter()


@router.post("/RegistrUserPage")
async def UserRegistration(current_user: UserCreateFormPost, db: Session = Depends(get_db), response: Response = None):
    print("RegistrUserPage Post")
    print(current_user)
    form = UserCreateForm(current_user)
    await form.load_data()
    if await form.is_valid(db):
        user = UserCreate(
            login=form.login,
            email=form.email,
            password=form.password
        )
        try:
            print("trying login")
            user = create_new_user(user_Create=user, db=db)# добавление в bd
            response.set_cookie(key="user_id", value=str(user.id), httponly=True, samesite="lax")
        except IntegrityError:
            print("Error: create_new_user")
    return form.errors
