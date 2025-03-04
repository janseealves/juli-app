from fastapi import APIRouter
from http import HTTPStatus

from app.schemas import UserPublic, UsersResponse

router = APIRouter()

users = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "password": "secret"
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "email": "janedoe@example.com",
        "password": "secret"
    }
]

@router.get("/users",tags=["user"], status_code=HTTPStatus.OK, response_model=UsersResponse)
def get_user():
    return {"users": users}
