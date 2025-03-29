from .animal_exotico import AnimalExotico

class Huron(AnimalExotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
    
    def hacer_sonido(self):
        return "¡Eek Eek!"
    