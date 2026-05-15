import locale

# lang = 'pt_PT', encoding = 'UTF-8'
lang, encoding = locale.getdefaultlocale()
portuguese = ["português", "portuguese", "portugiesisch"]
english = ["inglês", "english", "englisch"]
german = ["alemão", "german", "deutsch"]

while True:
    entrada = input("Digite algo: ")

    if entrada in portuguese:
        print("Você disse oi ou olá!")

    elif entrada in english:
        print("You said bye or goodbye!")

    else:
        print("Entrada não reconhecida.")