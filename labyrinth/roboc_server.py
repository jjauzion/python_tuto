# -*-coding:Utf-8 -*

import socket
import select
import src.param as param
from src.run_roboc import init_game
from src.network_functions import init_server, terminate_server

map, robot = init_game()
main_connexion = init_server('', 12800)

server_run = True
start_game = False
new_connex = False
connected_client = []
while server_run:
    if not start_game:
        #Looking for connexion request on the main_coonexion 
        connexion_request, wlist, xlist =\
                select.select([main_connexion], [], [], 0.05)
        #Accept new connexion if any and add the new connexion the client list
        for connexion in connexion_request:
            client_connexion, connexion_detail = connexion.accept()
            connected_client.append(client_connexion)
            new_connex = True
        if new_connex == True:
            for client in connected_client:
                client.send("Nombre de joueur connecte (vous compris) : {}"\
                        .format(len(connected_client)).encode())
            new_connex = False
    else:
        print("Partie commencé !!")

    #Browse through the client list for active client
    active_client = []
    try:
        active_client, wlist, xlist = select.select(connected_client, [], [], 0.05)
    except select.error:
        pass
    else:
        for client in active_client:
            msg_recv = client.recv(1024)
            msg_recv = msg_recv.decode()
            print("<-- ", msg_recv)
            if msg_recv == param.start_command:
                start_game = True
            elif msg_recv == "fin":
                server_run = False
terminate_server(main_connexion, connected_client)
