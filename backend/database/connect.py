from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.core.config import postgresql_settings

def check_have_tables(name: str, table: list):
    for i in table:
        if i.name == name:
            return True
    return False

def get_engine(user, password, name_service_docker, port, database):
    url = f"postgresql://{user}:{password}@{name_service_docker}:{port}/{database}"
    engine = create_engine(url)
    #metadata = MetaData()
    #metadata.reflect(bind=engine, schema="public")
    #Name Table:
    #User
    #User_data
    #User_track
    #Track
    #User_rating
    #User_comment
    #Track_comment
    #Track_rating
    #if len(metadata.sorted_tables) == 0 or check_have_tables(name='user', table=metadata.sorted_tables):
    #    user = Table(
    #        "user",
    #        metadata,
    #        Column("id", Integer, primary_key=True, index=True),
    #        Column("login", String, nullable=False),
    #        Column("email", String, nullable=False),
    #        Column("hashed_password", String, nullable=False),
    #    )
    #if len(metadata.sorted_tables) == 0 or check_have_tables(name='user_data', table=metadata.sorted_tables):
    #    user = Table(
    #        "user",
    #        metadata,
    #        Column("id", Integer, primary_key=True, index=True),
    #        Column("login", String, nullable=False),
    #        Column("email", String, nullable=False),
    #        Column("hashed_password", String, nullable=False),
    #    )
    #metadata.create_all(bind=engine)
    return engine

engine = get_engine(postgresql_settings["pg_user"],
                        postgresql_settings["pg_password"],
                        postgresql_settings["pg_name_service_docker"],
                        postgresql_settings["pg_port"],
                        postgresql_settings["pg_database"])
def get_session():

    session = sessionmaker(bind=engine)()
    return session

def get_db():
    db = get_session()
    try:
        yield db
    finally:
        db.close()