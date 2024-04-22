from sqlalchemy import false, update, true
from backend.security_util.hashing import Hasher
from backend.database.models import User, User_data
from backend.model.models_auth import UserCreate, UserDataCreate, UserGet
from sqlalchemy.orm import Session

def get_user(user: UserGet, db: Session):
    user_ = db.query(User).filter(User.login == user.login).all()
    result = None
    for us in user_:
        if Hasher.verify_password(user.password, us.hashed_password):
            result = us
    return result

def get_user_id(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).all()
    return user
def create_new_user(user_Create: UserCreate, db: Session, user_data: UserDataCreate):
    user = User(
        login=user_Create.login,
        email=user_Create.email,
        hashed_password=Hasher.get_password_hash(user_Create.password),
        auth2 = false()
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    user_get = UserGet(
        login=user_Create.login,
        password = user_Create.password
    )
    id = get_user(user_get, db).id
    user_data_ = User_data(
        user_id = id,
        name = user_data.name,
        surname = user_data.surname
    )
    db.add(user_data_)
    db.commit()
    db.refresh(user_data_)
    return user
def update_user_login(user_id: int, up_data: str, db: Session):
    user = db.query(User).filter(User.id == user_id).all()
    db.execute(update(User).where(User.id == user_id).values(login = up_data))
    db.commit()
    db.refresh(user)
def update_user_password(user_id: int, up_data: str, db: Session):
    db.execute(update(User).where(User.id == user_id).values(hashed_password=Hasher.get_password_hash(up_data)))
    db.commit()
    user = db.query(User).filter(User.id == user_id).all()
    db.refresh(user)
def update_user_email(user_id: int, up_data: str, db: Session):
    db.execute(update(User).where(User.id == user_id).values(email=up_data))
    db.commit()
    user = db.query(User).filter(User.id == user_id).all()
    db.refresh(user)
def update_user_auth(user_id: int, up_data: bool, db: Session):
    db.execute(update(User).where(User.id == user_id).values(auth2=up_data))
    db.commit()
    user = db.query(User).filter(User.id == user_id).all()
    db.refresh(user)

def delete_user(user_id: int, db: Session):
    #также доделать удаление списка треков
    user = get_user_id(db, user_id)
    db.delete(user)
    db.commit()
def delete_user_data(user_id: int, db: Session):
    #также доделать удаление списка треков
    user_data = db.query(User_data).filter(User_data.user_id == user_id).all()
    db.delete(user_data)
    db.commit()
def update_user_data_name(user_id: int, up_data: str, db: Session):
    db.execute(update(User_data).where(User_data.user_id == user_id).values(name=up_data))
    db.commit()
    user = db.query(User_data).filter(User_data.user_id == user_id).all()
    db.refresh(user)
def update_user_data_surname(user_id: int, up_data: str, db: Session):
    db.execute(update(User_data).where(User_data.user_id == user_id).values(surname=up_data))
    db.commit()
    user = db.query(User_data).filter(User_data.user_id == user_id).all()
    db.refresh(user)
def get_user_data(user_id: int, db:Session):
    user_data = db.query(User_data).filter(User_data.user_id == user_id).all()
    return user_data
def get_all_user(db:Session):
    users = db.query(User).all()
    return users