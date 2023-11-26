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
import os

# WHY IS THERE 2x THE SAME THING ??? (FewerElk note)
#app = Ursina(development_mode=True)
#window.title = "RE:World"



if __name__ == '__main__':
    ######################################
    ######################################
    ######### ICON TO DEBUG ##############
    ######################################
    ######################################
    app = Ursina(title="RE:WORLD", icon="\\assets\\icon\\reicon.ico", development_mode=True, fullscreen=True)  #default icon for the moment, but can't be loaded. hum...

    screen = None  # for global statement
    modding.init()
    m = menu.Menu(app)
    #richpresence.start() >> Desactived due a bug
    app.run()
