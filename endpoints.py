import fastapi
from asyncpg import UniqueViolationError
from fastapi import APIRouter, Depends, HTTPException, status, Request, Header, status, HTTPException
# from reposytory import UserRep, get_user_rep
from models import UserModel, ItemModel, ItemOut, UserCreate
from bd import User, Item
from fastapi.security import OAuth2PasswordRequestForm
from oauth import token
from oauth import OAuth

router = APIRouter()

# @router.post("/{user_id}")
# async def create_user(user_id: int, users_rep: UserRep = Depends(get_user_rep)):
#     s = await users_rep.get_user(user_id)
#     return {"user_id": user_id}


@router.post("/create_user")
async def create_user(request: Request, user: UserCreate):
    hased_pass = OAuth.get_password_hash(user.password)
    data = user.dict()
    data['hashed_password'] = hased_pass
    data.pop('password')
    # print(OAuth.verify_password(user.password, hased_pass))
    try:
        s = await User.objects.get_or_create(**data)
        return s
    except Exception as e:
        return {'detail': e.detail}


@router.get("/{username}", response_model=User, response_model_exclude=['is_active', 'hashed_password', 'items__user'])
async def create_user(username: str, user: User = Depends(OAuth.get_current_user)):
    print(user.username)
    a = await User.objects.select_related("items").get_or_none(username=username)
    if not a:
        raise HTTPException(status_code=404, detail='Not found')
    return a


@router.post('/items', response_model=Item, response_model_include=['id', 'user__id'])
async def create_item(item: ItemModel):
    user = await User.objects.get()
    item = await Item.objects.update_or_create(**item.dict(), user=user)

    return item


@router.put('/item_put')
async def put_item(item: Item):
    new_data = item.dict(exclude_unset=True)
    print(new_data)


@router.post('/token')
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await OAuth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = OAuth.create_access_token(data={'sub': user.username})
    return {"access_token": access_token, "token_type": "bearer"}
