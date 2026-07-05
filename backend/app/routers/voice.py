from pathlib import Path

from fastapi import APIRouter, File, UploadFile, Depends

from app.services.transcription import transcribe_audio
from app.services.llm import categorize_activity
from app.crud.activity import create_activity
from app.database import get_db
from app.utils.time_slot import get_current_time_slot
from app.services.sheets import append_activity

from sqlalchemy.orm import Session

router = APIRouter(prefix="/voice", tags=["Voice"])

UPLOAD_DIR = Path("uploads")  
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/upload")
async def upload_audio(file: UploadFile = File(...), 
                       db: Session = Depends(get_db),
                       ):
    
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    text = transcribe_audio(str(file_path))
    structured_output = categorize_activity(text)

    activity = create_activity(
        db=db,
        category=structured_output["category"],
        task=structured_output["task"],
        transcript=text,
        time_slot=get_current_time_slot(),
    )

    append_activity(
        time_slot=activity.time_slot,
        category=activity.category,
        task=activity.task,
        transcript=activity.transcript,
        created_at=str(activity.created_at),
    )


    return {
        "message": "Audio uploaded and transcribed successfully.",
        "filename": file.filename,
        "transcript": text,
        "analysis": structured_output,
        "id": activity.id,
    }