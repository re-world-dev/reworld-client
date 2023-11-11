from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.stdpy import thread 
from libs import richpresence

if __name__ == "__main__":
    raise Exception("Please run the main.py file !")

class Menu(object):
    def __init__(self, app):
        self.app = app
        self.home_menu()

    def home_menu(self):
        self.clear()
        # Sky(texture=modding.sky_getskypath())
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text="RE:WORLD", wordwrap=10, x=-0.9, y=0.1, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
        self.bplay = Button(text='Play', color=color.azure, scale=.10, text_origin=(-.100, -0.1), x=-0.8)
        self.bplay.on_click = self.play_menu
        self.bplay.tooltip = Tooltip('Start a new journey')
        self.bpExit = Button(text='Exit', color=color.azure, scale=.10, text_origin=(-.100, -0.1), x=-0.8, y=-0.1)
        self.bpExit.on_click = application.quit
        self.bpExit.tooltip = Tooltip('Exit')

    def play_menu(self):
        self.clear()
        # Sky(texture=modding.sky_getskypath())
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text="Select a mode", wordwrap=10, x=-0.9, y=0.1, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
        self.bsolo = Button(text='SOLO', color=color.azure, scale=.10, text_origin=(-.100, -0.1), x=-0.8)
        self.bsolo.on_click = application.quit
        self.bsolo.tooltip = Tooltip('Start a new journey')

        self.bmulti = Button(text='MULTIPLAYERS', color=color.azure, scale=.10, text_origin=(-.100, -0.1), x=-0.8, y=-0.1)
        self.bmulti.on_click = self.server_list
        self.bmulti.tooltip = Tooltip('Multiplayer mode')

        self.breturn = Button(text='Return', color=color.azure, scale=.10, text_origin=(-.100, -0.1), x=-0.8, y=-0.2)
        self.breturn.on_click = self.home_menu
        self.breturn.tooltip = Tooltip('Return to home menu')

    def server_list(self):
        self.clear()
        # Sky(texture=modding.sky_getskypath())
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text="SERVER LIST", wordwrap=10, x=-0.9, y=0.1, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
        baddsrv = Button(text='Add a server', color=color.azure, scale=.10, text_origin=(-.100, -0.1), x=-0.8)
        baddsrv.on_click = application.quit
        baddsrv.tooltip = Tooltip('Add a new online game area !')
        bret = Button(text='Return', color=color.azure, scale=.10, text_origin=(-.100, -0.1), x=-0.8, y=-0.1)
        bret.on_click = self.home_menu
        bret.tooltip = Tooltip('Exit')

    def clear(self):
        #home_menu
        try:
            destroy(self.title)
            destroy(self.bplay)
            destroy(self.bpExit)
        except:
            pass
        #play_menu
        try:
            destroy(self.title)
            destroy(self.bsolo)
            destroy(self.bmulti)
            destroy(self.breturn)
        except:
            pass