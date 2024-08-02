from sqlalchemy.orm import Session

from backend.services.checking_input_data import Verification
from backend.model.models_user import SettingsPostResponse
from backend.database.work_user_db import get_user_id, delete_user
from backend.database.work_user_db import (update_user_auth, update_user_login,
                                           update_user_email, update_user_password
                                           )
from backend.database.work_db_user_track import delete_tracks_users
from backend.database.work_db_comment import delete_all_comments_user
class RealizationSettings:
    def __init__(self, db: Session, user_id: int):
        self.db = db
        self.user_id = user_id
        self.OldData = get_user_id(user_id=user_id, db=db)
        self.result = SettingsPostResponse(ResultCommand=False, Message='')
    def UpdateUsername(self, NewUsername):
        CheckNewUsername = Verification(db=self.db)
        CheckNewUsername.CheckUpdateLogin(NewLogin=NewUsername, Oldlogin=self.OldData.login)
        errors = CheckNewUsername.errors
        self.result.Message = errors
        if errors == '':
            update_user_login(user_id=self.user_id, up_data=NewUsername, db=self.db)
            self.result.ResultCommand = True
        return self.result
    def UpdateEmail(self, NewEmail):
        CheckNewEmail = Verification(db=self.db)
        CheckNewEmail.CheckUpdateEmail(NewEmail=NewEmail, OldEmail=self.OldData.email)
        errors = CheckNewEmail.errors
        self.result.Message = errors
        if errors == '':
            update_user_email(user_id=self.user_id, up_data=NewEmail, db=self.db)
            self.result.ResultCommand = True
        return self.result
    def UpdatePassword(self, NewPassword, CurrentPassword):
        CheckNewPassword = Verification(db=self.db)
        print(f"New Password: {NewPassword}")
        print(f"Current Password: {CurrentPassword}")
        CheckNewPassword.CheckUpdatePassword(NewPassword=NewPassword, OldPassword=self.OldData.hashed_password, CurrentPassword=CurrentPassword)
        errors = CheckNewPassword.errors
        self.result.Message = errors
        if errors == '':
            update_user_password(user_id=self.user_id, up_data=NewPassword, db=self.db)
            self.result.ResultCommand = True
        return self.result
    def UpdateSecondFactor(self, NewSecondFactor):
        self.result.Message = ''
        self.result.ResultCommand = True
        if NewSecondFactor == "false":
            update_user_auth(user_id=self.user_id, up_data=False, db=self.db)
        else:
            update_user_auth(user_id=self.user_id, up_data=True, db=self.db)
        return self.result
    def DeleteYourself(self):
        self.result.Message = ''
        self.result.ResultCommand = True
        delete_user(user_id=self.user_id, db=self.db)
        delete_tracks_users(db=self.db, user_id=self.user_id)
        delete_all_comments_user(db=self.db, user_id=self.user_id)
        return self.result
    def LogOutAccount(self, request):
        self.result.Message = ''
        self.result.ResultCommand = True
        request.cookies.clear()
        return self.result