import socket as skt
import time as tm

class Client(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.ip, self.port))
        ...
        self.socket.close()