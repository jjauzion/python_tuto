#!/usr/local/bin/python3.6
# -*-coding:Utf-8 -*

import random
import unittest

class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def setUp(self):
        """Initialisation des tests unitaire"""
        self.liste = list(range(10))

    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        elt = random.choice(self.liste)
        # Vérifie que 'elt' est dans 'liste'
        self.assertIn(elt, self.liste)

    def test_shuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'."""
        random.shuffle(self.liste)
        self.liste.sort()
        self.assertEqual(self.liste, list(range(10)))

    def test_sample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        extrait = random.sample(self.liste, 5)
        for element in extrait:
            self.assertIn(element, self.liste)
        #self.assertRaises(ValueError, random.sample, liste, 20)
        with self.assertRaises(ValueError):
            random.sample(self.liste, 20)
