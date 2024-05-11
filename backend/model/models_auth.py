from pydantic import BaseModel

#используется в создании пользователя, то есть при идентификации
class UserCreate(BaseModel):
    login: str
    email: str
    password: str
#используется для получения инфы с фронта при идентификации
class UserCreateFormPost(BaseModel):
    login: str
    email: str
    password: str
    confirmPassword: str
#для аутентификации форма используется
class UserLogin(BaseModel):
    login: str
    password: str
    identification: bool #так этого нет на фронте, но в теории должно быть так как вроде как перессылка по url на беке происходит
#
class UserGet(BaseModel):
    login: str
    password: str

class CodeAuth2(BaseModel):
    code: str
