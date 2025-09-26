import chromadb

def index_transcript(transcript):
    client = chromadb.Client()
    collection = client.create_collection("meetings")
    collection.add(documents=[transcript])
