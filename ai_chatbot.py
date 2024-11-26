import openai
import pyttsx3
import speech_recognition as sr

# openai.api_key = "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"
#openai.api_key = "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"
#openai.api_key = "sk-S0XEPg2XhjCozeFEtIIT3BIbkFJf7hu4sNyxCLCEDCw8XK4" #with I
openai.api_key = "sk-S0XEPg2XhjCozeFEtllT3BlbkFJf7hu4sNyxCLCEDCw8XK4" #with l (L)

engine = pyttsx3.init()
# engine.setProperty('rate', 150)
# # Set volume 0-1
# engine.setProperty('volume', 1)

# Making changes to make the audio more human-like
# Configure voice modulation and tone
voices = engine.getProperty('voices')
# Select the first voice (index 0)
voice = voices[0]
# Set the voice rate (default is 200)
engine.setProperty('rate', 150)
# Set the voice pitch (default is 50)
engine.setProperty('pitch', 100)
# Set the voice volume (default is 1.0)
engine.setProperty('volume', 0.8)
# Set the voice gender (default is 'neutral')
#engine.setProperty('gender', 'female')


r = sr.Recognizer()
conversation = ""
user_name = "You"
bot_name = "Edward"
strat_chat_log = "This is a conversation with Edward, an alien astronaut who was rescued and rebuilt by the agile students of DY Patil College of Engineering, Akurdi, lead by Nilanjan Paul aka Neelu. He now lives among the students of the college, stranded from his friends and family after the crash. He is smart, intelligent, interactive and funny but ocassionally also sarcastic. The Director is Retd. Admiral Amit Vikram, Principal Dr. Malti Ma'am and Head of Innovation cell Dr. Manish Sharma Sir respectively. Have a humor of 90%"

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