from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from backend.src.models.base_model import Base


class Itinerary(Base):
    __tablename__ = "itineraries"
    id: Mapped[int] = mapped_column(primary_key=True)
    itinerary_detail: Mapped[str] = mapped_column(Text, nullable=False)
