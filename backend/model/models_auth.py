from pydantic import BaseModel

#используется в создании пользователя, то есть при идентификации
class UserCreate(BaseModel):
    login: str
    email: str
    password: str
class UserCreateFormPost(BaseModel):
    username: str
    email: str
    password: str
    confirmPassword: str

#для аутентификации
class UserLogin(BaseModel):
    login: str
    password: str
class UserLoginResponse(BaseModel):
    second_factor: bool
    access_user: bool

#для второй аутентификации
class CodeAuth2(BaseModel):
    code: str
class CodeAuth2Response(BaseModel):
    isLoginSuccessful: bool

