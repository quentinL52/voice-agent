import os
from groq import Groq

client = Groq()

filename = r"voice_LLM\human.mp3"

def speechgroq(audiofile):
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
        file=(filename, file.read()),
        model="whisper-large-v3",        
        )
        return transcription.text
    
if __name__ == "__main__":
    print(speechgroq(r"voice_LLM\human.mp3"))

