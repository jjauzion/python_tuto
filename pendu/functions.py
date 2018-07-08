def get_letter():
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
