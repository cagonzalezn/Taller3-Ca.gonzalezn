import sys
import os
import unittest
from modelos.boa_Constrictor import boaConstrictor

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestBoaConstrictor(unittest.TestCase):

    def test_agregar_ratones(self):
        #Creo una instancia de boaConstrictor
        boa = boaConstrictor("Boa", 20.0, 5, "Brasil", 12.0)

        # Inicialmente la boa no ha comido ratones
        self.assertEqual(boa.obtener_ratones_comidos(), 0)

        # Alimento la boa con 3 ratones
        boa.agregar_raton()
        boa.agregar_raton()
        boa.agregar_raton()

        # Verifico que ha comido 3 ratones
        self.assertEqual(boa.obtener_ratones_comidos(), 3)

    def test_limite_ratones(self):
        boa = boaConstrictor("Boa", 20.0, 5, "Brasil", 12.0)
        for _ in range(10):
            boa.agregar_raton()

        # Se puede alimentar hasta 10 ratones sin problemas
        self.assertEqual(boa.obtener_ratones_comidos(), 10)

        # Con otro ratón, debería lanzar un ValueError
        boa.agregar_raton()

        # Se lanza un ValueError si se intenta agregar más de 10 ratones
        with self.assertRaises(ValueError) as context:
            boa.obtener_ratones_comidos()
        self.assertEqual(str(context.exception), "Demasiados Ratones!")

if __name__ == "__main__":
    unittest.main()
