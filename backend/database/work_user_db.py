from sqlalchemy import false
from backend.security_util.hashing import Hasher
from backend.database.models import User, User_data
from backend.model.models_auth import UserCreate, UserDataCreate, UserGet
from sqlalchemy.orm import Session



def get_user(user: UserGet, db: Session):
    #print(user.login, user.password)
    #print(Hasher.get_password_hash(user.password))
    user_ = db.query(User).filter(User.login == user.login).all()
    result = None
    for us in user_:
        if Hasher.verify_password(user.password, us.hashed_password):
            result = us
    #print(result)
    return result
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

def update_user(user: User, db: Session):
    ...
def update_user_data(user: User, db: Session):
    ...
def delete_user(user_id: int, db: Session):
    #также доделать удаление списка треков
    user = db.query(User).filter(User.id == user_id).all()
    user_data = db.query(User).filter(User_data.user_id == user_id).all()
    db.delete(user_data)
    db.delete(user)
    db.commit()
    db.refresh(user)
    db.refresh(user_data)

def get_user_data(id: int, db:Session):
    ...