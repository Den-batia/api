from fastapi import APIRouter, Depends, Request, status, HTTPException, Security
from schemas.schemas import ItemModel, UserCreate, UserBase, RoleCreate, UserModel, UserWithoutRole, TokenData, RoleInBd
from models.models import User, Item, Role
from fastapi.security import OAuth2PasswordRequestForm
from depends.oauth import OAuth
from constants.role import Roles

router = APIRouter()

# @router.post("/{user_id}")
# async def create_user(user_id: int, users_rep: UserRep = Depends(get_user_rep)):
#     s = await users_rep.get_user(user_id)
#     return {"user_id": user_id}


@router.post("/create_user", response_model=User)
async def create_user(user: UserCreate):
    hashed_pass = OAuth.get_password_hash(user.password)
    data = user.dict()
    data.update({'hashed_password': hashed_pass})
    data = UserWithoutRole(**data)
    user = await User.objects.get_or_none(username=data.username)
    if user:
        raise HTTPException(
            status_code=409,
            detail="The user with this username already exists in the system.",
        )
    role = await Role.objects.get_or_none(name=Roles.GUEST['name'])
    user = await User.objects.create(**data.dict(), role=role)
    # await user.roles.add(role)
    return user


@router.get("/about_me", response_model=User, response_model_exclude=['is_active', 'hashed_password', 'items__user', 'role__roleuser'])
async def create_user(user: TokenData = Security(OAuth.get_current_user, scopes=['ADMIN'])):
    a = await User.objects.select_related(['role', 'items']).get_or_none(username=user.username)
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
    access_token = OAuth.create_access_token(data={'sub': user.username, 'role': user.role.name})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/roles/create_role')
async def create_role(data: RoleCreate):
    role = await Role.objects.get_or_create(**data.dict())
    return role


@router.get('/roles', response_model=list[RoleInBd])
async def get_roles():
    roles = await Role.objects.select_related('users').all()
    return roles

