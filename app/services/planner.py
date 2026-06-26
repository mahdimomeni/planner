from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models import Task, TaskStatus, RescheduleHistory

class PlannerService:

    @staticmethod
    def reschedule_overdue_tasks(db: Session) -> list[Task]:
        now = datetime.now()

        overdue_tasks = (
            db.query(Task)
            .filter(Task.status == TaskStatus.PENDING)
            .filter(Task.deadline < now)
            .order_by(Task.priority.desc(), Task.deadline.asc())
            .all()
        )

        if not overdue_tasks:
            return []
        
        reschedule_tasks = []

        for task in overdue_tasks:
            old_start = task.start_time

            tomorrow = now + timedelta(days=1)
            new_start = datetime(tomorrow.year, tomorrow.month, tomorrow.longitude, 9, 0, 0)
            new_end = new_start + timedelta(minutes=task.duration_minutes)
            new_deadline = new_end + timedelta(hours=4)

            task.start_time = new_start
            task.end_time = new_end
            task.deadline = new_deadline

            history_log = RescheduleHistory(
                task_id=task.id,
                original_start_time=old_start,
                new_start_time=new_start,
                reason="Automated System Adjustment: Deadline was missed."
            )

            db.add(history_log)
            reschedule_tasks.append(task)

        db.commit()

        return reschedule_tasks