from utils import hash_password, verify_password
from core import settings, get_db
from models import User
from schemas import (
    LoginForm,
)
from datetime import timedelta, datetime
from jose import JWTError, jwt
from .user import user_service
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import Annotated


class AuthService():

    async def authenticate_user(self, email: str, password: str, db: Session):
        user = user_service.get_user_by_email(email, db)
        if not user:
            # print("user")
            return False
        if not verify_password(password, user.password_hash):
            # print("pass")
            return False
        return user

    def create_access_token(self, data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        # print(encoded_jwt)
        decoded = jwt.decode(
            str(encoded_jwt), key=settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        # print(decoded)
        return encoded_jwt

    # def create_refresh_token(self, data: dict):
    #     to_encode = data.copy()
    #     expire = timedelta(
    #         minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES) + datetime.utcnow()
    #     to_encode.update({"exp": expire})
    #     encoded_jwt = jwt.encode(
    #         to_encode, settings.REFRESH_SECRET_KEY, algorithm=settings.ALGORITHM)
    #     self.save_refresh_token(user_id=data["sub"], refresh_token=encoded_jwt)
    #     return encoded_jwt

    # def save_refresh_token(self, user_id: int, refresh_token: str):
    #     engine2 = create_engine(settings.DATABASE_URL)
    #     SessionLocal2 = sessionmaker(autocommit=False, autoflush=False, bind=engine2)
    #     db = SessionLocal2()
    #     new_refresh_token = RefreshToken(
    #         id=str(uuid.uuid4()),
    #         user_id=user_id,
    #         refresh_token=refresh_token)
    #     db.add(new_refresh_token)
    #     db.commit()

    def get_current_user(self, token: str, db: Session):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, settings.SECRET_KEY,
                                 algorithms=[settings.ALGORITHM])
            # print(token)
            user_id: int = payload.get("sub")
            if user_id is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        user = user_service.get_by_id(db, user_id)
        if user is None:
            raise credentials_exception
        return user

    def get_current_active_user(
        current_user: Annotated[User, Depends(get_current_user)]
    ):
        if not current_user.is_active:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user

    async def login_for_access_token(
        self,
        form_data: LoginForm,
        # response: Response,
        db: Session
    ):
        # print(form_data)
        user = await self.authenticate_user(form_data.email, form_data.password, db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.create_access_token(
            {
                "sub": str(user.id),
                "phone": user.phone_number,
            },
            access_token_expires
        )
        # response.set_cookie(key="access_token", value=access_token, httponly=True)

        # refresh_token = self.create_refresh_token(
        #     data={
        #         "sub": str(user.id),
        #         "phone": user_info.phone_number,
        #         "group": "1"
        #     }
        # )
        return {"access_token": access_token,
                "token_type": "bearer"}

    # def logout(
    #     current_user: Annotated[User, Depends(get_current_user)],
    #     refresh_token: str,
    #     db: Session = Depends(get_db)
    # ):
    #     # Delete the refresh token from the database
    #     query = delete(RefreshToken).where(
    #         RefreshToken.refresh_token == refresh_token)
    #     db.execute(query)
    #     db.commit()
    #     return {"message": "Logout successful"}

    # def refresh_access_token(self, refresh_token: RefreshToken, response: Response, db: Session = Depends(get_db)):
    #     refresh_token = refresh_token.refresh_token
    #     credentials_exception = HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Could not validate credentials",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )
    #     # Verify the refresh token
    #     try:
    #         payload = jwt.decode(refresh_token, settings.REFRESH_SECRET_KEY, algorithms=[
    #                              settings.ALGORITHM])
    #         user_id = payload.get('sub')
    #         if user_id is None:
    #             raise credentials_exception
    #         token_expires = datetime.utcfromtimestamp(payload.get('exp'))
    #         if token_expires < datetime.utcnow():
    #             # delete the refresh token from the database
    #             query = delete(RefreshToken).where(
    #                 RefreshToken.refresh_token == refresh_token)
    #             db.execute(query)
    #             db.commit()
    #             raise credentials_exception
    #     except JWTError:
    #         raise credentials_exception

    #     # Create a new access token
    #     access_token_expires = timedelta(
    #         minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    #     access_token = self.create_access_token(
    #         data={"sub": user_id}, expires_delta=access_token_expires
    #     )
    #     response.set_cookie(key="access_token",
    #                         value=access_token, httponly=True)
    #     return {"access_token": access_token, "token_type": "bearer"}


auth_service = AuthService()
