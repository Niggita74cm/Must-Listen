from backend.core.config import settings
from backend.database.base import Base
from backend.database.connect import engine
from backend.database.utils import check_db_connected
from backend.database.utils import check_db_disconnected
from fastapi import FastAPI
from backend.base_auth import api_router as web_app_router
from fastapi.middleware.cors import CORSMiddleware


def include_router(app):
    app.include_router(web_app_router)
def create_tables():
    Base.metadata.create_all(bind=engine)
def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app



app = start_application()
origins = ["http://localhost:8080/"]

app.add_middleware(
   CORSMiddleware,
    allow_origins=["*"],
   allow_credentials=True,
   allow_methods=["*"],
  allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await check_db_connected()


@app.on_event("shutdown")
async def shutdown_event():
    await check_db_disconnected()



# if __name__ == "__main__":
#     uvicorn.run(app, port=8000, host="0.0.0.0")
