from .RobocError import ExitRoboc
import src.param as param

class       Robot:
    """Class Robot()\n\
            | Create a new robot object.\n\
            |\n\
            | Public methods defined here:\n\
            |\n\
            | move(self, command)\n\
            |     Try to move the robot base on the command\n"""

    def     __init__(self, my_map):
        self._map = my_map
        self._map.add_robot(self)
        self.position = {'x': 0, 'y': 0}

    def     _update_coord(self, direction, coord):
        tmp = dict(coord)
        if direction == param.command_list[0]:
            coord['x'] -= 1
        elif direction == param.command_list[1]:
            coord['x'] += 1
        elif direction == param.command_list[2]:
            coord['y'] += 1
        elif direction == param.command_list[3]:
            coord['y'] -= 1
        if not self._position_is_valid(coord):
            coord['x'] = tmp['x']
            coord['y'] = tmp['y']
            return False
        else:
            return True

    def     _position_is_valid(self, coord):
        if coord['x'] < 0 or coord['y'] < 0 or\
                coord['x'] >= self._map._size['x'] or\
                coord['y'] >= self._map._size['y']:
            return False
        val = self._map.get_case(coord['x'], coord['y'])
        if val == param.wall_char:
            return False
        else:
            return True

    def     _move_toward(self, direction, length):
        coord = dict(self.position)
        while (length > 0):
            if not self._update_coord(direction, coord):
                break
            length -= 1
        del self.position
        self.position = coord

    def     move(self, command):
        try:
            direction = command[0]
            assert param.command_list.find(direction) >= 0
        except (IndexError, AssertionError):
            param.usage()
            return False
        if len(command) > 1 and not (param.is_int(command[1:])):
            param.usage()
            return False
        elif len(command) > 1:
            length = int(command[1:])
        else:
            length = 1
        self._move_toward(direction, length)
        return True
