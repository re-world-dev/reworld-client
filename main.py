from os import environ

#===================
#     RE:WORLD
#===================

#Libs checks
import auto_lib_install as ali
ali.start()


def exec(code):
    exec(code)
# Libs import
import modding #RML (reworld mod loader)
from libs import console 
from pydub import AudioSegment
from pydub.playback import play
from libs import assetsconf
import menu
from libs import richpresence

loading_screen = None
console.info("-----------------------------")
console.info("RE:WORLD")
console.info("2023 The RE:WORLD project")
console.info("-----------------------------")
console.info("Discord : https://discord.gg/EauquJY6aQ")

console.info("Main/Render : Game init")

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.stdpy import thread 

app = Ursina(development_mode=True)
window.title = "RE:World"



if __name__ == '__main__':
    app = Ursina()

    screen = None  # for global statement
    modding.init()
    menu.home_menu()
    #richpresence.start() >> Desactived due a bug
    app.run()
