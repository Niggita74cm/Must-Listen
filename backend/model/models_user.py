from pydantic import BaseModel

class UserInfo(BaseModel):
    username: str
    email: str
    second_factor: bool
    NumberPrivileges: str

class ConfigurationOptions(BaseModel):
    SettingsCommand: str
    NewData: str
    OldData: str

class SettingsPostResponse(BaseModel):
    ResultCommand: bool
    Message: str
