from starlette.status import HTTP_303_SEE_OTHER

from backend.database.models import User
from backend.database.work_user_db import get_user
from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import true
from backend.model.models_auth import UserLogin, UserGet, CodeAuth2
from typing import List
from fastapi.responses import RedirectResponse
import smtplib
from backend.security_util.generate_pswd import generate_one_time_psswd


class LoginForm:
    def __init__(self, current_user: UserLogin):
        self.current_user: UserLogin = current_user
        self.errors: List = []

    async def load_data(self):
        self.login = self.current_user.login
        self.password = self.current_user.password
        self.auth2 = None

    async def is_valid(self):
        if not self.password or not len(self.password) >= 4:
            self.errors.append("A valid password is required")
        if not self.errors:
            return True
        return False

router = APIRouter()
@router.get("/")
def login():
    print("Get list authentication")
    return {"Get list": "auth"}


@router.post("/", response_model=UserLogin)
async def login(current_user: UserLogin, db: Session = Depends(get_db)):
    if current_user.identification == true():
        response = RedirectResponse(url=f"/identification", status_code=HTTP_303_SEE_OTHER)
        return response
    print("Post data authentication")
    form = LoginForm(current_user)
    await form.load_data()
    if await form.is_valid():
        try:
            Get_user = UserGet(
                login=form.login,
                password=form.password
            )
            user: User = get_user(Get_user, db=db)
            if user is None:
                print("User does not exist or wrong password")
                response = RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
            else:
                print("Logged in successfully")
                if user.auth2 == true():
                    print("authentication two factor")

                    response = RedirectResponse(url=f"/auth2", status_code=HTTP_303_SEE_OTHER)
                    response.set_cookie(key="email_user", value=user.email, max_age=3600, secure=True, httponly=True)
                else:
                    print("no authentication two factor")
                    response = RedirectResponse(url="/app/LK", status_code=HTTP_303_SEE_OTHER)
                response.set_cookie(key="user_id", value=user.id, secure=True)
            return response
        except HTTPException:
            return {"message": "Invalid credentials"}
auth2_data = {}

@router.get("/auth2")
async def auth2(request: Request):
    print("Get Auth2")
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login('vamp.be.live@gmail.com', '')
        one_time_password = CodeAuth2(
            code=generate_one_time_psswd(6)
        )
        email_user = request.cookies.get("email_user")
        print(email_user)
        smtpObj.sendmail("vamp.be.live@gmail.com", email_user,
                         f'Code password for Must Music: {one_time_password.code}')
        auth2_data[email_user] =one_time_password.code
        print(auth2_data)
    except HTTPException:
        ...
    return {"message": "Get Auth2"}#вот это переделать и все


@router.post("/auth2", response_model = CodeAuth2)
async def auth2(code: CodeAuth2, request: Request):
    print("Post Auth2")
    email_user = request.cookies.get("email_user")
    print(email_user)
    print(auth2_data[email_user])
    print(code.code)
    if code.code == str(auth2_data[email_user]):
        print("Auth2 successful")
        response = RedirectResponse(url="/app/LK", status_code=HTTP_303_SEE_OTHER)
    else:
        print("Auth2 not successful")
        response = RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    return response
    return {"code": "Post Auth2"}