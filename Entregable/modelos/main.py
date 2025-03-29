from boa_Constrictor import boaConstrictor
from huron import Huron

# Aquí creo una instancia de BoaConstrictor
boa = boaConstrictor(nombre="Python", peso=15.5, edad=4, pais_origen="Colombia", impuestos=10.0)

# Aquí creo una instancia de Huron
huron = Huron(nombre="Nucita", peso=2.3, edad=2, pais_origen="Australia", impuestos=5.0)

print(f"La boa hace: {boa.hacer_sonido()}")
#Imprime: La boa hace: ¡Tsss, tss!
print(f"El hurón hace: {huron.hacer_sonido()}") 
#Imprime: El hurón hace: ¡Eek Eek!

print(f"El costo de flete de la boa es: {boa.calcular_flete()}")
#Imprime: El costo de flete de la boa es: 155.0

print(f"El costo de flete del hurón es: {huron.calcular_flete()}")
#Imprime: El costo de flete del hurón es: 11.5

#Asigno kilos para cada animal
boa.comer(3)
huron.comer(1)

print(f"Kilos comidos por la boa: {boa.obtener_kilos_comidos()}")
#Kilos comidos por la boa: 3
print(f"Kilos comidos por el hurón: {huron.obtener_kilos_comidos()}")
#Kilos comidos por el hurón: 1

boa.agregar_raton()
boa.agregar_raton()

print(f"La boa ha comido {boa.obtener_ratones_comidos()} ratones.")
# Imprime: La boa ha comido 2 ratones.
