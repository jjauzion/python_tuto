# -*-coding:Utf-8 -*

import socket
import re
from src.network_functions import connect_to_server
from src.network_functions import terminate_connexions
from src.network_functions import Listener, Messenger
import src.param as param

def     get_server_ip():
    valid_ip = "^[0-9]{1,3}(.[0-9]{1,3}){3}$"
    ip = ""
    while re.search(valid_ip, ip) is None:
        ip = input("Saisissez l'adresse ip du serveur: ")
    return ip

host = "192.168.1.21"
host = get_server_ip()
port = 12800
print("Connexion au serveur en cours...")
server_messenger, player_id = connect_to_server(host, port, 30)
if not server_messenger:
    quit()
server_listener, player_id = connect_to_server(host, port, 30, player_id)
if not server_listener:
    quit()
print("Connexion au serveur réussi !")
param.print_heading()
print("Bienvenue dans le lobbie du jeu, ici tu peux attendre d'autres joueurs et chatter avec eux, ou tu peux lancé directement ta partie (#start) !")
print(param.str_usage())
messenger = Messenger(server_messenger)
listener = Listener(server_listener)
messenger.start()
listener.start()
listener.join()
messenger.stop()
messenger.join()
terminate_connexions([server_messenger, server_listener])
print("Bye !")
