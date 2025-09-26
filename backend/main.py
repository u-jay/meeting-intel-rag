from fastapi import FastAPI, UploadFile, File, BackgroundTasks, Depends
from database import engine, get_db
from model import Meeting, Base
from analysis import process_meeting_file

Base.metadata.create_all(bind=engine)  # Ensure DB tables

app = FastAPI()

@app.post("/upload/")
async def upload_meeting(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    filepath = f"../upload/{file.filename}"
    with open(filepath, "wb") as f:
        f.write(await file.read())
    background_tasks.add_task(process_meeting_file, filepath, file.filename)
    return {"status": "File uploaded and processing started"}

@app.get("/meeting/{meeting_id}")
def get_meeting(meeting_id: int, db=Depends(get_db)):
    meeting = db.query(Meeting).get(meeting_id)
    if not meeting:
        return {"error": "Meeting not found"}
    return {
        "summary": meeting.summary,
        "topics": meeting.topics,
        "sentiment": meeting.sentiment,
        "actions": meeting.actions
    }
