import os
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE = os.getenv("VOICE_ID")
if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY environment variable not set")

client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

voice = VOICE
def text_to_speech_file(text: str) -> str:
    response = client.text_to_speech.convert(
        voice_id='GgV5QStPLpmkN7FOHJtY',  
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2", 
        voice_settings=VoiceSettings(
            stability=0.3,
            similarity_boost=1.0,
            style=0.5,
            use_speaker_boost=True,
        ),
    )

    save_file_path = "voice_LLM\output.mp3"

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)
    return save_file_path


if __name__ == "__main__":
    text_to_speech_file(" ")