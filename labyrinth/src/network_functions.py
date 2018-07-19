# -*-coding:Utf-8 -*

import socket
import select
import time
from threading import Thread, RLock

locker = RLock()

class   Listener(Thread):
    """Create a thread that listen and print message on an openned connexion"""
    def __init__(self, connexion):
        Thread.__init__(self)
        self.connexion = connexion
    def run(self):
        msg = b""
        while msg.decode() != "fin":
            with locker:
                msg = self.connexion.recv(1024)
            print(msg.decode())
            time.sleep(0.05)

class   Messenger(Thread):
    """Create a thread that send message on an openned connexion"""
    def __init__(self, connexion):
        Thread.__init__(self)
        self.connexion = connexion
    def run(self):
        msg = ""
        while msg != "fin":
            with locker:
                msg = input("> ")
                self.connexion.send(msg.encode())
            time.sleep(0.05)

def     init_server(hote, port):
    main_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_connexion.bind((hote, port))
    main_connexion.listen(5)
    print("Serveur en écoute sur le port {}".format(port))
    return main_connexion

def     terminate_server(main_connexion, connected_client):
    for client in connected_client:
        client.send(b"fin")
        client.close()
    main_connexion.close()
    print("Connexion terminée")

def     connect_to_server(hote, port, timeout):
    start = time.time()
    connected = False
    wait_time = 0
    while (wait_time < timeout and connected == False):
        try:
            connexion_to_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connexion_to_server.connect((hote, port))
        except ConnectionRefusedError:
            connected = False
            wait_time = time.time() - start
        else:
            connected = True
    if wait_time >= timeout:
        print("Timeout: connexion to server failed...")
        return None
    else:
        print("Connexion établie avec le serveur sur le port {}".format(port))
        return connexion_to_server 
