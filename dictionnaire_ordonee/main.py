#!/usr/local/bin/python3.6
# -*-coding:Utf-8 -*

from ordered_dict import OrderedDictionary

fruits = OrderedDictionary()
print(fruits)

fruits["pomme"] = 52
fruits["poire"] = 34
fruits["prune"] = 128
fruits["melon"] = 15
print(fruits)

fruits.sort()
print(fruits)

legumes = OrderedDictionary(carotte = 26, haricot = 48)
print("4: ", legumes)

print(len(legumes))

legumes.reverse()
fruits = fruits + legumes
print("6: ", fruits)
fruits + 9

del fruits['haricot']
print("7: ", fruits)
print('haricot' in fruits)
print(legumes['haricot'])

for cle in legumes:
    print(cle)

print(legumes.keys())
print(legumes.values())
for nom, qtt in legumes.items():
    print("{0} ({1})".format(nom, qtt))
for key in legumes.keys():
    print("legumes {0} -> {1}".format(key, legumes[key]))

key = legumes.keys()
key[0] = "plop"
print(legumes)

