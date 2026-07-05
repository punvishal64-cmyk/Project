from pydantic import BaseModel


class ActivityCreate(BaseModel):
    category: str
    task: str
    time_slot: str


class ActivityResponse(ActivityCreate):
    id: int

    class Config:
        from_attributes = True