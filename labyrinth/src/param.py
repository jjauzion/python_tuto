"""This file contains the parameters of roboc game and generic functions"""

import os

maps_path = "maps/"
save_path = "maps/"

wall_char = "O"
door_char = "."
exit_char = "U"
robot_char = "X"
foe_char = "+"

command_list = "NSEO"
quit_command = "Q"
start_command = "C"

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
    print("\nGuide le robot ({}) vers la sortie ({})!".format(robot_char, exit_char))
    print("\nCommandes :")
    print("  --> '{}' + nb_de_case : Aller 'nb_de_cases' vers le nord".format(command_list[0]))
    print("  --> '{}' + nb_de_case : Aller 'nb_de_cases' vers le sud".format(command_list[1]))
    print("  --> '{}' + nb_de_case : Aller 'nb_de_cases' vers l'est".format(command_list[2]))
    print("  --> '{}' + nb_de_case : Aller 'nb_de_cases' vers l'ouest".format(command_list[3]))
    print("  --> '{}' : Sauvegarder et quitter le jeu\n".format(quit_command))

def     str_usage():
    str = "\nGuide le robot ({}) vers la sortie ({})!\n".format(robot_char, exit_char)
    str += "\nCommandes :\n"
    str += "  --> '{}' + nb_de_case : Aller 'nb_de_cases' vers le nord\n".format(command_list[0])
    str += "  --> '{}' + nb_de_case : Aller 'nb_de_cases' vers le sud\n".format(command_list[1])
    str += "  --> '{}' + nb_de_case : Aller 'nb_de_cases' vers l'est\n".format(command_list[2])
    str += "  --> '{}' + nb_de_case : Aller 'nb_de_cases' vers l'ouest\n".format(command_list[3])
    str += "  --> '{}' : Sauvegarder et quitter le jeu\n\n".format(quit_command)
    return str

def     print_heading():
    print("")
    print("/----------------------------------------------------------\\")
    print("|  _  .-')              .-. .-')                           |")
    print("| ( \( -O )             \  ( OO )                          |")
    print("|  ,------.  .-'),-----. ;-----.\  .-'),-----.    .-----.  |")
    print("|  |   /`. '( OO'  .-.  '| .-.  | ( OO'  .-.  '  '  .--./  |")
    print("|  |  /  | |/   |  | |  || '-' /_)/   |  | |  |  |  |('-.  |")
    print("|  |  |_.' |\_) |  |\|  || .-. `. \_) |  |\|  | /_) |OO  ) |")
    print("|  |  .  '.'  \ |  | |  || |  \  |  \ |  | |  | ||  |`-'|  |")
    print("|  |  |\  \    `'  '-'  '| '--'  /   `'  '-'  '(_'  '--'\  |")
    print("|  `--' '--'     `-----' `------'      `-----'    `-----'  |")
    print("\----------------------------------------------------------/\n")
