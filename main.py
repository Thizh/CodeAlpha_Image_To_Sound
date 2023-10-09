'''
Project Name: Text to Speech

Author: Thisitha Wickramarachchi

Description: This program uses pytesseract library for Optical Character Recognition and Google Text To Speech (gTTS) python library to convert text into speech. 
To run this program you need to be connected to the internet.
'''
# sudo apt install tesseract-ocr
# pip install gTTS playsound

from PIL import Image
import pytesseract
import numpy as np
import gtts
from playsound import playsound

# convert image to text
imgFile = 'image_01.jpg'
img1 = np.array(Image.open(imgFile))
text = pytesseract.image_to_string(img1)

#convert text into speech
def textToSpeech(text) :
    tts = gtts.gTTS(text=text, lang='en')
    speechFile = "speech.mp3" # save the synthesized speech to a mp3 file
    tts.save(speechFile)
    playsound(speechFile)

textToSpeech(text)