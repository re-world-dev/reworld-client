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

class Game(object):
    def __init__(self):
        self.pt = load_texture("assets/player/texture.png")
        self.player = FirstPersonController(y=2, origon_y=-.5)
        self.player.position = Vec3(0, 2, 0)
        grass = load_texture('assets/grass.png')
        self.floor = Entity(model='plane',texture='grass', collider='box', scale=(100,1,100), texture_scale=(100, 100))
        self.player_list = []

    def add_player(self):
        pe = Entity(model="assets/player/test.obj", scale_y=1, texture=self.pt)
        pe.position = Vec3(20, 2, 20)
        self.player_list.append(pe)