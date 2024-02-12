import os
os.system('cls' if os.name == 'nt' else 'clear')
import time
import random
from queue import Queue

class Pasajero:
    def __init__(self, nombre, vip=False):
        self.nombre = nombre
        self.vip = vip

def proceso_check_in(cola_no_vip):
    print("Realizando proceso de check-in...")
    while not cola_no_vip.empty():
        pasajero = cola_no_vip.get()
        print(f"Check-in completado para {pasajero.nombre}")
        time.sleep(random.uniform(0.5, 1))  # Simulación de tiempo de check-in

def proceso_inspeccion(cola_no_vip):
    print("\nRealizando proceso de inspección...")
    while not cola_no_vip.empty():
        pasajero = cola_no_vip.get()
        print(f"Inspección completada para {pasajero.nombre}")
        time.sleep(random.uniform(0.5, 1))  # Simulación de tiempo de inspección

def proceso_embarque(cola_vip, cola_no_vip):
    print("\nIniciando proceso de embarque...")
    print("\nEmbarcando pasajeros VIP:")
    while not cola_vip.empty():
        pasajero = cola_vip.get()
        print(f"Embarcando pasajero VIP: {pasajero.nombre}")
        time.sleep(random.uniform(0.5, 1))  # Simulación de tiempo de embarque

    print("\nEmbarcando pasajeros no VIP:")
    while not cola_no_vip.empty():
        pasajero = cola_no_vip.get()
        print(f"Embarcando pasajero no VIP: {pasajero.nombre}")
        time.sleep(random.uniform(0.5, 1))  # Simulación de tiempo de embarque

# Ejemplo de uso
cola_pasajeros = Queue()

# Crear pasajeros y añadirlos a la cola
for i in range(1, 50):
    vip = True if i % 5 == 0 else False  # Cada 5to pasajero es VIP
    cola_pasajeros.put(Pasajero(f"Pasajero {i}", vip))

# Separar pasajeros VIP de los no VIP
cola_vip = Queue()
cola_no_vip = Queue()

while not cola_pasajeros.empty():
    pasajero = cola_pasajeros.get()
    if pasajero.vip:
        cola_vip.put(pasajero)
    else:
        cola_no_vip.put(pasajero)

# Procesos
proceso_check_in(cola_no_vip)
proceso_inspeccion(cola_no_vip)
proceso_inspeccion(cola_vip)
proceso_embarque(cola_vip, cola_no_vip)
