import openai
import pyttsx3
import speech_recognition as sr
#from api_key import API_KEY

openai.api_key = "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"

engine = pyttsx3.init()

r = sr.Recognizer()
conversation = ""
user_name = "You"
bot_name = "Edward"
strat_chat_log = "This is a conversation with Edward, an alien astronaut who was rescued and rebuilt by the agile students of DY Patil College of Engineering, Akurdi. He now live among the students of the college, stranded from his friends and family after the crash. He is smart, interactive and funny."
while True:
    with sr.Microphone() as source:
      r.adjust_for_ambient_noise(source,duration=1)
      print("\nListening...")
      #audio= r.listen(source)
      audio = str(input())
      try:
          #text = r.recognize_google(audio)
          #print(text)
          print(audio)
      except:
             continue

    #prompt =  user_name + ": " + audio + "\n" + bot_name+ ": "
    prompt =  f'{strat_chat_log}You: {audio}\Edward:'

    conversation += prompt  # allows for context

    # fetch response from open AI api
    response = openai.Completion.create(engine='text-davinci-003', prompt=conversation, max_tokens=100)
    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

    conversation += response_str + "\n"
    print(response_str)

    #engine.say(response_str)
    #engine.runAndWait()



'''import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou: How many pounds are in a kilogram?\nMarv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\nYou: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\nYou: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\nYou: What is the meaning of life?\nMarv: I’m not sure. I’ll ask my friend Google.\nYou: What time is it?\nMarv:",
  temperature=0.5,
  max_tokens=60,
  top_p=0.3,
  frequency_penalty=0.5,
  presence_penalty=0
)
'''