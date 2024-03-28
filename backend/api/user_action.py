from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/app/LK")
def main_LK(db: Session = Depends(get_db)):
    ...


#для кнопок
@router.post("/app/LK")
def main_LK(db: Session = Depends(get_db)):
    ...
#для поиска
@router.post("/app/LK")
def main_LK(db: Session = Depends(get_db)):
    ...