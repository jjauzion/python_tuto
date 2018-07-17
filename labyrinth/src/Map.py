from .RobocError import RobocError
from os import makedirs
from os.path import exists, isfile
from .param import *

class       Map:
    """Class Map()\n\
            | Create a new map object.\n\
            |\n\
            | Public methods defined here:\n\
            |\n\
            | generate_from_file(self, file_name)\n\
            |     Generate the map from the file in argument.\n\
            |     Path of the map file is defined in param.py\n\
            |\n\
            | add_robot(self, robot)\n\
            |     Link robot to the map\n\
            |\n\
            | get_case(self, x, y)\n\
            |     Return the value of the case at coordinate (x,y)\n\
            |\n\
            | save(self, name)\n\
            |     Save the current status of the map with the name\
            given in argument. If name already exist ask for confirmation\n\
            |\n\
            | __str__(self)\n\
            |     Return 2d printable string of the current map\n"""

    def     __init__(self):
        self._map = ""
        self._size = {'x': -1, 'y': -1}
        self._exit_coord = {'x': -1, 'y': -1}

    def     _find_robot(self):
        self.robot.position['x'] = 0
        for line in self._map:
            self.robot.position['y'] = is_in_list(line, robot_char)
            if (self.robot.position['y'] != -1):
                break
            self.robot.position['x'] += 1
        self._map[self.robot.position['x']][self.robot.position['y']]\
                = " "

    def     _get_map_size(self):
        self._size['y'] = len(self._map[0])
        self._size['x'] = len(self._map)

    def     _get_map_exit(self):
        self._exit_coord['x'] = 0
        for line in self._map:
            self._exit_coord['y'] = is_in_list(line, exit_char)
            if (self._exit_coord['y'] != -1):
                break
            self._exit_coord['x'] += 1

    def     _split_lines(self):
        for i, line in enumerate(self._map):
            self._map[i] = list(line)

    def     add_robot(self, robot):
        self.robot = robot

    def     generate_from_file(self, file_name):
        with open(maps_path + file_name, "r") as my_file:
            content = my_file.read()
        if (content.find(robot_char) == -1) |\
                (content.find(exit_char) == -1):
            raise RobocError("Le fichier {} n'est pas une carte valide"\
                    .format(maps_path + file_name))
        self._map = content.split("\n")
        self._split_lines()
        self._get_map_size()
        self._get_map_exit()
        self._find_robot()

    def     get_case(self, x, y):
        return self._map[x][y]

    def     save(self, name):
        if name == "":
            print("La partie n'a pas été sauvegardé")
            return False
        if not exists(save_path):
            makedirs(save_path)
        if isfile(save_path + name + ".txt"):
            confirm = input("Ce nom est déjà pris. Voulez-vous écraser le labyrinthe existant? (o pour confirmer)\n")
            if confirm != "o":
                print("La partie n'a pas été sauvegardé")
                return False
        save = self.__str__()
        with open(save_path + name + ".txt", 'w') as my_file:
            my_file.write(save)
            print("Sauvegarde effectué ! ({})".format(save_path + name + ".txt"))
        return True

    def     __str__(self):
        if hasattr(self, 'robot'):
            tmp = self._map[self.robot.position['x']][self.robot.position['y']]
            self._map[self.robot.position['x']][self.robot.position['y']] =\
                    'X' ## A CHANGER !!! par robot_char
        printable = []
        for line in self._map:
            printable.append("".join(line))
        printable = "\n".join(printable)
        if hasattr(self, 'robot'):
            self._map[self.robot.position['x']][self.robot.position['y']] = tmp
        return(printable)
