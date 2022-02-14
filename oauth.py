from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends, status
from passlib.context import CryptContext
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import datetime, timedelta
from jose import jwt, JWTError
from models import TokenData, UserModel

from bd import User


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
token = OAuth2PasswordBearer(tokenUrl='token')


class OAuth:
    @classmethod
    async def get_current_user(cls, token: str = Depends(token)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception
        user = await cls.get_user(username=token_data.username)
        if user is None:
            raise credentials_exception
        return user

    @classmethod
    def verify_password(cls, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password):
        return pwd_context.hash(password)

    @classmethod
    def get_password_hash(cls, password):
        return pwd_context.hash(password)

    @classmethod
    def decode_token(cls):
        return {}

    @classmethod
    def create_access_token(cls, data: dict):
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @classmethod
    async def get_user(cls, username: str):
        user = await User.objects.get_or_none(username=username)
        if user:
            return UserModel(**user.dict())
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect username or password",)

    @classmethod
    async def authenticate_user(cls, username: str, password: str):
        user = await cls.get_user(username)
        if not user:
            return False
        if not cls.verify_password(password, user.hashed_password):
            return False
        return user