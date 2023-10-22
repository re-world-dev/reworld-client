#===================
#     RE:WORLD
#===================
# Console Libraries


import requests
import datetime

def info(text):
    formatted_text = f"\033[94mINFO  :\033[0m {text}"
    print(str(datetime.datetime.now()) + " " + formatted_text)

def alert(text):
    formatted_text = f"\033[91mALERT :\033[0m {text}"
    print(str(datetime.datetime.now()) +" " +formatted_text)




