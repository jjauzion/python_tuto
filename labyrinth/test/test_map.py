# -*-coding:Utf-8 -*

import unittest
import pickle
from src.Map import Map
from src.Robot import Robot

class       MapTest(unittest.TestCase):

    def     setUp(self):
        self.map = Map()

    def     test_generate_from_file(self):
        self.map.generate_from_file("../test/testmap.txt")
        self.robot = Robot(self.map, 1)
        str = self.map.print()
        str = str.replace("X", " ")
        with open("test/map_validation_data", "rb") as file:
            my_unpickler = pickle.Unpickler(file)
            valid_data = my_unpickler.load()
        valid_data = valid_data.replace("X", " ")
        self.assertEqual(str, valid_data)

    def     test_get_case_1(self):
        self.map.generate_from_file("../test/testmap.txt")
        self.robot = Robot(self.map, 1)
        ret = self.map.get_case({'x': 0, 'y': 0})
        self.assertEqual(ret, 'O')

    def     test_get_case_2(self):
        self.map.generate_from_file("../test/testmap.txt")
        self.robot = Robot(self.map, 1)
        ret = self.map.get_case({'x': 1, 'y': 1})
        self.assertEqual(ret, ' ')

