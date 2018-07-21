"""This file contains the parameters of roboc game and generic functions"""

import os

maps_path = "maps/"
save_path = "maps/"

wall_char = "O"
door_char = "."
exit_char = "U"
robot_char = "X"
foe_char = "+"

"""
command_list structure :
    command_list[0] -> move north
    command_list[1] -> move south
    command_list[2] -> move east
    command_list[3] -> move west
    command_list[4] -> wall-up door
    command_list[5] -> break wall
"""
command_list = "NSEOMP"

start_command = "start"
exit_command = "exit"
command_char = "#"

max_player = 5

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

def     str_usage():
    str = "\nGuide ton robot ({}) vers la sortie ({}) avant les autres ({})!\n".format(robot_char, exit_char, foe_char)
    str += "\nChat :\n"
    str += "  --> 'texte' : envoie 'texte' aux autres joueurs\n"
    str += "\nCommandes de jeu:\n"
    str += "  --> '{}{}' + nb_de_case : Aller 'nb_de_cases' vers le nord\n".format(command_char, command_list[0])
    str += "  --> '{}{}' + nb_de_case : Aller 'nb_de_cases' vers le sud\n".format(command_char, command_list[1])
    str += "  --> '{}{}' + nb_de_case : Aller 'nb_de_cases' vers l'est\n".format(command_char, command_list[2])
    str += "  --> '{}{}' + nb_de_case : Aller 'nb_de_cases' vers l'ouest\n".format(command_char, command_list[3])
    str += "  --> '{}{}' + direction : Murer la porte situé sur la case pointé par direction\n".format(command_char, command_list[4])
    str += "  --> '{}{}' + direction : Casser le murer situé sur la case pointé par direction\n".format(command_char, command_list[5])
    str += "\nCommandes serveur:\n"
    str += "  --> '{}{}' : Démarre la partie si vous êtes dans le lobbie\n".format(command_char, start_command)
    str += "  --> '{}{}' : Interromps la partie et désactive le serveur\n".format(command_char, exit_command)
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
