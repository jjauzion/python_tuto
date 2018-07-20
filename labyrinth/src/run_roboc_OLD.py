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
