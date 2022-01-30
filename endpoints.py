import fastapi
from fastapi import APIRouter, Depends, HTTPException, status, Request
# from reposytory import UserRep, get_user_rep
from models import UserModel
from bd import User, Item

router = APIRouter()


# @router.post("/{user_id}")
# async def create_user(user_id: int, users_rep: UserRep = Depends(get_user_rep)):
#     s = await users_rep.get_user(user_id)
#     return {"user_id": user_id}

@router.post("/", response_model=User)
async def create_user(request: Request, data: dict):

    # print(dict(request.headers))
    a = await User.objects.get_or_create()
    # s = await users_rep.get_user(user_id)
    # return {"user_id": user_id}
    return a


@router.get("/{email}", response_model=User)
async def create_user(email: str, request: Request):
    a = await User.objects.select_related("items").fields({'id': ..., 'email': ...}).get(email=email)
    # s = await users_rep.get_user(user_id)
    # return {"user_id": user_id}
    return a