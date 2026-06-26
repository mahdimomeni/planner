from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.models import TaskStatus, Priority

class TaskBase(BaseModel):
    title: str = Field(..., max_length=100, examples=["Review System Architecture"])
    description: Optional[str] = Field(None, max_length=500)
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    deadline: datetime
    duration_minutes: int = Field(30, ge=15, description="Duration in minutes, minimum 15")
    priority: Priority = Priority.MEDIUM

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    deadline: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    priority: Optional[Priority] = None
    status: Optional[TaskStatus] = None

class TaskResponse(TaskBase):
    id: int
    status: TaskStatus
    created_at: datetime

    class Config:
        from_attributes = True