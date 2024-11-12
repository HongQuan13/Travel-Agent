# id	SERIAL (PK)	Unique identifier for the conversation
# user_id	INTEGER (FK)	References Users.id
# trip_id	INTEGER (FK)	References Trips.id (optional, links the conversation to a specific trip)
# status	VARCHAR	Status of the conversation (e.g., active, completed)
# started_at	TIMESTAMP	Timestamp for when the conversation started
# ended_at	TIMESTAMP	Timestamp for when the conversation ended (nullable)

from sqlalchemy import Integer, ForeignKey, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

from backend.src.models.userModel import User
from backend.src.models.messageModel import Message


class Base(DeclarativeBase):
    pass


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="conversations")
    messages: Mapped[list["Message"]] = relationship(
        "Message", back_populates="conversation"
    )
