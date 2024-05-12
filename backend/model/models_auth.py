from pydantic import BaseModel

#используется в создании пользователя, то есть при идентификации(для фронта не важно)
class UserCreate(BaseModel):
    login: str
    email: str
    password: str
#используется для  идентификации (получение инфы с фронта)
class UserCreateFormPost(BaseModel):
    login: str
    email: str
    password: str
    confirmPassword: str
#для аутентификации форма используется (получение инфы с фронта)
class UserLogin(BaseModel):
    login: str
    password: str
    identification: bool #так этого нет на фронте, но в теории должно быть так как вроде как перессылка по url на беке происходит
#нужно для аутентификации пользователя (для фронта не важно)
class UserGet(BaseModel):
    login: str
    password: str
#для второй аутентификации (получение инфы с фронта)
class CodeAuth2(BaseModel):
    code: str
