from typing import TYPE_CHECKING
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.models.base_model import Base
from backend.src.models.message_model import Message

if TYPE_CHECKING:
    from backend.src.models.user_model import User


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    # relation
    user: Mapped["User"] = relationship(back_populates="conversation")
    message: Mapped["Message"] = relationship(back_populates="conversation")
