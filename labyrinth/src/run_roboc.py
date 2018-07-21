from .Map import Map
from .Robot import Robot
import os
import src.param as param
from threading import Thread, RLock
import time

# -*-coding:Utf-8 -*

def     init_game():
    map = Map()
    print("Quelle carte voulez-vous héberger sur le serveur ?\n")
    map_name = None
    while map_name == None:
        map_name = get_map_choice()
    map.generate_from_file(map_name)
    return (map)

locker = RLock()

def     game_manager(player_list, robot_list, map, server_param):
    winner = None
    while (winner == None and server_param["run"]):
        for player in player_list:
            with locker:
                player.command = None
                player.send_message("\n*** A toi de jouer ! ***\n")
                player.send_message(map.print(player.id))
            valid_command = False
            while valid_command == False and server_param["run"]:
                command = None
                while (command == None) and server_param["run"]:
                    with locker:
                        command = player.command
                    time.sleep(0.1)
                if not command or command == param.exit_command:
                    return
                valid_command = robot_list[player.id - 1].move(command)
                with locker:
                    if not valid_command:
                        player.send_message(param.str_usage())
                    player.command = None
            with locker:
                player.send_message(map.print(player.id))
            winner = map.victory()
            if winner:
                break
            player.send_message("\n*** C'est au tour des autres joueurs... ***\n")
    for player in player_list:
        with locker:
            if player.id != winner:
                player.send_message("*** Perdu !! Le joueur {} a gagné... *** <----\n".format(winner))
            else:
                player.send_message("----> *** Bravo !! Vous avez gagné ! *** <----\n".format(winner))

def     run_game(player_list, map, server_param):
    robot_list = []
    for player in player_list:
        new_robot = Robot(map, player.id)
        robot_list.append(new_robot)
        player.command = None
    for player in player_list:
        player.send_message(map.print(player.id))
    game_thread = Thread(target=game_manager, args=(player_list, robot_list, map, server_param))
    return game_thread


def     get_map_choice():
    """Ask user to enter the map number.\n\
            Return the map name corresponding to the number entered by the user\n\
            or return None if the number entered is wrong"""

    maps = get_map_list()
    map_number = input("\nEntrez le numéro de labyrinthe pour commencer à jouer : ")
    try:
        map_number = int(map_number)
        assert map_number - 1 < len(maps) and map_number >= 1
        return maps[map_number - 1]
    except (ValueError, AssertionError):
        print("\nMauvaise saisie !\n")
        return None

def     get_map_list():
    """Print the list of available maps in the maps folder\
    (defined in param.py) and return a list with the maps name"""

    maps = os.listdir(param.maps_path)
    print("Labyrinthes existants :")
    for i, map in enumerate(maps):
        if map.find(".txt") != -1:
            map = map.replace(".txt", "")
            print("  {} - {}.".format(i + 1, map))
    return maps
