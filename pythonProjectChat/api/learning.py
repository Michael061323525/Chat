from fastapi import APIRouter
from initialize import app

router = APIRouter(prefix="/api")


@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


app.include_router(router)
