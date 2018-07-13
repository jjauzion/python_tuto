#!/usr/local/bin/python3.6
# -*-coding:Utf-8 -*

from src import *
import src.param as param

print("/----------------------------------------------------------\\")
print("|  _  .-')              .-. .-')                           |")
print("| ( \( -O )             \  ( OO )                          |")
print("|  ,------.  .-'),-----. ;-----.\  .-'),-----.    .-----.  |")
print("|  |   /`. '( OO'  .-.  '| .-.  | ( OO'  .-.  '  '  .--./  |")
print("|  |  /  | |/   |  | |  || '-' /_)/   |  | |  |  |  |('-.  |")
print("|  |  |_.' |\_) |  |\|  || .-. `. \_) |  |\|  | /_) |OO  ) |")
print("|  |  .  '.'  \ |  | |  || |  \  |  \ |  | |  | ||  |`-'|  |")
print("|  |  |\  \    `'  '-'  '| '--'  /   `'  '-'  '(_'  '--'\  |")
print("|  `--' '--'     `-----' `------'      `-----'    `-----'  |")
print("\----------------------------------------------------------/")

my_map = Map.Map()
print(my_map)
my_map.generate_from_file("facile.txt", param)
print(my_map)

robot = Robot.Robot(my_map)
robot.move("N45", param)

my_map.generate_from_file("empty.txt", param)
