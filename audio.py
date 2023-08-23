from gtts import gTTS
import subprocess


def response_recorder(response_to_record):
    tts = gTTS(response_to_record, lang="fr-FR")
    tts.save("out.mp3")
    cmd = ["mpyg321", "-q", "out.mp3"]
    subprocess.call(cmd)
