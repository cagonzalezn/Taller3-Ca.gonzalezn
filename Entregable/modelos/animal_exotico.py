from .animal import Animal

class AnimalExotico(Animal):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad)
        self.__pais_origen = pais_origen
        self.__impuestos = impuestos

    def calcular_flete(self):
        return self.__impuestos * self._peso       