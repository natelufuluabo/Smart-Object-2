from io import BytesIO
import pygame
from gtts import gTTS


def response_recorder(response_to_record):
    tts = gTTS(response_to_record, lang="fr")

    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
