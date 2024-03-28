from backend.database.work_user_db import create_new_user
from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends
from backend.model.models_auth import UserCreateFormPost
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER
from backend.api.form.form_identific import UserCreateForm, filling_user

router = APIRouter()
@router.get("/identification")
def register():
    print("current_user")
    return {"data": "get identification"}


@router.post("/identification", response_model = UserCreateFormPost)
async def register(current_user: UserCreateFormPost, db: Session = Depends(get_db)):
    form = UserCreateForm(current_user)
    await form.load_data()
    if await form.is_valid():
        user, user_data = filling_user(form)
        try:
            print("trying login")
            user = create_new_user(user_Create=user, db=db, user_data=user_data)# добавление в bd
            response = RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
        except IntegrityError:
            print("Error: create_new_user")
    return response