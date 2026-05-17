import locale, platform, sys, os
# lang = 'pt_PT', encoding = 'UTF-8'
encoding = locale.getencoding()
lang, _ = locale.getlocale()
cpu_architecture = platform.machine()
portuguese = ["português", "portuguese", "portugiesisch"]
english = ["inglês", "english", "englisch"]
german = ["alemão", "german", "deutsch"]
filesystems = ["ext4", "brtfs", "gpfs"]
if encoding != "UTF-8":
    print("Your system's encoding is not UTF-8. Please change it to UTF-8 to continue.")
    sys.exit(1)
caminho_modelo = '/proc/device-tree/model'
if os.path.exists(caminho_modelo): # Verifica se o arquivo existe (sistemas x86 comuns não têm essa árvore de dispositivos)
    try:
        with open(caminho_modelo, 'r') as f:
            modelo = f.read().strip()
            if "Raspberry Pi 5" in modelo and cpu_architecture == "aarch64":
                RASPBERRY = True
            # If not a Raspberry Pi 5 and not aarch64, exit with code 1
            elif "Raspberry Pi 5" in modelo is False and (cpu_architecture == "aarch64") is False:
                sys.exit(1)
    except Exception:
        print("Could not read the device model.")

# Installation for amd64 architecture
if cpu_architecture == "x86_64":
    while True:
        if encoding == "UTF-8":
            if lang == "pt_PT":
                print("Idioma detectado: Português")
                entrada = input("Que idioma deseja definir com padrão? ").lower()
                if entrada == "":
                    entrada = "portuguese"
                break
            elif lang == "en_US":
                print("Language detected: English")
                entrada = input("What language would you like to set as default? ").lower()
                if entrada == "":
                    entrada = "english"
                break
            elif lang == "de_DE":
                print("Sprache erkannt: Deutsch")
                entrada = input("Welche Sprache möchten Sie als Standard festlegen? ").lower()
                if entrada == "":
                    entrada = "german"
                break
    if entrada in portuguese:
        
    elif entrada in english:
        
    elif entrada in german:
        
    else:
        