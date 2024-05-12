from sqlalchemy import false, update
from backend.services.security_util.hashing import Hasher
from backend.database.models import User
from backend.model.models_auth import UserCreate, UserGet
from sqlalchemy.orm import Session

#получение пользователей по логину
def get_all_users(db: Session, login: str):
    user = db.query(User).filter(User.login == login).all()
    return user
#получение данных о пользователе по паролю и логину
def get_user(user: UserGet, db: Session):
    user_ = get_all_users(db, user.login)
    result = None
    for us in user_:
        if Hasher.verify_password(user.password, us.hashed_password):
            result = us
    return result
#получение данных о пользователе по id
def get_user_id(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    return user
#создание нового пользователя при идентификации
def create_new_user(user_Create: UserCreate, db: Session):
    user = User(
        login=user_Create.login,
        email=user_Create.email,
        hashed_password=Hasher.get_password_hash(user_Create.password),
        auth2 = false()
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user



#
def update_user_login(user_id: int, up_data: str, db: Session):
    user = db.query(User).filter(User.id == user_id).all()
    db.execute(update(User).where(User.id == user_id).values(login = up_data))
    db.commit()
    db.refresh(user)
#
def update_user_password(user_id: int, up_data: str, db: Session):
    db.execute(update(User).where(User.id == user_id).values(hashed_password=Hasher.get_password_hash(up_data)))
    db.commit()
    user = db.query(User).filter(User.id == user_id).all()
    db.refresh(user)
#
def update_user_email(user_id: int, up_data: str, db: Session):
    db.execute(update(User).where(User.id == user_id).values(email=up_data))
    db.commit()
    user = db.query(User).filter(User.id == user_id).all()
    db.refresh(user)
#
def update_user_auth(user_id: int, up_data: bool, db: Session):
    db.execute(update(User).where(User.id == user_id).values(auth2=up_data))
    db.commit()
    user = db.query(User).filter(User.id == user_id).all()
    db.refresh(user)
#
def delete_user(user_id: int, db: Session):
    #также доделать удаление списка треков
    user = get_user_id(db, user_id)
    db.delete(user)
    db.commit()
#
def get_all_user(db:Session):
    users = db.query(User).all()
    return users