from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base



class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    category: Mapped[str] = mapped_column(String(50), nullable=False)

    task: Mapped[str] = mapped_column(String(255), nullable=False)

    time_slot: Mapped[str] = mapped_column(String(20), nullable=False)

    transcript: Mapped[str] = mapped_column( Text, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )