from backend.model.models_auth import UserCreate, UserDataCreate, UserCreateFormPost
from typing import List
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
class UserCreateForm:
    def __init__(self, current_user: UserCreateFormPost):
        self.current_user: UserCreateFormPost = current_user
        self.errors: List = []
    async def load_data(self):
        self.login = self.current_user.login
        self.email = self.current_user.email
        self.password = self.current_user.password
        self.name = self.current_user.name
        self.surname = self.current_user.surname
        self.confirmPassword = self.current_user.confirmPassword

    async def is_valid(self):
        #if not re.fullmatch(regex, self.email):
        #    self.errors.append("Please enter valid email")
        if not self.password or not len(self.password) >= 4:
            self.errors.append("Password must be > 4 chars")
        if not self.password or not len(self.login) >= 0:
            self.errors.append("login must be")
        if self.password != self.confirmPassword:
            self.errors.append("Confirm Password does not match")
        if not self.errors:
            return True
        return False

def filling_user(form:UserCreateForm):
    user = UserCreate(
        login=form.login,
        email=form.email,
        password=form.password
    )
    user_data = UserDataCreate(
        name=form.name,
        surname=form.surname
    )
    return user, user_data