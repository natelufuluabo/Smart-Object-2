from speech_recognition import Recognizer, Microphone

recognizer = Recognizer()
hotwords = [
    "Ouvrir la lumière",
    "Allumer la lumière",
    "Fermer la lumière",
    "Éteindre la lumière",
    "Ouvrir la lumière de l’entrée",
    "Allumer la lumière de l’entrée",
    "Fermer la lumière de l’entrée",
    "Éteindre la lumière de l’entrée",
    "Ouvrir la lumière du salon",
    "Allumer la lumière du salon",
    "Fermer la lumière du salon",
    "Éteindre la lumière du salon",
    "Quelle heure est-il?",
    "Il est quelle heure?",
    "Quel temps fait-il?",
]


def commande_recorder():
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
        for hotword in hotwords:
            if hotword in text:
                if hotword in {"Ouvrir la lumière", "Allumer la lumière"}:
                    pass
                elif hotword in {"Fermer la lumière", "Éteindre la lumière"}:
                    pass
                elif hotword in {
                    "Ouvrir la lumière de l’entrée",
                    "Allumer la lumière de l’entrée",
                }:
                    pass
                elif hotword in {
                    "Fermer la lumière de l’entrée",
                    "Éteindre la lumière de l’entrée",
                }:
                    pass
                elif hotword in {
                    "Ouvrir la lumière du salon",
                    "Allumer la lumière du salon",
                }:
                    pass
                elif hotword in {
                    "Fermer la lumière du salon",
                    "Éteindre la lumière du salon",
                }:
                    pass
                elif hotword in {"Quelle heure est-il?", "Il est quelle heure?"}:
                    pass
                elif hotword == "Quel temps fait-il?":
                    pass
            else:
                pass

    except Exception as ex:
        print(ex)
