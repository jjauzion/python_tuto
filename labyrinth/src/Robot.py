from .RobocError import ExitRoboc

class       Robot:
    """Class Robot()\n\
            | Create a new robot object.\n\
            |\n\
            | Methods defined here:\n\
            |\n\
            | move(self, command)\n\
            |     Try to move the robot base on the command\n\
            |     List of command (Q, N, E, S, O)\n\
            |     Exemple : E3 -> move robot to 3 case East bound\n\
            |     Exemple : S -> move robot 1 case south\n\
            |     Exemple : Q -> Save and quit\n"""

    def     __init__(self, my_map):
        self._map = my_map
        self.position = {'x': 0, 'y': 0}

    def     _update_coord(self, direction, coord, param):
        tmp = dict(coord)
        if direction == 'N':
            coord['x'] -= 1
        elif direction == 'S':
            coord['x'] += 1
        elif direction == 'O':
            coord['y'] -= 1
        elif direction == 'E':
            coord['y'] += 1
        if not self._position_is_valid(coord, param):
            coord['x'] = tmp['x']
            coord['y'] = tmp['y']
            return False
        else:
            return True

    def     _position_is_valid(self, coord, param):
        if coord['x'] < 0 or coord['y'] < 0:
            return False
        val = self._map.get_case(coord['x'], coord['y'])
        if val == param.wall_char:
            return False
        else:
            return True

    def     _move_toward(self, direction, length, param):
        coord = dict(self.position)
        while (length > 0):
            if not self._update_coord(direction, coord, param):
                break
            length -= 1
        del self.position
        self.position = coord

    def     move(self, command, param):
        try:
            direction = command[0]
            assert param.command_list.find(direction) >= 0
        except (IndexError, AssertionError):
            print("Wrong command! Usage: [N | S | E | O][nb] | Q")
        else:
            if len(command) > 1 and not (param.is_int(command[1:])):
                return False
            elif len(command) > 1:
                length = int(command[1:])
            else:
                length = 1
            self._move_toward(direction, length, param)
            return True

