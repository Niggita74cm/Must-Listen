from pydantic import BaseModel

#используется в создании пользователя, то есть при идентификации(для фронта не важно)
class UserCreate(BaseModel):
    login: str
    email: str
    password: str
#используется для  идентификации (получение инфы с фронта)
class UserCreateFormPost(BaseModel):
    username: str
    email: str
    password: str
    confirmPassword: str
#для аутентификации форма используется (получение инфы с фронта)
class UserLogin(BaseModel):
    login: str
    password: str
class UserLoginResponse(BaseModel):
    second_factor: bool
    access_user: bool







#нужно для аутентификации пользователя (для фронта не важно)
class UserGet(BaseModel):
    login: str
    password: str
#для второй аутентификации (получение инфы с фронта)
class CodeAuth2(BaseModel):
    code: str
