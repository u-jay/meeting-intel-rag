import ollama

def analyze_transcript(transcript):
    prompt = f"Summarize meeting, extract topics, sentiment, action items: {transcript}"
    response = ollama.generate(model="llama3", prompt=prompt)
    return response['summary'], response['topics'], response['sentiment'], response['actions']
