import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modelos.guarderia import Guarderia
from modelos.boa_Constrictor import boaConstrictor

class TestGuarderia(unittest.TestCase):
    def setUp(self):
        self.guarderia = Guarderia()

    def test_alimentar_boa_sin_exceder_limite(self):
        boa = self.guarderia.boas[0]
        for _ in range(10):
            resultado = self.guarderia.alimentar_boa(boa)
            self.assertEqual(resultado, "Éxito")
        self.assertEqual(boa.obtener_ratones_comidos(), 10)

    def test_alimentar_boa_excede_limite(self):
        boa = self.guarderia.boas[0]
        for _ in range(10):
            self.guarderia.alimentar_boa(boa)

        # Alimentar una vez más para exceder el límite
        resultado = self.guarderia.alimentar_boa(boa)
        self.assertEqual(resultado, "La boa está llena")

    def test_alimentar_boa_invalida(self):
        resultado = self.guarderia.alimentar_boa(None)
        self.assertEqual(resultado, "Esta Boa no existe!")

if __name__ == "__main__":
    unittest.main()
