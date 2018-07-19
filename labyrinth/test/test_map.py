# -*-coding:Utf-8 -*

import unittest
import pickle
from src.Map import Map
from src.Robot import Robot

class       MapTest(unittest.TestCase):

    def     setUp(self):
        self.map = Map()
        self.robot = Robot(self.map)

    def     test_generate_from_file(self):
        self.map.generate_from_file("../test/testmap.txt")
        str = self.map.__str__()
        with open("test/map_validation_data", "rb") as file:
            my_unpickler = pickle.Unpickler(file)
            valid_data = my_unpickler.load()
        self.assertEqual(str, valid_data)

    def     test_get_case_1(self):
        self.map.generate_from_file("../test/testmap.txt")
        ret = self.map.get_case(0, 0)
        self.assertEqual(ret, 'O')

    def     test_get_case_2(self):
        self.map.generate_from_file("../test/testmap.txt")
        ret = self.map.get_case(1, 1)
        self.assertEqual(ret, ' ')

