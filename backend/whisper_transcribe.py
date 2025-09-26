import subprocess

def transcribe_audio(filepath):
    subprocess.run(["./whisper.cpp", "-f", filepath, "-o", "transcript.txt"])
    with open("transcript.txt") as f:
        return f.read()
