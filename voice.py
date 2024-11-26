import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = "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"

engine = pyttsx3.init()
engine.setProperty('rate', 150)
# Set volume 0-1
engine.setProperty('volume', 1)

r = sr.Recognizer()
conversation = ""
user_name = "You"
bot_name = "Edward"
strat_chat_log = ""

while True:
    with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source,duration=0.5)
      print("\nI am Listening...")
      audio= r.listen(source)
      try:
          text = r.recognize_google(audio)
          print("You: ", text)
          response = openai.Completion.create(
              #engine="davinci-instruct-beta-v3",
              engine="text-davinci-003",
              #engine="ft-personal-2022-12-05-20-49-22",
              max_tokens=750,
              prompt=f'{strat_chat_log}You: {text}\Edward:',
              temperature=0.8,
              top_p=1,
              frequency_penalty=0.45,
              presence_penalty=0.20
              )
          print("Edward: ", response["choices"][0]["text"])
          say= response["choices"][0]["text"]
    
      except:
          continue

    engine.say(say) 
    engine.runAndWait()         