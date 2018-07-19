# -*-coding:Utf-8 -*

import socket
from src.network_functions import connect_to_server
from src.network_functions import terminate_server
from src.network_functions import Listener, Messenger
import src.param as param

param.print_heading()
print("Connexion au serveur en cours...")
server_connexion = connect_to_server("localhost", 12800, 30)
if not server_connexion:
    quit()
msg = ""
while msg != b'fin':
    msg = server_connexion.recv(1024)
    print(msg.decode())
    msg = input("> ")
    msg = msg.encode()
    server_connexion.send(msg)
terminate_server(server_connexion, [])
