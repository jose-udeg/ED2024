import os
os.system('cls' if os.name == 'nt' else 'clear')
from queue import Queue

def boarding_process():
    """
    Simula el proceso de embarque en un aeropuerto.

    Solicita al usuario que ingrese el tipo de pasajero (VIP o turista), la cantidad de pasajeros
    y si desean hacer el check-in. Los pasajeros se agregan a una cola de embarque y al final se
    muestra la lista combinada de pasajeros en la cola.

    Argumentos:
    None

    Retorna:
    None
    """
    # Crear una cola de embarque vacía
    boarding_queue = Queue()

    # Bucle principal para solicitar información de los pasajeros
    while True:
        try:
            # Preguntar si el pasajero es VIP o turista
            passenger_type = int(input("¿Es VIP o turista? (Ingrese 1 para VIP, 2 para turista): "))
            if passenger_type not in [1, 2]:
                raise ValueError("Por favor, ingrese 1 o 2.")
        except ValueError as e:
            print(e)
            continue

        if passenger_type == 1:
            # Si el pasajero es VIP
            all_passengers = int(input("¿Son todos los pasajeros VIP? (Ingrese 1 para sí, 2 para no): "))
            if all_passengers == 1:
                # Si todos son VIP, agregarlos a la cola de embarque
                boarding_queue.put("VIP")
            elif all_passengers == 2:
                # Si no todos son VIP, solicitar la cantidad y agregarlos a la cola de embarque
                num_passengers = 0
                while True:
                    try:
                        num_passengers = int(input("Ingrese la cantidad de pasajeros VIP: "))
                        break
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                        continue
                for _ in range(num_passengers):
                    boarding_queue.put("VIP")
            else:
                print("Opción no válida. Por favor, ingrese 1 o 2.")
        elif passenger_type == 2:
            # Si el pasajero es turista
            check_in = int(input("¿Vas a hacer check-in? (Ingrese 1 para sí, 2 para no): "))
            if check_in == 1:
                print("Realizando check-in...")
            elif check_in == 2:
                print("Sin check-in.")
            else:
                print("Opción no válida. Por favor, ingrese 1 o 2.")

            # Solicitar la cantidad de pasajeros turistas y agregarlos a la cola de embarque
            num_passengers = 0
            while True:
                try:
                    num_passengers = int(input("Ingrese la cantidad de pasajeros turistas: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue

            for _ in range(num_passengers):
                boarding_queue.put("Turista")

        # Preguntar si se desea agregar otro pasajero
        another_passenger = int(input("¿Desea agregar otro pasajero? (
