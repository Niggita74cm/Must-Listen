class Settings:
    PROJECT_NAME: str = "FastAPI-2FA"
    PROJECT_VERSION: str = "1.0.0"
settings = Settings()

postgresql_settings = {
    "pg_user": "vaa",
    "pg_password": "nasty18",
    "pg_name_service_docker": "postgres_db",
    "pg_port": "5432",
    "pg_database": "bip"
}