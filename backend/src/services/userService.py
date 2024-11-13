import logging
from sqlalchemy.orm import Session

from models.userModel import User
from interfaces.userInterface import CreateUserResponse, UserRequest

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self):
        logger.info("UserService initialized")

    async def create_user(self, user: UserRequest, db: Session):
        existUser = await db.query(User).filter_by(email=user.email).first()

        if existUser:
            logger.error("User account already exists!")
            return None

        newUser = User(user.username, user.email)
        await db.add(newUser)
        await db.commit()
        logger.info(f"Create new user {newUser.id} successfully")
        return CreateUserResponse(
            id=newUser.id, email=newUser.email, username=newUser.username
        )
