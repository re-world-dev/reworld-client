from os import environ

#===================
#     RE:WORLD
#===================

# Libs import
import modding #RML (reworld mod loader)
from libs import console 
from pydub import AudioSegment
from pydub.playback import play
from libs import assetsconf
loading_screen = None
console.info("-----------------------------")
console.info("RE:WORLD")
console.info("2023 The RE:WORLD project")
console.info("-----------------------------")
console.info("Discord : https://discord.gg/EauquJY6aQ")

console.info("Main/Render : Game init")
modding.init()
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.stdpy import thread 

app = Ursina(development_mode=True)
window.title = "RE:World"

def home_menu():
    # Sky(texture=modding.sky_getskypath())
    Text.default_resolution = 1080 * Text.size
    test = Text(text="RE:WORLD", wordwrap=10, x=-0.9, y=0.1, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
    bplay = Button(text='Play', color=color.azure, scale=.10, text_origin=(-.100, -0.1), x=-0.8)
    bplay.on_click = application.quit
    bplay.tooltip = Tooltip('Start a new journey')
    bpExit = Button(text='Exit', color=color.azure, scale=.10, text_origin=(-.100, -0.1), x=-0.8, y=-0.1)
    bpExit.on_click = application.quit
    bpExit.tooltip = Tooltip('Exit')

if __name__ == '__main__':
    app = Ursina()

    screen = None  # for global statement

    home_menu()
    app.run()
