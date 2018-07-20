from .Map import Map
from .Robot import Robot
import os
import src.param as param

# -*-coding:Utf-8 -*

def     init_game():
    map = Map()
    print("Quelle carte voulez-vous héberger sur le serveur ?\n")
    map_name = None
    while map_name == None:
        map_name = get_map_choice()
    map.generate_from_file(map_name)
    return (map)

def     run_game(player_list, map):
    robot_list = []
    for player in player_list:
        new_robot = Robot(map, player.id)
        robot_list.append(new_robot)
    for player in player_list:
        player.send_message(map.print(player.id))
    winner = None
    while (winner == None):
        for player in player_list:
            player.send_message("*** A toi de jouer ! ***\n")
            valid_command = False
            while valid_command == False:
                player.send_message(map.print(player.id))
                command = player.messenger.recv(1024).decode("utf-8")
                if command == "fin":
                    for player2 in player_list:
                        player2.send_message("fin")
                    return False
                valid_command = robot_list[player.id - 1].move(command)
                if not valid_command:
                    player.send_message(param.str_usage())
        winner = map.victory()
    for player in player_list:
        player.send_message("----> *** Le joueur {} a gagné !! *** <----".format(winner))
        player.send_message("fin")
    return True


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
