from fastapi import APIRouter, Depends
from users.schemas import CreateUser, UserOut, SortingOptions, SortingDirections, UpdateUsername
from users.services import create_user, get_users, update_user, delete_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", status_code=201)
async def create_new_user(new_user: CreateUser):
    return create_user(new_user)


@router.get("/", status_code=200)
async def get_users_list(sort_by: SortingOptions, sorting_direction: SortingDirections, skip: int = 0, limit: int = 10):
    return get_users(skip, limit, sort_by, sorting_direction)


@router.put("/{user_id}", status_code=201)
async def update_single_user(user_id: int, user: CreateUser):
    return update_user(user_id, user)


@router.delete("/{user_id}", status_code=204)
async def delete_single_user(user_id: int):
    return delete_user(user_id)
