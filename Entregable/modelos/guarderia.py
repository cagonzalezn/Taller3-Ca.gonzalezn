from modelos.boa_Constrictor import boaConstrictor
from modelos.huron import Huron

class Guarderia:
    def __init__(self):
        self.boas = [
            boaConstrictor("Boa1", 20.0, 5, "Brasil", 12.0),
            boaConstrictor("Boa2", 22.0, 6, "Colombia", 10.0)
        ]
        self.hurones = [
            Huron("Huron1", 8.0, 3, "Argentina", 5.0),
            Huron("Huron2", 7.5, 2, "Chile", 4.5)
        ]

    def alimentar_boa(self, boa):
        if boa is None:
            return "Esta Boa no existe!"
        
        try:
            boa.agregar_raton()  # Intentamos alimentar la boa
            return "Éxito"
        except ValueError:
            return "La boa está llena"

# Prueba de la guardería
if __name__ == "__main__":
    guarderia = Guarderia()

    # Caso 1: Boa válida (debe mostrar "Éxito" varias veces)
    for _ in range(11):  
        print(guarderia.alimentar_boa(guarderia.boas[0]))

    # Caso 2: Boa llena (debe mostrar "La boa está llena")
    print(guarderia.alimentar_boa(guarderia.boas[0]))

    # Caso 3: Boa no válida (debe mostrar "Esta Boa no existe!")
    print(guarderia.alimentar_boa(None))
