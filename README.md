# meeting-intel-rag
# Meeting Insights RAG

## Backend Setup
1. Install Python dependencies:
    pip install -r backend/requirements.txt
2. Download and build whisper.cpp binary in backend/
3. Start Ollama server and pull model (e.g., "ollama pull llama3")
4. Start FastAPI backend:
    uvicorn backend.main:app --reload

## Frontend Setup
cd frontend/
npm install
npm start

## Usage
- Open http://localhost:3000 in browser
- Upload an audio/video meeting file
- API will process and extract meeting summary, topics, sentiment, actions
- Query insights via: http://localhost:8000/meeting/{meeting_id}
