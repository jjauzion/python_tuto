"""This file contains the parameters of roboc game"""

maps_path = "maps/"

wall_char = "O"
door_char = "."
exit_char = "U"
robot_char = "X"

command_list = "QNSEO"

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
