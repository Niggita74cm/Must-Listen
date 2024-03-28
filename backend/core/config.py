class Settings:
    PROJECT_NAME: str = "FastAPI-2FA"
    PROJECT_VERSION: str = "1.0.0"
settings = Settings()

postgresql_settings = {
    "pg_user": "VAA",
    "pg_password": "password",
    "pg_host": "localhost",
    "pg_port": "5432",
    "pg_database": "bip"
}