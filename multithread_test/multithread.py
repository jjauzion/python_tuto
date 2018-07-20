# -*-coding:Utf-8 -*

from threading import Thread
import time

class Afficheur(Thread):

    def __init__(self, msg):
        Thread.__init__(self)
        self.msg = msg

    def run(self):
        i = 0
        while i < 20:
            print(self.msg)
            time.sleep(0.5)
            i += 1

class Liseur(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        i = 0
        while i < 20:
            msg = input("> ")
            print("msg = ", msg)
            i += 1

aff = Afficheur("affiche")
lis = Liseur()

aff.start()
lis.start()

aff.join()
lis.join()
