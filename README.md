# Edward - AI Chatbot and Face Recognition System
Edward is an AI-powered chatbot and face recognition system developed for the TechFest Sambhav 2k23. The project integrates speech recognition, OpenAI's GPT-3 API, and facial recognition to create an interactive assistant capable of real-time conversation and face identification.


## Features
- **AI Chatbot:** Engage in conversations with Edward using natural language processing via OpenAI's GPT-3 API. See `ai_chatbot.py` and `chatbot.py`.

- **Speech Recognition:** Interact with Edward using voice commands, implemented with the speech_recognition library in voice.py.

- **Face Recognition:** Identify and recognize faces from a video feed using the SimpleFacerec class in simple_facerec.py.

## Prerequisites
- Python 3.x
- Webcam (for face recognition)
- Microphone (for voice interaction)
- OpenAI API key (obtain from OpenAI)
- Required Python libraries:
    - `openai`
    - `pyttsx3`
    - `speech_recognition`
    - `opencv-python`
    - `face_recognition`
    - `numpy`


## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/Sambhav_Fest_2023.git
cd Sambhav_Fest_2023
```

2. **Install the required Python libraries:**

```
pip install openai pyttsx3 speechrecognition opencv-python face_recognition numpy
```


3. **Set up the OpenAI API key:**

- Replace the placeholder API key in the `api_key` file with your actual OpenAI API key.

4. **Prepare face images for recognition:**

- Place images of known individuals in the `images` directory.
- The `load_encoding_images` method will encode these images for recognition.


## Usage

**Running the AI Chatbot**

To start the chatbot, run:

```python
python ai_chatbot.py
```

This script uses the OpenAI API to generate responses and `pyttsx3` for text-to-speech output.

**Running the Face Recognition System**

To start face recognition, run:
```python
python face_rec/main_video.py
```

This will open a video feed window that detects and labels known faces using your webcam.

**Running the Voice Interaction with Face Recognition**
For an interactive experience combining voice commands and face recognition, run:

```python
python face_rec/test.py
```

or
```python3
python face_rec/test2.py
```

These scripts integrate voice recognition, the AI chatbot, and face recognition.

## License

This project is licensed under the GNU General Public License v3.0.