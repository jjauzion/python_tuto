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
            |     Exemple : Q -> Save and quit\n"""

    def     __init__(self, my_map):
        self._my_map = my_map

    def     _move_toward(self, direction, length):
        print("dir : {} ; distance : {}".format(direction, length))

    def     move(self, command, param):
        try:
            direction = command[0]
            assert param.command_list.find(direction) >= 0
        except (IndexError, AssertionError):
            print("Wrong command! Usage: [N | S | E | O][nb] | Q")
        else:
            length = command[1:]
            self._move_toward(direction, length)

