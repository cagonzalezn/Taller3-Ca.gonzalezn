import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from modelos.huron import Huron
from modelos.boa_Constrictor import boaConstrictor

class TestHuron(unittest.TestCase):
    def test_hacer_sonido_huron(self):
        huron = Huron("Hurón", 5.0, 2, "Argentina", 8.0)
        
        self.assertEqual(huron.hacer_sonido(), "¡Eek Eek!")
    
    def test_hacer_sonido_boa(self):

        boa = boaConstrictor("Boa", 20.0, 5, "Brasil", 12.0)
        
        self.assertEqual(boa.hacer_sonido(), "¡Tsss, tss!")

if __name__ == "__main__":
    unittest.main()