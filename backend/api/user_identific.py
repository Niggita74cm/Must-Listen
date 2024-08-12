from backend.database.work_user_db import create_new_user
from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from backend.model.models_auth import UserCreateFormPost, UserCreate
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from backend.services.checking_input_data import Verification
router = APIRouter()
@router.post("/RegistrUserPage")
async def UserRegistration(current_user: UserCreateFormPost, db: Session = Depends(get_db), response: Response = None):
    print("RegistrUserPage Post")
    print(current_user)
    correct_form = Verification(db=db)
    if await correct_form.CheckAllNewData(NewLogin=current_user.username, NewPassword=current_user.password,
                                          NewEmail=current_user.email, ConfirmPassword=current_user.confirmPassword):
        user = UserCreate(
            login=current_user.username,
            email=current_user.email,
            password=current_user.password
        )
        try:
            print("trying login")
            user = create_new_user(user_Create=user, db=db)# добавление в bd
            response.set_cookie(key="user_id", value=str(user.id), httponly=True, samesite="lax")
        except IntegrityError:
            print("Error: create_new_user")
    return correct_form.errors
