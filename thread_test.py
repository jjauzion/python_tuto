'''
import random
import sys
from threading import Thread
import time

class Afficheur(Thread):

    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 20:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            i += 1

thread1 = Afficheur("1")
thread2 = Afficheur("2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()
'''

import random
import sys
from threading import Thread, RLock
import time

verrou = RLock()

class Afficheur(Thread):

    """Thread chargé simplement d'afficher un mot dans la console."""

    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 5:
            with verrou:
                for lettre in self.mot:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
            i += 1

# Création des threads
thread_1 = Afficheur("canard")
thread_2 = Afficheur("TORTUE")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()
