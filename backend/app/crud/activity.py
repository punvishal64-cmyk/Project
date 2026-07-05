from sqlalchemy.orm import Session

from app.models.activity import Activity


def create_activity(
    db: Session,
    category: str,
    task: str,
    time_slot: str,
    transcript: str,
) -> Activity:
    activity = Activity(
        category=category,
        task=task,
        time_slot=time_slot,
        transcript=transcript,
    )

    db.add(activity)
    db.commit()
    db.refresh(activity)

    return activity