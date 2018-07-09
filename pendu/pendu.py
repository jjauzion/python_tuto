#!/usr/local/bin/python3.6
# -*-coding:Utf-8 -*

from random import choice
import param
from functions import *

word = choice(param.word_list)
hidden_letter = "abcdefghifklmnopqrstuvwxyz"
visible_word = gen_visible_word(hidden_letter, word)

count = 8;
while ((count > 0) & (visible_word.count("*") > 0)):
    print("\n------------------------------")
    print("Le mot du pendu :", visible_word)
    print("Il te reste {} chances".format(count))
    letter = get_letter()
    if len(letter) > 1:
        score = count
        count = 0
    hidden_letter = update_hidden_letter(hidden_letter, letter)
    visible_word = gen_visible_word(hidden_letter, word)
    count -= 1
if visible_word.count("*") <= 0:
    print("\n *** Bien joué! ***")
    save_score(score, param.score_file)
else:
    print("\n Perdu! Le mot était : ", word)
