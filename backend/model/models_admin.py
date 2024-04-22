from pydantic import BaseModel

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

class DataForDeleteUser(BaseModel):
    user_id: int
    login: str
    email: str
    login_ind: bool
    email_ind: bool
    close: bool


#переделать
class DataForDeleteComment(BaseModel):
    user_id: int
    track_id: bool
    text: str
    text_ind: bool
    login: str
    login_ind: bool
    close: bool