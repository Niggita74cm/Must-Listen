from backend.database.connect import get_db
from fastapi import APIRouter
from fastapi import Depends, Request
from sqlalchemy.orm import Session
from backend.model.models_action import ActionMain, ActionComment
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER

router = APIRouter()

