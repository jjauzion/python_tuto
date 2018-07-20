# -*-coding:Utf-8 -*

import select
from src.player import Player
import src.param as param

def     add_player(player_list, connexion):
    who = connexion.recv(1024).decode("utf-8")
    if who == "request_id":
        new_player = Player()
        new_player.set_messenger(connexion)
        player_list.list.append(new_player)
        connexion.send("{}".format(new_player.id).encode("utf-8"))
    else:
        player_id = int(who[5:])
        player_list.set_listener(player_id, connexion)
        for player in player_list:
            player.send_message("---> Nombre de joueur connecte (vous compris) : {}"\
                    .format(len(player_list)))

def     chat_room(connected_client, player_list, server_param):
    active_client = []
    try:
        active_client, wlist, xlist = select.select(connected_client, [], [], 0.05)
    except select.error:
        pass
    else:
        for client in active_client:
            msg_recv = client.recv(1024).decode("utf-8")
            print("<-- ", msg_recv)
            if msg_recv == param.start_command:
                server_param["start_game"] = True
            elif msg_recv == "fin":
                server_param["run"] = False
            else:
                player_id = player_list.get_id(client.getpeername())
                for player in player_list:
                    if player_id != player.id:
                        player.send_message("Joueur {}: ".format(player_id)\
                                +  msg_recv)
