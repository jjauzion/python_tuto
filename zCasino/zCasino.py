#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

from random import *
from math import ceil

print("Welcome to the Z Casino :)\n")

cash = -1
while cash < 0:
    try:
        cash = input("Combien voulez convertir en jeton ? $")
        cash = int(cash)
        assert cash > 0
    except ValueError as error_return:
        print("There is an error :/ ", error_return)
        continue
    except AssertionError:
        print("Common... negative amount really?")
        continue
print(chr(27) + "[2J")
while cash > 0:
    print("\n---------------------\nVos jetons: ", cash,"$\n")
    try:
        mise = input("Allez roulette! Combien voulez-vous miser sur ce coup?\
 ('q' pour quitter)\n") 
        if (mise == "q"):
            break
        mise = int(mise)
        assert (mise >= 0) and (mise <= cash)
    except AssertionError:
        print("Hum la mise me semble incorrecte monsieur, v'pouvez préciser?")
        continue
    try:
        play = input("Sur quelle nombre voulez-vous misez? (de 0 a 49)\n") 
        play = int(play)
        assert (play >= 0) and (play <= 49)
    except AssertionError:
        print("Monsieur, la case ", play, " n'existe pas...")
        continue
    roulette = randrange(50)
    print("La bille tombe sur le ......... ..\n......\n.. ... ...\n", roulette)
    if (roulette == play):
        print("WoooooowwwwwwwwwWWW !!! Gagné !!")
        gain = mise * 3
    elif (roulette % 2 == play % 2):
        print("Presque... meme couleur c'est pas mal :)")
        gain = ceil(mise * 1.5)
    else:
        print("Oups... perdu :/")
        gain = 0
    print("Vos gains sur ce coup: ",  gain - mise, "$")
    cash += gain - mise
if cash <= 0:
    print("Merci d'etre venue. A+")
else:
    print("A bientot !")
