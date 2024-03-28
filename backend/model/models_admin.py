from pydantic import BaseModel

#{
#choose_create_user:bool
#choose_delete_user:bool
#choose_delete_comment:bool
#user_id:int//не знаю как это получить
#comment_id: int//не знаю как это получить
#}
class ChooseAction(BaseModel):
    choose_create_user: bool
    choose_delete_user: bool
    choose_delete_comment: bool
    close: bool

class UserCreateAdmin(BaseModel):
    login: str
    email: str
    password: str
    name: str
    surname: str
    confirmPassword: str
    close: bool

class DataForAdmin(BaseModel):
    data_id: int
    close: bool
