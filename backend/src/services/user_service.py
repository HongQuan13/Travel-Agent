import logging
from sqlalchemy.orm import Session
from fastapi import HTTPException

from backend.src.models.user_model import User
from backend.src.interfaces.user_interface import (
    CreateUserResponse,
    CreateUserRequest,
)

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self):
        logger.info("UserService initialized")

    async def create_user(self, user: CreateUserRequest, db: Session):
        exist_user = db.query(User).filter_by(email=user.email).first()

        if exist_user:
            raise HTTPException(status_code=400, detail="User account exist")

        new_user = User(username=user.username, email=user.email)
        db.add(new_user)
        db.commit()
        logger.info(f"Create new user {new_user.id} successfully")

        return CreateUserResponse(
            id=new_user.id, email=new_user.email, username=new_user.username
        )
