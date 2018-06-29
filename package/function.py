#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

"""module de table de multiplication"""

def table_par(nb, max=10):
    """Table de multiplication

     (max >= 0"""

    i = 1
    while i <= max:
        print(i, "*", nb, "=", i * nb)
        i += 1

# exe fct table_par si le module est executer en main
if __name__ == "__main__":
    table_par(9)
