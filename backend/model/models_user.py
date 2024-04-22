from pydantic import BaseModel

class UserSetting(BaseModel):
    delete_user: bool
    exit_user: bool
    up_auth2: bool
    up_login: bool
    up_email: bool
    up_name: bool
    up_surname: bool
    auth2: bool
    login: str
    email: str
    name: str
    surname: str
    close: bool
class UserSettingPassword(BaseModel):
    password_valid: str
    password: str
    close: bool