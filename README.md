# voice-agent
**projet LLM agent conversationnel**


this project is a fully multinlingual agent.
its based on the langchain framework, and use llama3 as model.

the API used in this project :
- groq for the LLM provider and the text to speech transcription.
- elevenlabs for the speech to text functionnality.

all the API in this project are free to use (eleven labs include a free tier use)

for the speech to text part, it start by a voice recorder, that will be saved as the human.mp3, then sent to groq API for transcription, the returned text is then used a LLM prompt input, then it will generate an answer that will be sent to the eleven labs API, then return a an output mp3 that will be played automatically through playsound.

i use a separate system_prompt file.

