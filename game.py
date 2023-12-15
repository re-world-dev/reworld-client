from os import environ


if __name__ == "__main__":
    raise Exception("Please run the main.py file !")

# Libs import

from libs import console 
from pydub import AudioSegment
from pydub.playback import play
from libs import assetsconf
import menu
from libs import richpresence
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Game(Entity):
    def __init__(self, app, menu, **kwargs):
        self.app = app
        self.menu = menu
        self.player = FirstPersonController(y=2, origon_y=-.5, **kwargs)
        self.player.position = Vec3(0, 2, 0)
        super().__init__(parent=self.player)
        grass = load_texture('assets/grass.png')
        self.floor = Entity(model='plane',texture='grass', collider='box', scale=(100,1,100), texture_scale=(100, 1, 100))
        self.player_list = []

        self.player.speed = 7.5


    def on_escape(self):
        destroy(self.player)
        self.menu.home_menu()
        #application.quit()

    def add_player(self):
        pl = Player(0, 1, 5, "")
        pl.show()
        self.player_list.append(pl)

    def input(self, key):

        if key == "escape":
            self.on_escape()

    def update(self):
        if held_keys["left shift"] == 1:
            self.player.camera_pivot.y = 1.5
            self.player.speed = 2.5
        elif held_keys["left control"] == 1:
            self.player.speed = 15
        else:
            self.player.speed = 7.5
            self.player.camera_pivot.y = 2
        

class Player(object):
    def __init__(self, x, y, z, name):
        self.x = x
        self.y = y
        self.z = z

        self.name = name

        self.obj_lst = []

        self.pt = load_texture("assets/player/texture2.png")

    def show(self):
        pe = Entity(model="assets/player/test.obj", scale_y=1, texture=self.pt, collider="box")
        pe.position = Vec3(self.x, self.y, self.z)
        self.obj_lst.append(pe)