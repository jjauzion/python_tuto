class       RobocError(Exception):
    """Exception raised in case of wrong input for Roboc game"""

    def     __init__(self, message):
        self.message = message

    def     __str__(self):
        return self.message
