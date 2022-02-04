import fastapi
from fastapi import APIRouter, Depends, HTTPException, status, Request, Header, status, HTTPException
# from reposytory import UserRep, get_user_rep
from models import UserModel, ItemModel, ItemOut
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


@router.get("/{email}", response_model=User, response_model_exclude=['is_active', 'hashed_password'])
async def create_user(email: str):
    a = await User.objects.select_related("items").get_or_none(email=email)
    if not a:
        raise HTTPException(status_code=404, detail='Not found')
    return a


@router.post('/items', response_model=Item, response_model_include=['id', 'user__id'])
async def create_item(item: ItemModel):
    user = await User.objects.get()
    item = await Item.objects.update_or_create(**item.dict(), user=user)

    return item