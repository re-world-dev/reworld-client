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

        t1 = WallTool()
        i1= Item(-1, 10, 2) 


        self.inventory = Inventory(self)


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
            if self.inventory.state == 1:
                self.inventory.close()
            self.on_escape()
        if key == "e":
            self.inventory.toggle()
        if key == "scroll up":
            if self.inventory.state == 1:
                self.inventory.right()
        if key == "scroll down":
            if self.inventory.state == 1:
                self.inventory.left()

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

class Tool(object):
    def __init__(self, model, texture=None):
        self.model = model
        self.self = Entity(model=model, parent=camera.ui, scale=1, color=color.gold, position=(.2, -.2))

    def action_1(self):
        pass

    def action_2(self):
        pass

class Stack(object):
    def __init__(self, id:int, inv):
        self.id = id
        self.inv = inv
        self.item = None
        
    def set(self, item:Tool):
        self.item = item

class Inventory(object):
    def __init__(self, player:Game):
        self.player = player
        #Stack (name_id)
        #To expand later
        self.hand_0 = Stack(0, self)
        self.c1_1 = Stack(1, self)
        self.c2_2 = Stack(2, self)
        self.c3_3 = Stack(3, self)
        self.c4_4 = Stack(4, self)
        self.state = 0
        self.selected = 0

    def open(self):
        self.overlay = [Button(text="", color=color.white, scale=(.05, 0.05), x=0, y=0), 
                        Button(text="", color=color.white, scale=(.05, 0.05), x=.1, y=-.15), 
                        Button(text="", color=color.white, scale=(.05, 0.05), x=.2, y=-.15), 
                        Button(text="", color=color.white, scale=(.05, 0.05), x=.3, y=-.15), 
                        Button(text="", color=color.white, scale=(.05, 0.05), x=.4, y=-.15)]
        self.state = 1
        self.select(self.selected)

    def close(self):
        for btn in self.overlay:
            #specific overlay class later ?
            destroy(btn)
        self.overlay = []
        self.state = 0

    def unselect_all(self):
        if self.state == 1:
            for btn in self.overlay:
                btn.color = color.white
        else:
            print("the unselect_all method was called but no inventory was open !")

    def select(self, id):
        if self.state == 1:
            self.unselect_all()
            btn = self.overlay[id]
            btn.color = color.blue
        else:
            print("the select method was called but no inventory was open !")

    def left(self):
        self.selected += 1
        try:
            self.select(self.selected)
        except IndexError:
            self.selected = 0
            self.select(self.selected)

    def right(self):
        self.selected -= 1
        try:
            self.select(self.selected)
        except IndexError:
            self.selected = len(self.overlay) - 1
            self.select(self.selected)

    def toggle(self):
        if self.state == 0:
            self.open()
        elif self.state == 1:
            self.close()
        else:
            raise RuntimeError("Something went wrong with the inventory : an unknow state was entered.")

class WallTool(Tool):
    def __init__(self):
        super().__init__(self, "assets/tools/walltool/walltool.obj")

class Item(Entity):
    def __init__(self, x, y, z):
        super().__init__(model="assets\player\test.obj", color=color.gold, x=x, y=y, z=z, scale=1)

        self.on_click = destroy(self)