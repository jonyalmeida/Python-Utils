import io
import pygame
from gtts import gTTS


def speak(text):
    with io.BytesIO() as file:
        gTTS(tesxt=text, lang="en").write_to_fp(file)
        file.seek(0)
        pygame.mixer.init()
