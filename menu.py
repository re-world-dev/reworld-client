from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.stdpy import thread 
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