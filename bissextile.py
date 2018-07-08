#!/usr/local/bin/python3.6
# -*-coding:Utf-8 -*

while 1:
    try:
        year = input("Saisissez un année : ")
        if year == "exit":
            break
        year = int(year)
        assert year > 0
    except ValueError as error_return:
        print("There is an error :/ ", error_return)
        continue
    except AssertionError:
        print("Common... negative year really?")
        continue
    except KeyboardInterrupt:
        break
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(year, "est une année bissextile")
    else:
        print(year, "n'est pas une année bissextile")
