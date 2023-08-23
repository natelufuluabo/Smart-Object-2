import pygame
from io import BytesIO
from gtts import gTTS


def response_recorder(response_to_record):
    tts = gTTS(response_to_record, lang="fr")

    fp = BytesIO()
    tts.write_to_fp(fp)  # tts.save('out.mp3')
    fp.seek(0)
    pygame.mixer.init()  # utilisation de pygame pour lire les sons
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
