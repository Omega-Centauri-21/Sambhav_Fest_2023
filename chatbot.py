import openai
import pyttsx3
import speech_recognition as sr
#from api_key import API_KEY


# openai.api_key = "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"
#openai.api_key = "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"
#openai.api_key = "sk-S0XEPg2XhjCozeFEtIIT3BIbkFJf7hu4sNyxCLCEDCw8XK4" #with I
openai.api_key = "sk-S0XEPg2XhjCozeFEtllT3BlbkFJf7hu4sNyxCLCEDCw8XK4" #with l (L)

engine = pyttsx3.init()

r = sr.Recognizer()



conversation = ""
user_name = "You"
bot_name = "Jarvis"

while True:
    with sr.Microphone() as source:
        print("\nlistening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    print("no longer listening.\n")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

    prompt = user_name + ": " + user_input + "\n" + bot_name+ ": "

    conversation += prompt  # allows for context

    # fetch response from open AI api
    response = openai.Completion.create(engine='text-davinci-001', prompt=conversation, max_tokens=100)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

    conversation += response_str + "\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()