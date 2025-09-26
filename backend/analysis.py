from whisper_transcribe import transcribe_audio
from ollama_llm import analyze_transcript
from chroma_index import index_transcript
from database import SessionLocal
from models import Meeting

def process_meeting_file(filepath, filename):
    transcript = transcribe_audio(filepath)
    summary, topics, sentiment, actions = analyze_transcript(transcript)
    index_transcript(transcript)
    db = SessionLocal()
    meeting = Meeting(
        filename=filename,
        summary=summary,
        topics=topics,
        sentiment=sentiment,
        actions=actions
    )
    db.add(meeting)
    db.commit()
    db.close()
