import locale

# lang = 'pt_PT', encoding = 'UTF-8'
encoding = locale.getencoding()
lang, _ = locale.getlocale()
portuguese = ["português", "portuguese", "portugiesisch"]
english = ["inglês", "english", "englisch"]
german = ["alemão", "german", "deutsch"]

while True:
    if encoding != "UTF-8":
        print("Your system's encoding is not UTF-8. Please change it to UTF-8 to continue.")
        break
    elif encoding == "UTF-8":
        if lang == "pt_PT":
            print("Idioma detectado: Português")
            entrada = input("Que idioma deseja definir com padrão? ").lower()
        elif lang == "en_US":
            print("Language detected: English")
            entrada = input("What language would you like to set as default? ").lower()
        elif lang == "de_DE":
            print("Sprache erkannt: Deutsch")
            entrada = input("Welche Sprache möchten Sie als Standard festlegen? ").lower()


if entrada in portuguese:
    print("Idioma definido para português!")

elif entrada in english:
    print("Language set to English!")

elif entrada in german:
    print("Sprache auf Deutsch eingestellt!")

else:
    print("Language not recognized or unavailable.")