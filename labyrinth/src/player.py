class       Player():
    """A player is defined by:\
            -> it's id (proctected attribute)\
            -> it's listener socket\
            -> it's messenger socket\
        No required argument at player creation"""

    nb_of_player = 0
    used_id = []

    def     __init__(self):
        Player.nb_of_player += 1
        self._id = Player.nb_of_player
        Player.used_id.append(self._id)

    def     _get_id(self):
        return self._id

    def     _set_id(self, id):
        if Player.used_id.count(id) > 0:
            print("id déjà utilisé..")
        else:
            self._id = id

    id = property(_get_id, _set_id)

    def     set_listener(self, connexion):
        self.listener = connexion
        self.listener_socket = connexion.getpeername()

    def     set_messenger(self, connexion):
        self.messenger = connexion
        self.messenger_socket = connexion.getpeername()

    def     send_message(self, msg):
        self.listener.send(msg.encode("utf-8"))

class PlayerList():
    """List of player"""

    def     __init__(self):
        self.list = []

    def     __iter__(self):
        for player in self.list:
            yield player

    def     __len__(self):
        return len(self.list)

    def     get_id(self, socket):
        for player in self.list:
            if player.listener_socket == socket or player.messenger_socket == socket:
                return player.id
        return -1

    def     set_listener(self, id, connexion):
        for player in self.list:
            if player.id == id:
                player.set_listener(connexion)
                break
