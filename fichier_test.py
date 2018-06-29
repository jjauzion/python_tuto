#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

myfile = open("fichier.txt", "r")
content = myfile.read()
print(content, end="")
myfile.close()
with open("fichier.txt", "a") as myfile:
    myfile.write("j'ecrit dans le fichier {} \n".format(10))
print(myfile.closed)

import pickle

score = {
        "joueur1": 5,
        "joueur2": 10,
        "joueur3": 1,
        }

with open("save", "wb") as myfile:
    mypickle = pickle.Pickler(myfile)
    mypickle.dump(score)

with open("save", "rb") as myfile:
    mypickle = pickle.Unpickler(myfile)
    score_in_file = mypickle.load()

print(score_in_file)
