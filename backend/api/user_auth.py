from starlette.status import HTTP_303_SEE_OTHER
from backend.database.models import User
from backend.database.work_user_db import get_user, get_user_id
from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import true
from backend.model.models_auth import UserLogin,  CodeAuth2, UserLoginResponse, CodeAuth2Response
import smtplib
from backend.services.security_util.generate_pswd import generate_one_time_psswd
from starlette.responses import Response
from email.mime.text import MIMEText


router = APIRouter()
@router.post("/api/", response_model=UserLoginResponse)
async def login(current_user: UserLogin, db: Session = Depends(get_db), response: Response = None):
    print("Post data authentication")
    try:
        result = UserLoginResponse(
            second_factor=False,
            access_user=False
        )
        Get_user = UserLogin(
            login=current_user.login,
            password=current_user.password
        )
        user: User = get_user(Get_user, db=db)
        if user is None:
            print("User does not exist or wrong password")
        else:
            print("Logged in successfully")
            result.access_user = True
            if user.auth2 == true():
                print("authentication two factor")
                result.second_factor = True
            else:
                response.set_cookie(key="user_id", value=str(user.id), httponly=True, samesite="lax")
                print("no authentication two factor")
        print(result)
        return result
    except HTTPException:
        return {"message": "Invalid credentials"}


@router.get("/api/2factor")
async def auth2(request: Request, db: Session = Depends(get_db), response: Response = None):
    print("Get Auth2")
    try:

        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login('vamp.be.live@gmail.com', 'pami ieuq ywqu vxgj')
        one_time_password = CodeAuth2(
            code=generate_one_time_psswd(6)
        )
        user_id = int(request.cookies.get("user_id"))
        print(f'user_id: {user_id}')
        user = get_user_id(user_id, db)
        email_user = user.email
        print(f'email_user: {email_user}')

        body_msg = f'Code password for Must Music: {one_time_password.code}'
        print(body_msg)
        msg = MIMEText(body_msg)
        msg['Subject'] = "Must Music"
        msg['From'] = 'vamp.be.live@gmail.com'
        msg['To'] = email_user
        smtpObj.send_message(msg=msg)
        response.set_cookie(key="code", value=one_time_password.code,  secure=True, httponly=True, samesite="lax")
        print(f'one_time_password.code: {one_time_password.code}')
    except HTTPException:
        return "Invalid credentials"
    return "One-time password sent successfully"


@router.post("/api/2factor", response_model=CodeAuth2Response)
async def auth2(code: CodeAuth2, request: Request, db: Session = Depends(get_db), response: Response = None):
    print("Post Auth2")
    user_id = int(request.cookies.get("user_id"))
    code_get = request.cookies.get("code")
    user = get_user_id(user_id, db)
    email_user = user.email
    print(f'email_user: {email_user}')
    print(f'code_get: {code_get}')
    print(code.code)
    access = False
    if code.code == str(code_get):
        print("Auth2 successful")
        access = True
        response.set_cookie(key="user_id", value=str(user_id), secure=True)
    accessAuth2 = CodeAuth2Response(
        isLoginSuccessful=access
    )
    return accessAuth2