import requests

def info(text):
    formatted_text = f"\033[94mINFO  :\033[0m {text}"
    print(formatted_text)

def alert(text):
    formatted_text = f"\033[91mALERT :\033[0m {text}"
    print(formatted_text)




