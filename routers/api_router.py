from fastapi import APIRouter
from constants import API_VERSION
# Create API router
api_router = APIRouter(
    prefix=f"/api/{API_VERSION}",
    tags=["api"],
    responses={404: {"description": "API Operation not found"}},
)