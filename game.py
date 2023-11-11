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

grass = load_texture('a')
floor = Entity(model='cube',texture='grass',Collider='mesh')
