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
import translations.tr_sys as tr
import translations.tr_config as trc
import account_sys

# WHY IS THERE 2x THE SAME THING ??? (FewerElk note)
#app = Ursina(development_mode=True)
#window.title = "RE:World"

def ok():
    translations_system = tr.Translation(trc.lang)
    app = Ursina(title="RE:WORLD", icon="\\assets\\icon\\reicon.ico", development_mode=True, fullscreen=True)
    m = menu.Menu(app, translations_system)
    app.run()

if __name__ == '__main__':
    lgsys = account_sys.AccountSystem(ok=ok)
    lgsys.home()
