from sqlalchemy import Enum, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime

from backend.src.models.conversationModel import Conversation


class Base(DeclarativeBase):
    pass


# id	SERIAL (PK)	Unique identifier for each message
# conversation_id	INTEGER (FK)	References Conversations.id
# sender	VARCHAR	Either ‘user’ or ‘bot’ to indicate who sent it
# message_text	TEXT	The actual message content
# timestamp

# app/models/message_model.py


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.id"), nullable=False
    )
    sender: Mapped[str] = mapped_column(Enum("user", "bot"), nullable=False)
    message_text: Mapped[str] = mapped_column(Text, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)

    conversation: Mapped["Conversation"] = relationship(
        "Conversation", back_populates="messages"
    )