from sqlalchemy.orm import Session
from backend.database.work_user_db import get_user_id

def check_on_admin(db: Session, user_id: int):
    user_data = get_user_id(user_id,db)
    if user_data.username == 'admin':
        return True
    return False