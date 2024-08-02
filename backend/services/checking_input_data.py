import re
from backend.database.work_user_db import get_all_users
from sqlalchemy.orm import Session
from backend.services.security_util.hashing import Hasher

class Verification:
    def __init__(self, db: Session):
        self.errors = ''
        self.db: Session = db
    def CheckNewLogin(self, NewLogin):
        if not len(NewLogin) > 0:
            self.errors += "[Логин не должен быть пустым] "
        if len(get_all_users(self.db, NewLogin)) != 0:
            self.errors += "[Этот логин уже существует] "
    def CheckNewPassword(self, NewPassword, ConfirmPassword):
        if not NewPassword or not len(NewPassword) >= 8:
            self.errors += "[Пароль должен содержать не менее 8 символов] "
        if NewPassword != ConfirmPassword:
            self.errors += "[Повторный ввод пароля неверен] "
    def CheckUpdateLogin(self, NewLogin, Oldlogin):
        self.CheckNewLogin(NewLogin)
        if NewLogin == Oldlogin:
            self.errors += "[Данный логин вы уже используете] "
        if (NewLogin == "anvi_admin" or NewLogin == "sasha_admin"
                or NewLogin == "nikita_admin" or NewLogin == "masha_admin"):
            self.errors += "[Данный логин недопустим] "
        if not self.errors:
            return True
        print(self.errors)
        return False
    def CheckNewEmail(self, NewEmail):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, NewEmail):
            self.errors += "[Пожалуйста, введите действительный адрес электронной почты] "
    def CheckUpdatePassword(self, NewPassword, OldPassword, CurrentPassword):
        self.CheckNewPassword(NewPassword, NewPassword)
        print(f'Old Password: {OldPassword}')
        if NewPassword == OldPassword:
            self.errors += "[Данный пароль вы уже используете] "
        if not Hasher.verify_password(CurrentPassword, OldPassword):
            self.errors += "[Введен неверный пароль] "
        if not self.errors:
            return True
        print(self.errors)
        return False
    def CheckUpdateEmail(self, NewEmail, OldEmail):
        self.CheckNewEmail(NewEmail)
        if NewEmail == OldEmail:
            self.errors += "[Данную электронную почту вы уже используете] "
        if not self.errors:
            return True
        print(self.errors)
        return False
    def CheckAllNewData(self, NewLogin, NewPassword, NewEmail, ConfirmPassword):
        self.CheckNewLogin(NewLogin)
        self.CheckNewPassword(NewPassword, ConfirmPassword)
        self.CheckNewEmail(NewEmail)
        if not self.errors:
            return True
        print(self.errors)
        return False