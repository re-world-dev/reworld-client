from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.stdpy import thread 
from libs import richpresence
import client_main as client
from threading import Thread

if __name__ == "__main__":
    raise Exception("Please run the main.py file !")

class Menu(object):
    def __init__(self, app):
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

    def home_menu(self):
        self.clear()
        # Sky(texture=modding.sky_getskypath())
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text="RE:WORLD", wordwrap=10, x=-0.1, y=0.1, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
        self.bplay = Button(text="Play", y=0, scale=0.1, color=color.azure, text_origin=(-.100, -0.1))
        self.bplay.on_click = self.play_menu
        self.bplay.tooltip = Tooltip('Start a new journey')
        self.bpExit = Button(text="Exit", y=-.1, scale=0.1, color=color.orange, text_origin=(-.100, -0.1))
        self.bpExit.on_click = application.quit
        self.bpExit.tooltip = Tooltip('See you soon !')

    def play_menu(self):
        self.clear()
        # Sky(texture=modding.sky_getskypath())
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text="Select a mode", wordwrap=10, x=-0.85, y=0.15, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
        self.bsolo = Button(text='Solo', color=color.azure, scale=.15, text_origin=(-.100, -0.1), x=-0.8)
        self.bsolo.on_click = application.quit
        self.bsolo.tooltip = Tooltip('Start a new journey')

        self.bmulti = Button(text='Multiplayer', color=color.azure, scale=.15, text_origin=(-.100, -0.1), x=-0.8, y=-0.15)
        self.bmulti.on_click = self.server_list
        self.bmulti.tooltip = Tooltip('Multiplayer mode')

        self.breturn = Button(text='Return', color=color.azure, scale=.15, text_origin=(-.100, -0.1), x=-0.8, y=-0.3)
        self.breturn.on_click = self.home_menu
        self.breturn.tooltip = Tooltip('Return to home menu')

    def server_list(self):
        self.clear()
        # Sky(texture=modding.sky_getskypath())
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text="SERVER LIST", wordwrap=10, x=-0.85, y=0.15, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
        self.baddsrv = Button(text='Add a server', color=color.azure, scale=.10, text_origin=(-.100, -0.1), x=-0.8)
        self.baddsrv.on_click = self.add_server
        self.baddsrv.tooltip = Tooltip('Add a new online game area !')
        self.bret = Button(text='Return', color=color.azure, scale=.10, text_origin=(-.100, -0.1), x=-0.8, y=-0.1)
        self.bret.on_click = self.play_menu
        self.bret.tooltip = Tooltip('Return to play menu')

        for i, ip in enumerate(self.server_list_ips):
            btn = Button(text=ip, y=i*-0.1, scale=0.1, color=color.azure, text_origin=(-.100, -0.1))
            btn.on_click = lambda: self.connect(ip)
            self.server_objects.append(btn)

    def connect(self, ip):
        self.ip = ip
        self.clear()
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text="Connecting...\nPlease wait.", wordwrap=0, x=-0, y=0, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
        self.stop = Button(text="CANCEL", y=-0.1, scale=0.1, color=color.azure, text_origin=(-.100, -0.1))
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
            self.title = Text(text=f"Failed to connect to the server:\n{e}", wordwrap=0, x=-5, y=0, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
            self.stop = Button(text="Return to server list", y=-0.1, scale=0.1, color=color.azure, text_origin=(-.100, -0.1))
            self.stop.on_click = self.server_list
        ...


    def add_server(self):
        self.clear()
        Text.default_resolution = 1080 * Text.size
        self.title = Text(text="ADD A SERVER", wordwrap=10, x=-0.1, y=0.1, scale=1.5)  # Augmentez la valeur de 'scale' pour agrandir le texte.
        self.entry = InputField(label="Server ip", wordwrap=10)

        self.bconfirm = Button(text='Add', color=color.azure, scale=.10, text_origin=(-.100, -0.1), y=-0.1)
        self.bconfirm.on_click = self.confirm_add_server
        self.bconfirm.tooltip = Tooltip('Add the server to your list')

        self.bcancel = Button(text='Return', color=color.azure, scale=.10, text_origin=(-.100, -0.1), y=-0.2)
        self.bcancel.on_click = self.server_list
        self.bcancel.tooltip = Tooltip('Return to server list')

    def confirm_add_server(self):
        ip = self.entry.text
        self.server_list_ips.append(ip)
        with open("saves/servers/serverlist.txt", 'a') as file:
            file.write(ip + "\n")
        self.server_list()

    def clear(self):
        #home_menu
        try:
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