import os
from .Map import Map
from .Robot import Robot
import src.param as param

def     run_roboc():
    #Creation d'un carte
    map = Map()
    #Creation d'un robot lier a la carte cree
    robot = Robot(map)
    map_name = None
    while map_name == None:
        map_name = get_map_choice()
    map.generate_from_file(map_name)
    param.usage()
    print(map, "\n")
    while (map._exit_coord != map.robot.position):
        command = input("--> ")
        command = command.upper()
        if command == param.quit_command:
            save = input("Entrez le nom de la sauvegarde ('Q' pour quitter): ")
            if save == 'q' or save == 'Q':
                break
            elif map.save(save):
                break
            else:
                print(map, "\n")
                continue
        robot.move(command)
        print(map, "\n")
    if (map._exit_coord == map.robot.position):
        print("\n-------------\nVictoire !!\n-------------")
    else:
        print("\nA bientôt !!")

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

