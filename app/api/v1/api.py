from fastapi import APIRouter

from app.api.v1.endpoints import auth, recipe

api_router = APIRouter()
api_router.include_router(recipe.router, prefix="/recipes", tags=["recipes"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
