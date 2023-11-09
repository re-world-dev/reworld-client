#Auto download the lib required if nessessary
def start():
    import os
    
    print("CHECKING LIBRAIRIES...")
    
    #Ursina
    try:
        import ursina
        print("Ursina : INSTALLED")
    except ModuleNotFoundError:
        os.system("pip install ursina")
    
    #pyyaml
    try:
        import yaml
        print("PyYaml : INSTALLED")
    except ModuleNotFoundError:
        os.system("pip install pyyaml")
    
    #pydub
    try:
        import pydub
        print("Pydub : INSTALLED")
    except ModuleNotFoundError:
        os.system("pip install pydub")
    
    #requests
    try:
        import requests
        print("Request : INSTALLED")
    except ModuleNotFoundError:
        os.system("pip install requests")
    
    #discord-rich-presence
    try:
        import discordrp
        print("DiscordRichPresence : INSTALLED")
    except ModuleNotFoundError:
        os.system("pip install discord-rich-presence")
    
    print("LIBRAIRIES CHECKED !")