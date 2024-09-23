from fastapi import APIRouter
from backend.api.user_auth import router as route_login
from backend.api.user_identific import router as route_signup
from backend.api.user_LK import router as route_LK_User
from backend.api.user_setting import router as route_setting
from backend.api.SearchPage import router as route_search
from backend.api.TrackPage import router as route_track
from backend.api.fake_auth import router as route_fake_auth

api_router = APIRouter()
api_router.include_router(route_signup, prefix="", tags=["register-webapp"])
api_router.include_router(route_login, prefix="", tags=["auth-webapp"])
api_router.include_router(route_LK_User, prefix="", tags=["action-webapp"])
api_router.include_router(route_setting, prefix="", tags=["setting-users-webapp"])
api_router.include_router(route_search, prefix="", tags=["search-track-webapp"])
api_router.include_router(route_track, prefix="", tags=["track-page-webapp"])
api_router.include_router(route_fake_auth, prefix="", tags=["track-page-fake"])