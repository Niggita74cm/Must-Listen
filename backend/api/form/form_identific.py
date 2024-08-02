import re
from backend.model.models_auth import UserCreateFormPost
from backend.database.work_user_db import get_all_users
from sqlalchemy.orm import Session
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
class UserCreateForm:
    def __init__(self, current_user: UserCreateFormPost):
        self.current_user: UserCreateFormPost = current_user
        self.errors = ''
    async def load_data(self):
        self.login = self.current_user.username
        self.email = self.current_user.email
        self.password = self.current_user.password
        self.confirmPassword = self.current_user.confirmPassword

    async def is_valid(self, db: Session):
        if not re.fullmatch(regex, self.email):
            self.errors += "[Please enter valid email] "
        if not self.password or not len(self.password) >= 8:
            self.errors += "[Password must be >= 8 chars] "
        if not self.password or not len(self.login) >= 0:
            self.errors += "[login must be] "
        if self.password != self.confirmPassword:
            self.errors += "[Confirm Password does not match] "
        if len(get_all_users(db, self.login)) != 0:
            print(len(get_all_users(db, self.login)))
            self.errors += "[This login already exists]"
        if not self.errors:
            return True
        print(self.errors)
        return False
