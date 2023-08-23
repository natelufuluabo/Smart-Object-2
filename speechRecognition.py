import datetime
from speech_recognition import Recognizer, Microphone
from audio import response_recorder
from weather import get_current_temp

recognizer = Recognizer()

current_time = datetime.datetime.now()

hours_minutes = current_time.strftime("%H:%M")


def command_recorder():
    # On enregistre le son
    with Microphone() as source:
        print("Réglage du bruit ambiant... Patientez...")
        recognizer.adjust_for_ambient_noise(source)
        print("Vous pouvez parler...")
        recorded_audio = recognizer.listen(source)
        print("Enregistrement terminé !")

    # Reconnaissance de l'audio
    try:
        print("Reconnaissance du texte...")
        text = recognizer.recognize_google(recorded_audio, language="fr-FR")
        print("Vous avez dit : {}".format(text))
        if text in {
            "ouvrir la lumière de l'entrée",
            "allumer la lumière de l'entrée",
        }:
            response_recorder("La lumière de l’entrée est allumée")
        elif text in {
            "fermer la lumière de l'entrée",
            "éteindre la lumière de l'entrée",
        }:
            response_recorder("La lumière de l’entrée est éteinte")
        elif text in {
            "ouvrir la lumière du salon",
            "allumer la lumière du salon",
        }:
            response_recorder("La lumière du salon est allumée")
        elif text in {
            "fermer la lumière du salon",
            "éteindre la lumière du salon",
        }:
            response_recorder("la lumière du salon est éteinte")
        elif text in {"quelle heure est-il", "il est quelle heure"}:
            response_recorder(f"Il est {hours_minutes}")
        elif text == "quel temps fait-il":
            response_recorder(f"Il fait {get_current_temp()} degrés")
        elif text in {"ouvrir la lumière", "allumer la lumière"}:
            response_recorder(
                "Dans quelle pièce souhaiteriez-vous allumer les lumières ?"
            )
        elif text in {"fermer la lumière", "éteindre la lumière"}:
            response_recorder(
                "Dans quelle pièce souhaiteriez-vous éteindre les lumières ?"
            )
        else:
            response_recorder("Commande invalide")

    except Exception as ex:
        response_recorder("Aucune commande détectée")
