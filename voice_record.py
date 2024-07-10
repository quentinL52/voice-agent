import sounddevice as sd
import numpy as np
import wave
import threading
import os

def record_audio(filename=r"voice_LLM/human.mp3", samplerate=44100, channels=2):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    audio_data = []


    def callback(indata, frames, time, status):
        if status:
            print(status)
        audio_data.append(indata.copy())

    def stop_recording():
        input("Je suis a l'ecoute.... appuis sur entrée pour que je te reponde")
        nonlocal recording
        recording = False

    threading.Thread(target=stop_recording).start()

    recording = True
    try:
        with sd.InputStream(samplerate=samplerate, channels=channels, dtype='int16', callback=callback):
            while recording:
                sd.sleep(100)
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    audio_data = np.concatenate(audio_data, axis=0)

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2) 
        wf.setframerate(samplerate)
        wf.writeframes(audio_data.tobytes())
    
record_audio()