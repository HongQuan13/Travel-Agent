import logging
from sqlalchemy.orm import Session

from models.user_model import User
from interfaces.user_interface import CreateUserResponse, CreateUserRequest

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self):
        logger.info("UserService initialized")

    async def create_user(self, user: CreateUserRequest, db: Session):
        existUser = db.query(User).filter_by(email=user.email).first()

        if existUser:
            logger.error("User account already exists!")
            return None

        newUser = User(username=user.username, email=user.email)
        db.add(newUser)
        db.commit()
        logger.info(f"Create new user {newUser.id} successfully")

        return CreateUserResponse(
            id=newUser.id, email=newUser.email, username=newUser.username
        )
