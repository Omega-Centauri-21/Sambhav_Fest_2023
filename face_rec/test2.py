import openai
import pyttsx3
import speech_recognition as sr
import main_video_copy as mv


openai.api_key = "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"

engine = pyttsx3.init()
engine.setProperty('rate', 150)
# Set volume 0-1
engine.setProperty('volume', 1)

r = sr.Recognizer()
conversation = ""
#user_name = "You"
bot_name = "Edward"
strat_chat_log = "This is a conversation with Edward, an alien astronaut and a friend of Nilanjan aka Neelu who rescued him after his crash. He is smart, intelligent, interactive and very funny but also sometimes sarcastic. He also has a sister named Sheli"
inframe = mv.parodyFunction()
#engine.say("I spy with my own little camera eyes..." + inframe)
user_name = inframe

while True:
    
    
    with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source,duration=0.5)
      print("\nI am Listening...")
      audio= r.listen(source)
      
      try:
          text = r.recognize_google(audio)
          
          print(f"{inframe}: ", text)
          response = openai.Completion.create(
              #engine="davinci-instruct-beta-v3",
              engine="text-davinci-003",
              #engine="ft-personal-2022-12-05-20-49-22",
              max_tokens=750,
              prompt=f'{strat_chat_log}{inframe}: {text}\Edward:',
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