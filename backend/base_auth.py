from fastapi import APIRouter
from backend.api.user_auth import router as route_login
from backend.api.user_identific import router as route_signup
from backend.api.user_LK import router as route_user
from backend.api.admin import router as route_admin
from backend.api.SearchPage import router as route_search
from backend.api.TrackPage import router as route_track
api_router = APIRouter()
api_router.include_router(route_signup, prefix="", tags=["users-webapp"])
api_router.include_router(route_login, prefix="", tags=["auth-webapp"])
api_router.include_router(route_admin, prefix="", tags=["admin_list-webapp"])
api_router.include_router(route_user, prefix="", tags=["action-webapp"])
api_router.include_router(route_track, prefix="", tags=["track-page-webapp"])