from .animal_exotico import AnimalExotico

class boaConstrictor(AnimalExotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__ratones_comidos = 0 
    
    def hacer_sonido(self):
        return "¡Tsss, tss!"
    
    def agregar_raton(self):
        self.__ratones_comidos += 1 

    def obtener_ratones_comidos(self):
        #si los ratones comidos son mas de 10
        #lanzará un ValueError con el mensaje “Demasiados Ratones!”.
        if self.__ratones_comidos > 10:
            raise ValueError("Demasiados Ratones!")
        #si no, retornará la cantidad de ratones comidos.
        return self.__ratones_comidos 
 