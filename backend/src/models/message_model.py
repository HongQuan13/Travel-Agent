from sqlalchemy import Enum, Integer, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from backend.src.models.base_model import Base


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.id"), nullable=False
    )
    sender: Mapped[str] = mapped_column(Enum("user", "bot"), nullable=False)
    category: Mapped[str] = mapped_column(Enum("text", "plan"), default="text")
    content: Mapped[str] = mapped_column(Text, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
