"""This file contains the parameters of roboc game"""

maps_path = "maps/"
save_path = "maps/"

wall_char = "W"
door_char = "."
exit_char = "U"
robot_char = "X"

command_list = "NSEO"
quit_command = "Q"

def     is_int(nb):
    try:
        value = int(nb)
        return True
    except ValueError:
        return False

def     is_in_list(list, value):
    try:
        return list.index(value)
    except ValueError:
        return -1

def     usage():
    print("\nCommandes :")
    print("  --> '{}' + nb_de_case : Aller 'nb_de_cases' vers le nord".format(command_list[0]))
    print("  --> '{}' + nb_de_case : Aller 'nb_de_cases' vers le sud".format(command_list[1]))
    print("  --> '{}' + nb_de_case : Aller 'nb_de_cases' vers le est".format(command_list[2]))
    print("  --> '{}' + nb_de_case : Aller 'nb_de_cases' vers le ouest".format(command_list[3]))
    print("  --> '{}' : Sauvegarder et quitter le jeu\n".format(quit_command))
