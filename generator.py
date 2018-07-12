#!/usr/local/bin/python3.6
# -*-coding:Utf-8 -*

def interval(start, end):
    i = start
    while (i <= end):
        yield i
        i += 1

for nombre in interval(3, 10):
    print(nombre)
