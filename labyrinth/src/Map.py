from .RobocError import RobocError

class       Map:
    """Class Map()\n\
            | Create a new map object.\n\
            |\n\
            | Methods defined here:\n\
            |\n\
            | generate_from_file(self, file_name, param)\n\
            |     Generate the map from the file in argument.\n\
            |     Path of the map file is defined in param.py\n\
            |\n\
            | __str__(self)\n\
            |     Return 2d printable string of the current map\n"""

    def     __init__(self):
        self._map = ""
        self._size = {'x': -1, 'y': -1}
        self._exit_coord = {'x': -1, 'y': -1}

    def     _find_robot(self, param):
        self.robot.position['x'] = 0
        for line in self._map:
            self.robot.position['y'] = param.is_in_list(line, param.robot_char)
            if (self.robot.position['y'] != -1):
                break
            self.robot.position['x'] += 1
        self._map[self.robot.position['x']][self.robot.position['y']]\
                = " "

    def     _get_map_size(self):
        self._size['y'] = len(self._map[0])
        self._size['x'] = len(self._map)

    def     _get_map_exit(self, param):
        self._exit_coord['x'] = 0
        for line in self._map:
            self._exit_coord['y'] = param.is_in_list(line, param.exit_char)
            if (self._exit_coord['y'] != -1):
                break
            self._exit_coord['x'] += 1

    def     _split_lines(self):
        for i, line in enumerate(self._map):
            self._map[i] = list(line)

    def     add_robot(self, robot):
        self.robot = robot

    def     generate_from_file(self, file_name, param):
        with open(param.maps_path + file_name, "r") as my_file:
            content = my_file.read()
        if (content.find(param.robot_char) == -1) |\
                (content.find(param.exit_char) == -1):
            raise RobocError("Le fichier {} n'est pas une carte valide"\
                    .format(param.maps_path + file_name))
        self._map = content.split("\n")
        self._split_lines()
        self._get_map_size()
        self._get_map_exit(param)
        self._find_robot(param)

    def     get_case(self, x, y):
        return self._map[x][y]

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
