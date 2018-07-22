# -*-coding:Utf-8 -*

from .RobocError import RobocError
import os
import os.path
import src.param as param

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
            | get_case(self, coord)\n\
            |     input coord shall be a dictionary with at least 'x' and 'y' key\n\
            |     Return the value of the case at coordinate (x,y)\n\
            |\n\
            | save(self, name)\n\
            |     Save the current status of the map with the name\
            given in argument. If name already exist ask for confirmation\n\
            |\n\
            | print(self)\n\
            |     Return 2d printable string of the current map\n\
            |\n\
            | __str__(self)\n\
            |     Return 2d printable string of the current map\n"""

    def     __init__(self):
        self._map = ""
        self._size = {'x': -1, 'y': -1}
        self._exit_coord = {'x': -1, 'y': -1}
        self.robot_list = []

    def     _set_map_size(self):
        self._size['y'] = len(self._map[0])
        self._size['x'] = len(self._map)

    def     _get_map_exit(self):
        self._exit_coord['x'] = 0
        for line in self._map:
            self._exit_coord['y'] = param.is_in_list(line, param.exit_char)
            if (self._exit_coord['y'] != -1):
                break
            self._exit_coord['x'] += 1

    def     _split_lines(self):
        for i, line in enumerate(self._map):
            self._map[i] = list(line)
        y_max = len(self._map[0])
        self._map[:] = [line for line in self._map if len(line) == y_max]

    def     get_map_size(self):
        return (self._size['x'], self._size['y'])

    def     add_robot(self, robot):
        self.robot_list.append(robot)

    def     generate_from_file(self, file_name):
        with open(param.maps_path + file_name, "r") as my_file:
            content = my_file.read()
        content.replace(param.robot_char, " ")
        if (content.find(param.exit_char) == -1):
            raise RobocError("Le fichier {} n'est pas une carte valide"\
                    .format(param.maps_path + file_name))
        self._map = content.split("\n")
        self._split_lines()
        self._set_map_size()
        self._get_map_exit()

    def     set_case(self, coord, value):
        self._map[coord['x']][coord['y']] = value

    def     get_case(self, coord):
        return self._map[coord['x']][coord['y']]

    def     victory(self):
        for robot in self.robot_list:
            if robot.position == self._exit_coord:
                return (robot.id)
        return None

    def     print(self, id=-1):
        tmp = []
        if hasattr(self, 'robot_list'):
            for robot in self.robot_list:
                if self.get_case(robot.position) == param.robot_char or\
                        self.get_case(robot.position) == param.foe_char:
                    tmp.append(" ")
                else:
                    tmp.append(self.get_case(robot.position))
                if robot.id == id or id < 0:
                    self._map[robot.position['x']][robot.position['y']] =\
                            param.robot_char
                elif self.get_case(robot.position) != param.robot_char:
                    self._map[robot.position['x']][robot.position['y']] =\
                            param.foe_char
        printable = []
        for line in self._map:
            printable.append("".join(line))
        printable = "\n".join(printable)
        if hasattr(self, 'robot_list'):
            i = 0
            for robot in self.robot_list:
                self._map[robot.position['x']][robot.position['y']] = tmp[i]
                i += 1
        return(printable)

    def     __str__(self):
        return (self.print())
