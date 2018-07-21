# -*-coding:Utf-8 -*

import socket
import select
import src.param as param
from src.run_roboc import init_game
from src.run_roboc import run_game
from src.network_functions import init_server, terminate_connexions
from src.server_function import add_player, chat_room
from src.player import PlayerList
from threading import Thread, RLock

map = init_game()
main_connexion = init_server('', 12800)

server_param = {"run": True, "start_game": False, "game_started": False}
connected_client = []
player_list = PlayerList()
chat_thread = Thread(target=chat_room,\
        args=(connected_client, player_list, server_param))
chat_thread.start()
while (not server_param["game_started"]) and server_param["run"]:
    if len(player_list) < param.max_player:
        #Looking for connexion request on the main_coonexion 
        connexion_request, wlist, xlist =\
                select.select([main_connexion], [], [], 0.05)
        #Accept new connexion if any and add the new connexion the client list
        for connexion in connexion_request:
            client_connexion, connexion_detail = connexion.accept()
            connected_client.append(client_connexion)
            add_player(player_list, client_connexion)
    else:
        main_connexion.close()
    if server_param["start_game"] == True:
        server_param["start_game"] = False
        server_param["game_started"] = True
main_connexion.close()
if server_param["run"] and server_param["game_started"]:
    for client in connected_client:
        client.send("Partie commencé !\nC'est au tour du joueur 1".encode("utf-8"))
    game_thread = run_game(player_list, map, server_param)
    game_thread.start()
    game_thread.join()
    server_param["run"] = False
chat_thread.join()
terminate_connexions(connected_client, main_connexion=main_connexion)
