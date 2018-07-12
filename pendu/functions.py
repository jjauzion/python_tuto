def         get_letter():
    while (1):
        letter = input("Quelle lettre veux-tu essayer ? (Ou tapes le mot complet si tu as deviner)\n");
        letter = str(letter).lower()
        if (letter.isalpha() == True):
            return (letter)
        else:
            print("La saisie contient des charactères invalides")

def gen_visible_word(hidden_letter, word):
    visible_word = word
    i = 0
    while i < len(hidden_letter):
        visible_word = visible_word.replace(hidden_letter[i], '*')
        i += 1
    return visible_word

def update_hidden_letter(hidden_letter, letter):
    i = 0
    while i < len(letter):
        hidden_letter = hidden_letter.replace(letter[i], '')
        i += 1
    return hidden_letter

import pickle

def save_score(score, score_file):
    name = input("Saissez votre pseudo pour sauvegarder votre score\n")
    try:
        with open(score_file, "rb") as fd:
            depickler = pickle.Unpickler(fd)
            score_dic = depickler.load()
            if name not in score_dic.keys():
                score_dic[name] = 0
            else:
                score_dic[name] += score
            #score += 0 if score_dic.get(name) == None else score_dic.get(name)
    except FileNotFoundError:
        score_dic = {name: score}
    with open(score_file, "wb") as fd:
        my_pickle = pickle.Pickler(fd)
        my_pickle.dump(score_dic)
        print("Votre score a été ajouté!")
        print("Pseudo : {} ; score : {}".format(name, score_dic[name]))
