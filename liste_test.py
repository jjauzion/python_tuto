#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

def afficher_float(nb, precision):
    nb = str(nb)
    integer, rest = nb.split(".")
    print("int = {} ; rest = {}".format(integer, rest))
    return ",".join([integer, rest[:precision]])

def my_print(*param, sep=' ', end='\n'):
    '''
    output = str()
    for elm in param:
        output += str(elm)
        output += str(sep)
    output = output[:-1] + str(end)
    '''
    output = list()
    for elm in param:
        output.append(str(elm))
    output.append(str(end))
    print(sep.join(output))


#print(afficher_float(3., 5))
#my_print("test", 2, "my", "print", sep='_', end='|')
inventaire = [
        ("pomme", 22),
        ("melons", 4),
        ("poire", 18),
        ("fraise", 76),
        ("prunes", 51),
        ]
#inventaire.sort()
swap = [(qte, fruit) for fruit, qte in inventaire]
inventaire = [elm for elm in sorted(swap, reverse=True)]
print(*inventaire)

