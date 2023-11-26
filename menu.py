from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.stdpy import thread 
from libs import richpresence
import client_main as client
from threading import Thread
from random import *

if __name__ == "__main__":
    raise Exception("Please run the main.py file !")

class Menu(object):
    def __init__(self, app, tr):
        self.tr = tr
        self.dic = self.tr.gv_tr_dic()
        video = 'assets/sound/music/b.mp4'

        e4 = Entity(model='cube', texture=video, scale=(0, 0))
        video_sound = app.loader.loadSfx(video)
        video_sound.play()

        self.app = app
        self.server_list_ips = []
        self.server_objects = []
        self.load_servers()
        self.home_menu()

    def load_servers(self):
        """Load the servers from the file"""
        with open("saves/servers/serverlist.txt", 'r') as file:
            servers = file.read()
            lst_srv = servers.split("\n")
            for srv in lst_srv:
                if srv == "":
                    continue
                self.server_list_ips.append(srv)

    def home_menu(self):        #OK
        self.clear()
        # Sky(texture=modding.sky_getskypath())
        Sky(texture="assets/background/homemenu/background1.png")
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text="RE:WORLD", wordwrap=10, x=-0.1, y=0.1, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.

        self.bplay = Button(text=self.dic["menu.home.play.button"], y=0, scale=0.1, color=color.azure, text_origin=(-.100, -0.1))
        self.bplay.on_click = self.play_menu
        self.bplay.tooltip = Tooltip(self.dic["menu.home.play.tooltip"])

        self.bpExit = Button(text=self.dic["menu.home.exit.button"], y=-.1, scale=0.1, color=color.orange, text_origin=(-.100, -0.1))
        self.bpExit.on_click = application.quit
        self.bpExit.tooltip = Tooltip(self.dic["menu.home.exit.tooltip"])

        self.bcredits = Button(text=self.dic["menu.home.credits.button"], y=-.4, scale=0.1, color=color.azure, text_origin=(-.100, -0.1))
        self.bcredits.on_click = self.credits
        self.bcredits.tooltip = Tooltip(self.dic["menu.home.credits.tooltip"])

    def play_menu(self):        # OK
        self.clear()
        # Sky(texture=modding.sky_getskypath())
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text=self.dic["menu.play.title"], wordwrap=10, x=-0.85, y=0.15, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
        self.bsolo = Button(text=self.dic["menu.play.solo.button"], color=color.azure, scale=(.15, 0.1), text_origin=(-.100, -0.1), x=-0.8)
        self.bsolo.on_click = application.quit
        self.bsolo.tooltip = Tooltip(self.dic["menu.play.solo.tooltip"])

        self.bmulti = Button(text=self.dic["menu.play.multi.button"], color=color.azure, scale=(.15, 0.1), text_origin=(-.100, -0.1), x=-0.8, y=-0.1)
        self.bmulti.on_click = self.server_list
        self.bmulti.tooltip = Tooltip(self.dic["menu.play.multi.tooltip"])

        self.breturn = Button(text=self.dic["menu.play.return.button"], color=color.azure, scale=(.15, 0.1), text_origin=(-.100, -0.1), x=-0.8, y=-0.2)
        self.breturn.on_click = self.home_menu
        self.breturn.tooltip = Tooltip(self.dic["menu.play.return.tooltip"])

    def server_list(self):      #
        self.clear()
        # Sky(texture=modding.sky_getskypath())
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text=self.dic["menu.serverlist.title"], wordwrap=10, x=-0.85, y=0.15, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
        self.baddsrv = Button(text=self.dic["menu.serverlist.add.button"], color=color.azure, scale=(.15, .10), text_origin=(-.100, -0.1), x=-0.8)
        self.baddsrv.on_click = self.add_server
        self.baddsrv.tooltip = Tooltip(self.dic["menu.serverlist.add.tooltip"])
        self.bret = Button(text=self.dic["menu.serverlist.return.button"], color=color.azure, scale=(.15, .10), text_origin=(-.100, -0.1), x=-0.8, y=-0.1)
        self.bret.on_click = self.play_menu
        self.bret.tooltip = Tooltip(self.dic["menu.serverlist.return.tooltip"])

        for i, ip in enumerate(self.server_list_ips):
            btn = Button(text=ip, y=i*-0.1, scale=0.1, color=color.azure, text_origin=(-.100, -0.1))
            btn.on_click = lambda: self.connect(ip)
            self.server_objects.append(btn)

    def connect(self, ip):
        self.ip = ip
        self.clear()
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text=self.dic["menu.connection.label.working"], wordwrap=0, x=-0, y=0, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
        self.stop = Button(text=self.dic["menu.connection.stop.button"], y=-0.1, scale=0.1, color=color.azure, text_origin=(-.100, -0.1))
        self.stop.on_click = self.cancel_co
        
        t = Thread(target=self._connect)
        t.start()

    def cancel_co(self):
        self.cl.socket.close()
        time.sleep(1)
        self.server_list()

    def _connect(self):
        self.cl = client.Client(self.ip, 9605)
        try:
            self.cl.connect()
        except Exception as e:
            self.clear()
            Text.default_resolution = 1080 * Text.size
            self.title = Text(text=self.dic["menu.connection.failed.label"].format(e), wordwrap=0, x=-5, y=0, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
            self.stop = Button(text=self.dic["menu.connection.failed.button"], y=-0.1, scale=0.1, color=color.azure, text_origin=(-.100, -0.1))
            self.stop.on_click = self.server_list
        ...


    def add_server(self):
        self.clear()
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text=self.dic["menu.servercreation.title"], wordwrap=10, x=-0.1, y=0.1, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
        self.entry = InputField(label="Server ip", wordwrap=10, color=color.white)

        self.bconfirm = Button(text=self.dic["menu.servercreation.add.button"], color=color.azure, scale=.10, text_origin=(-.100, -0.1), y=-0.1)
        self.bconfirm.on_click = self.confirm_add_server
        self.bconfirm.tooltip = Tooltip(self.dic["menu.servercreation.add.tooltip"])

        self.bcancel = Button(text=self.dic["menu.servercreation.exit.button"], color=color.azure, scale=.10, text_origin=(-.100, -0.1), y=-0.2)
        self.bcancel.on_click = self.server_list
        self.bcancel.tooltip = Tooltip(self.dic["menu.servercreation.exit.tooltip"])

    def confirm_add_server(self):
        ip = self.entry.text
        self.server_list_ips.append(ip)
        with open("saves/servers/serverlist.txt", 'a') as file:
            file.write(ip + "\n")
        self.server_list()

    def credits(self):
        self.clear()
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text="CREDITS", wordwrap=50, y=0.1, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
        self.dev_t = Text(text="Developpers : ", wordwrap=50, y=0, scale=1.5)
        self.dev_1 = Text(text="EletrixTime (https://github.com/EletrixtimeYT)", wordwrap=50, y=-0.1, scale=1.5)
        self.dev_2 = Text(text="FewerElk (https://github.com/FewerElk)", wordwrap=50, y=-0.2, scale=1.5)
        self.dev_3 = Text(text="coder1max (https://github.com/coder1max)", wordwrap=50, y=-0.3, scale=1.5)
        #I hope I don't forget some one...

        self.titlem = Text(text="Music by :", wordwrap=10, y=-0.4, scale=1.5)
        self.m = Text(text="FewerElk (https://github.com/FewerElk)", wordwrap=10, y=-0.5, scale=1.5)

        self.bret = Button(text='Return', color=color.azure, scale=.10, text_origin=(-.100, -0.1), y=-.4)
        self.bret.on_click = self.home_menu

    def clear(self):
        try:
            destroy(self.title)
            destroy(self.dev_t)
            destroy(self.dev_1)
            destroy(self.dev_2)
            destroy(self.dev_3)
            destroy(self.titlem)
            destroy(self.m)
            destroy(self.bret)
        except:
            pass
        #home_menu
        try:
            destroy(self.bcredits)
            destroy(self.title)
            destroy(self.stop)
        except:
            pass
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
        #server list
        try:
            destroy(self.title)
            destroy(self.baddsrv)
            destroy(self.bret)
        except:
            pass
        #add server menu
        try:
            destroy(self.title)
            destroy(self.entry)
            destroy(self.bconfirm)
            destroy(self.bcancel)
        except:
            pass
        try:
            for i in self.server_objects:
                destroy(i)
            self.server_objects = []
        except:
            pass