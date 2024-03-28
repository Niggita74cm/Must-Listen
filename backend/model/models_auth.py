from pydantic import BaseModel

class UserCreate(BaseModel):
    login: str
    email: str
    password: str
class UserDataCreate(BaseModel):
    name: str
    surname: str
class UserCreateFormPost(BaseModel):
    login: str
    email: str
    password: str
    confirmPassword: str
    name: str
    surname: str
class UserLogin(BaseModel):
    login: str
    password: str
    auth: bool
    identification: bool

class UserGet(BaseModel):
    login: str
    password: str

class CodeAuth2(BaseModel):
    code: str
