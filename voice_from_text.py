from gtts import gTTS
import os

# Text to be converted to speech
text = "Hello, welcome to the Voice from Text project!"

# Language for speech
language = 'en'

# Initialize gTTS object
tts = gTTS(text=text, lang=language, slow=False)

# Save the speech to an MP3 file
tts.save("output.mp3")

# Play the saved MP3 file
os.system("start output.mp3")  # For Windows, use 'start'. For Mac, use 'afplay', and for Linux, use 'mpg321'.
