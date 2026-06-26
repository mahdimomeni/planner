from datetime import datetime
from enum import Enum as PyEnum
from typing import List, Optional
from sqlalchemy import ForeignKey, String, DateTime, Integer, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class TaskStatus(str, PyEnum):
    PENDING = "pending"
    COMPLETED = "completed"
    BACKLOGGED = "backlogged"

class Priority(str, PyEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)

    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    deadline: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, default=30)

    reschedule_logs: Mapped[List["RescheduleHistory"]] = relationship("RescheduleHistory", back_populates="task", cascade="all, delete-orphan")

class RescheduleHistory(Base):
    __tablename__ = "reschedule_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    task_id: Mapped[int] = mapped_column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)

    original_start_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    new_start_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    rescheduled_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    reason: Mapped[str] = mapped_column(String(255), default="System automated adjustment")

    task: Mapped["Task"] = relationship("Task", back_populates="reschedule_logs")