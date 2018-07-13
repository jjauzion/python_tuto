class       RobocError(Exception):
    """Exception raised in case of wrong input for Roboc game"""

    def     __init__(self, message):
        self.message = message

    def     __str__(self):
        return self.message

class       ExitRoboc(BaseException):
    """Exception raised to exit programs Roboc"""

    def     __init__(self, message):
        self.message = message

    def     __str__(self):
        return self.message
