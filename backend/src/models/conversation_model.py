from sqlalchemy import Integer, ForeignKey, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import Base
from models.user_model import User
from models.message_model import Message


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    # user: Mapped["User"] = relationship("User", back_populates="conversations")
    # messages: Mapped[list["Message"]] = relationship(
    #     "Message", back_populates="conversation"
    # )
