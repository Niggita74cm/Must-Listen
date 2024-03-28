import databases
from backend.core.config import postgresql_settings
def get_url(user, password, host, port, database):
    url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    return url
url = get_url(postgresql_settings["pg_user"],
                        postgresql_settings["pg_password"],
                        postgresql_settings["pg_host"],
                        postgresql_settings["pg_port"],
                        postgresql_settings["pg_database"])
async def check_db_connected():
    try:
        if not str(url).__contains__("postgresql"):
            database = databases.Database(url)
            if not database.is_connected:
                await database.connect()
                await database.execute("SELECT 1")
        print("Database is connected", "\N{smiling face with smiling eyes}")
    except Exception as e:
        print(
            "Looks like db is missing or is there is some problem in connection,see below traceback"
        )
        raise e
async def check_db_disconnected():
    try:
        if not str(url).__contains__("postgresql"):
            database = databases.Database(url)
            if database.is_connected:
                await database.disconnect()
        print("Database is Disconnected","\N{sleeping face}")
    except Exception as e:
        raise e