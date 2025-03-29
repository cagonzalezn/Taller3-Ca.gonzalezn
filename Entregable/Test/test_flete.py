import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from modelos.animal_exotico import AnimalExotico

class TestAnimalExotico(unittest.TestCase):
    def test_calcular_flete_python(self):
        animal = AnimalExotico("Python", 15.5, 4, "Colombia", 10.0)
        self.assertEqual(animal.calcular_flete(), 155.0)

    def test_calcular_flete_huron(self):
        animal = AnimalExotico("Hurón", 5.0, 2, "Argentina", 8.0)
        self.assertEqual(animal.calcular_flete(), 40.0)

    def test_calcular_flete_boa(self):
        animal = AnimalExotico("Boa", 20.0, 5, "Brasil", 12.0)
        self.assertEqual(animal.calcular_flete(), 240.0)

if __name__ == "__main__":
    unittest.main()