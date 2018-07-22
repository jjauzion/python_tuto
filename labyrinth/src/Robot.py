from .RobocError import ExitRoboc
import src.param as param
from random import randrange

class       Robot:
    """Class Robot()\n\
            | Create a new robot object.\n\
            |\n\
            | Public methods defined here:\n\
            |\n\
            | move(self, command)\n\
            |     Try to move the robot base on the command\n"""

    def     _init_random_position(self, my_map):
        x, y = my_map.get_map_size()
        self.position['x'] = randrange(0, x)
        self.position['y'] = randrange(0, y)
        while my_map.get_case(self.position) == param.wall_char or\
                my_map.get_case(self.position) == param.exit_char:
            self.position['x'] = randrange(0, x)
            self.position['y'] = randrange(0, y)

    def     __init__(self, my_map, id):
        self._map = my_map
        self.position = {'x': -1, 'y': -1}
        self._init_random_position(my_map)
        self.id = id
        self._map.add_robot(self)

    def     _add_direction(self, direction, coord):
        if direction == param.command_list[0]:
            coord['x'] -= 1
        elif direction == param.command_list[1]:
            coord['x'] += 1
        elif direction == param.command_list[2]:
            coord['y'] += 1
        elif direction == param.command_list[3]:
            coord['y'] -= 1

    def     _update_coord(self, direction, coord):
        tmp = dict(coord)
        self._add_direction(direction, coord)
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
        val = self._map.get_case(coord)
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
            command = command.upper()
            direction = command[0]
            assert param.command_list.find(direction) >= 0
        except (IndexError, AssertionError):
            return False
        if command[0] == param.command_list[4] or\
                command[0] == param.command_list[5]:
            return self.wall_action(command)
        elif len(command) > 1 and not (param.is_int(command[1:])):
            return False
        elif len(command) > 1:
            length = int(command[1:])
        else:
            length = 1
        self._move_toward(direction, length)
        return True

    def     break_wall(self, command):
        coord = dict(self.position)
        self._add_direction(command[1], coord)
        if self._map.get_case(coord) != param.wall_char:
            return False
        self._map.set_case(coord, param.door_char)
        return True

    def     wallup_door(self, command):
        coord = dict(self.position)
        self._add_direction(command[1], coord)
        if self._map.get_case(coord) != param.door_char:
            return False
        self._map.set_case(coord, param.wall_char)
        return True

    def     wall_action(self, command):
        if len(command) != 2 or param.command_list[:4].find(command[1]) < 0:
            return False
        if command[0] == param.command_list[4]:
            self.wallup_door(command)
        else:
            self.break_wall(command)
        return True
