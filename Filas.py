import os
os.system('cls' if os.name == 'nt' else 'clear')

fila = []

#añadir elementos a la fila
fila.append('cliente1')
fila.append('cliente2')
fila.append('cliente3')
fila.append('cliente4')

print("Los elementos de la fila son:", fila)

#atender cliente(elimiar elemento de la fila)
cliente_atendido = fila.pop(0)
print("Cliente atendido fue:", cliente_atendido)
print("Fila despues de atender a un cliente son:", fila)
