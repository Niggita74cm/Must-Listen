import re
from backend.model.models_auth import UserCreateFormPost
from typing import List
from backend.database.work_user_db import get_all_users
from sqlalchemy.orm import Session
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
class UserCreateForm:
    def __init__(self, current_user: UserCreateFormPost):
        self.current_user: UserCreateFormPost = current_user
        self.errors: List = []
    async def load_data(self):
        self.login = self.current_user.login
        self.email = self.current_user.email
        self.password = self.current_user.password
        self.confirmPassword = self.current_user.confirmPassword

    async def is_valid(self, db: Session):
        if not re.fullmatch(regex, self.email):
            self.errors.append("Please enter valid email")
        if not self.password or not len(self.password) >= 8:
            self.errors.append("Password must be >= 8 chars")
        if not self.password or not len(self.login) >= 0:
            self.errors.append("login must be")
        if self.password != self.confirmPassword:
            self.errors.append("Confirm Password does not match")
        if len(get_all_users(db, self.login)) != 0:
            print(len(get_all_users(db, self.login)))
            self.errors.append("This login already exists")
        if not self.errors:
            return True
        print(self.errors)
        return False
