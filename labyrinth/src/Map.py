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
        self._robot_coord = {'x': -1, 'y': -1}
        self._size = {'x': -1, 'y': -1}
        self._exit_coord = {'x': -1, 'y': -1}

    def     _find_robot(self, param):
        self._robot_coord['y'] = 0
        for line in self._map:
            self._robot_coord['x'] = line.find(param.robot_char)
            if (self._robot_coord['x'] != -1):
                break
            self._robot_coord['y'] += 1

    def     _get_map_size(self):
        self._size['x'] = len(self._map[0])
        self._size['y'] = len(self._map)

    def     _get_map_exit(self, param):
        self._exit_coord['y'] = 0
        for line in self._map:
            self._exit_coord['x'] = line.find(param.exit_char)
            if (self._exit_coord['x'] != -1):
                break
            self._exit_coord['y'] += 1

    def     generate_from_file(self, file_name, param):
        with open(param.maps_path + file_name, "r") as my_file:
            content = my_file.read()
        if (content.find(param.robot_char) == -1) |\
                (content.find(param.exit_char) == -1):
            raise RobocError("Le fichier {} n'est pas une carte valide"\
                    .format(param.maps_path + file_name))
        self._map = content.split("\n")
        self._get_map_size()
        self._get_map_exit(param)
        self._find_robot(param)

    def     print(self):
        print("\n".join(self._map))

    def     __str__(self):
        return("\n".join(self._map))
