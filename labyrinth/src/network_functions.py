# -*-coding:Utf-8 -*

import socket
import select
import time
from threading import Thread, RLock, Event
import src.param as param

class   Listener(Thread):
    """Create a thread that listen and print message on an openned connexion"""
    def __init__(self, connexion):
        Thread.__init__(self)
        self.connexion = connexion
    def run(self):
        msg = b""
        while msg.decode() != "fin":
            msg = self.connexion.recv(1024)
            print("\n" + msg.decode("utf-8") + "\n> ", end = "")
            time.sleep(0.05)

class   Messenger(Thread):
    """Create a thread that send message on an openned connexion"""
    def __init__(self, connexion):
        Thread.__init__(self)
        self.connexion = connexion
        self._stop_event = Event()
    def stop(self):
        self._stop_event.set()
    def stopped(self):
        return self._stop_event.is_set()
    def run(self):
        msg = ""
        while msg != "fin":
            msg = input("> ")
            if self.stopped():
                print("*** Message non remis, le serveur a été stoppé ***")
                break
            self.connexion.send(msg.encode("utf-8"))

def     init_server(hote, port):
    main_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_connexion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    main_connexion.bind((hote, port))
    main_connexion.listen(5)
    print("Serveur en écoute sur le port {}".format(port))
    return main_connexion

def     terminate_connexions(connexion_list, main_connexion=None):
    nb_of_connexion = 0
    for client in connexion_list:
        if main_connexion:
            client.send(b"fin")
        client.close()
        nb_of_connexion += 1
    if main_connexion:
        main_connexion.close()
        nb_of_connexion += 1
    print("{} connexion(s) closed".format(nb_of_connexion))

def     connect_to_server(hote, port, timeout, player_id=-1):
    start = time.time()
    connected = False
    wait_time = 0
    while (wait_time < timeout and connected == False):
        try:
            connexion_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connexion_to_server.connect((hote, port))
        except ConnectionRefusedError:
            if wait_time == 0:
                print("(...timeout dans {} sec)".format(timeout))
            connected = False
            wait_time = time.time() - start
        else:
            connected = True
    if wait_time >= timeout:
        print("Timeout: echec de la connexion au serveur...")
        return None, None
    else:
        if player_id < 0:
            player_id = request_id(connexion_to_server)
        else:
            connexion_to_server.send("id = {}".format(player_id).encode("utf-8"))
        return connexion_to_server, player_id


def     request_id(connexion):
    connexion.send("request_id".encode("utf-8"))
    player_id = connexion.recv(1024).decode("utf-8")
    player_id = int(player_id)
    print("Vous êtes le joueur {}".format(player_id))
    return player_id
