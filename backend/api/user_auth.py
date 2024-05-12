from starlette.status import HTTP_303_SEE_OTHER

from backend.database.models import User
from backend.database.work_user_db import get_user, get_user_id
from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import true
from backend.model.models_auth import UserLogin, UserGet, CodeAuth2
from backend.api.form.form_auth import LoginForm
from fastapi.responses import RedirectResponse
import smtplib
from backend.services.security_util.generate_pswd import generate_one_time_psswd
from starlette.responses import Response



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
                else:
                    print("no authentication two factor")
                    response = RedirectResponse(url="/app/LK", status_code=HTTP_303_SEE_OTHER)
                response.set_cookie(key="user_id", value=user.id, secure=True)
            return response
        except HTTPException:
            return {"message": "Invalid credentials"}
#auth2_data = {}
@router.get("/auth2")
async def auth2(request: Request, db: Session = Depends(get_db)):
    print("Get Auth2")
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login('vamp.be.live@gmail.com', 'pami ieuq ywqu vxgj')
        one_time_password = CodeAuth2(
            code=generate_one_time_psswd(6)
        )
        user_id = request.cookies.get("user_id")
        print(f'user_id: {user_id}')
        user = get_user_id(user_id, db)
        print(user.id)
        email_user = user.email
        print(email_user)
        smtpObj.sendmail("vamp.be.live@gmail.com", email_user,
                         f'Code password for Must Music: {one_time_password.code}')
        #заменить на кук в теории сработать должно
        #auth2_data[email_user] =one_time_password.code
        response = Response()
        response.set_cookie(key="code", value=one_time_password.code,  secure=True, httponly=True)
        print(one_time_password.code)
    except HTTPException:
        return {"message": "Invalid credentials"}
    return response #вот это переделать и все


@router.post("/auth2", response_model = CodeAuth2)
async def auth2(code: CodeAuth2, request: Request, db: Session = Depends(get_db)):
    print("Post Auth2")
    user_id = request.cookies.get("user_id")
    code_get = request.cookies.get("code")
    user = get_user_id(user_id, db)
    email_user = user.email
    print(email_user)
    print(code_get)
    print(code.code)
    if code.code == str(code_get):
        print("Auth2 successful")
        response = RedirectResponse(url="/app/LK", status_code=HTTP_303_SEE_OTHER)
        response.set_cookie(key="user_id", value=user_id, secure=True)
    else:
        print("Auth2 not successful")
        response = RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    return response