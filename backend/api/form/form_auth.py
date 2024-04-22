from typing import List
from backend.model.models_auth import UserLogin

class LoginForm:
    def __init__(self, current_user: UserLogin):
        self.current_user: UserLogin = current_user
        self.errors: List = []

    async def load_data(self):
        self.login = self.current_user.login
        self.password = self.current_user.password
        self.auth2 = None

    async def is_valid(self):
        if not self.password or not len(self.password) >= 4:
            self.errors.append("A valid password is required")
        if not self.errors:
            return True
        return False
