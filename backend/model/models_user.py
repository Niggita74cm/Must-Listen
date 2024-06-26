from pydantic import BaseModel

class UserSetting(BaseModel):
    delete_user: bool
    exit_user: bool
    up_auth2: bool
    up_login: bool
    up_email: bool
    auth2: bool
    login: str
    email: str
    #close: bool # непонятно нужно ли
    delete_user: bool
class UserSettingPassword(BaseModel):
    password_valid: str
    password: str
    close: bool