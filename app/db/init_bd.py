from models.models import User, Item, Role
from constants.role import Roles


async def init_db() -> None:

    # Create Super Admin Account
    # account = crud.account.get_by_name(
    #     db, name=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME
    # )
    # if not account:
    #     account_in = schemas.AccountCreate(
    #         name=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME,
    #         description="superadmin account",
    #     )
    #     crud.account.create(db, obj_in=account_in)

    # Create 1st Superuser
    # user = crud.user.get_by_email(db, email=settings.FIRST_SUPER_ADMIN_EMAIL)
    # if not user:
    #     account = crud.account.get_by_name(
    #         db, name=settings.FIRST_SUPER_ADMIN_ACCOUNT_NAME
    #     )
    #     user_in = schemas.UserCreate(
    #         email=settings.FIRST_SUPER_ADMIN_EMAIL,
    #         password=settings.FIRST_SUPER_ADMIN_PASSWORD,
    #         full_name=settings.FIRST_SUPER_ADMIN_EMAIL,
    #         account_id=account.id,
    #     )
    #     user = crud.user.create(db, obj_in=user_in)

    # Create Role If They Don't Exist

    # roles = await Role.objects.bulk_create_or_update(
    #     [
    #         Role(name=Roles.GUEST['name'], descriptions=Roles.GUEST["description"]),
    #         Role(name=Roles.ACCOUNT_ADMIN['name'], descriptions=Roles.ACCOUNT_ADMIN["description"]),
    #         Role(name=Roles.ACCOUNT_MANAGER['name'], descriptions=Roles.ACCOUNT_MANAGER["description"]),
    #         Role(name=Roles.SUPER_ADMIN['name'], descriptions=Roles.SUPER_ADMIN["description"]),
    #         Role(name=Roles.ADMIN['name'], descriptions=Roles.ADMIN["description"])
    #     ]
    # )
    await Role.objects.get_or_create(name=Roles.GUEST['name'], descriptions=Roles.GUEST["description"])
    await Role.objects.get_or_create(name=Roles.ACCOUNT_ADMIN['name'], descriptions=Roles.ACCOUNT_ADMIN["description"])
    await Role.objects.get_or_create(name=Roles.ACCOUNT_MANAGER['name'], descriptions=Roles.ACCOUNT_MANAGER["description"])
    await Role.objects.get_or_create(name=Roles.SUPER_ADMIN['name'], descriptions=Roles.SUPER_ADMIN["description"])
    await Role.objects.get_or_create(name=Roles.ADMIN['name'], descriptions=Roles.ADMIN["description"])

    # Assign super_admin role to user
    # user_role = crud.user_role.get_by_user_id(db, user_id=user.id)
    # if not user_role:
    #     role = crud.role.get_by_name(db, name=Role.SUPER_ADMIN["name"])
    #     user_role_in = schemas.UserRoleCreate(user_id=user.id, role_id=role.id)
    #     crud.user_role.create(db, obj_in=user_role_in)