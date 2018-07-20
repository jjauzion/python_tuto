# -*-coding:Utf-8 -*

import socket
import select
import src.param as param
from src.run_roboc import init_game
from src.run_roboc import run_game
from src.network_functions import init_server, terminate_connexions
from src.server_function import add_player, chat_room
from src.player import PlayerList

map = init_game()
main_connexion = init_server('', 12800)

server_param = {"run": True, "start_game": False, "game_started": False}
connected_client = []
player_list = PlayerList()
while server_param["run"]:
    if not server_param["game_started"]:
        #Looking for connexion request on the main_coonexion 
        connexion_request, wlist, xlist =\
                select.select([main_connexion], [], [], 0.05)
        #Accept new connexion if any and add the new connexion the client list
        for connexion in connexion_request:
            client_connexion, connexion_detail = connexion.accept()
            connected_client.append(client_connexion)
            add_player(player_list, client_connexion)
    if server_param["start_game"] == True:
        server_param["start_game"] = False
        server_param["game_started"] = True
        main_connexion.close()
        for client in connected_client:
            client.send("Partie commencé !".encode("utf-8"))
        run_game(player_list, map)
    chat_room(connected_client, player_list, server_param)
terminate_connexions(connected_client, main_connexion=main_connexion)
