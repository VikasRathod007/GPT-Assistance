import openai
import gradio
import os
from dotenv import load_dotenv
import pyttsx3

load_dotenv()
engine=pyttsx3.init()
openai.api_key = os.getenv('key')
messages = [{"role": "system", "content": "You are a Artificial Intelligence"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'english+f4')
    # engine.setProperty('voice',voices[11].id)
    slow_speech_text = f'<prosody rate="slow">{ChatGPT_reply}</prosody>'
    # os.system(f'''echo "{slow_speech_text}" | festival --tts''')

    # os.system('''echo %s | festival --tts''' % ChatGPT_reply)
    engine.say(ChatGPT_reply)
    engine.runAndWait()
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT,theme="soft",description="GPT-Chat-Bot",clear_btn="Clear", inputs = "text", outputs = "text", title = "")

demo.launch(share=True)

