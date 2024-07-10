import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from groq_speech import speechgroq
from playsound import playsound
from voice_record import record_audio
from text2speech import text_to_speech_file

load_dotenv()

groq_api = os.getenv('GROQ_API_KEY')

def read_system_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
file_path = 'system_prompt.txt'

system_prompt = read_system_prompt(file_path)

chat = ChatGroq(temperature=0.2, groq_api_key=groq_api, model_name="llama3-70b-8192")
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system_prompt), ("human", human)])
chain = prompt | chat

texte = speechgroq("voice_LLM\human.mp3")
reponse = chain.invoke({"text": texte})
text_to_speech_file(reponse.content)
playsound("voice_LLM\output.mp3")
