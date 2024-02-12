import os
os.system('cls' if os.name == 'nt' else 'clear')
from queue import Queue

def boarding_process():
    boarding_queue = Queue()

    while True:
        try:
            passenger_type = int(input("¿Es VIP o turista? (Ingrese 1 para VIP, 2 para turista): "))
            if passenger_type not in [1, 2]:
                raise ValueError("Por favor, ingrese 1 o 2.")
        except ValueError as e:
            print(e)
            continue

        if passenger_type == 1:
            all_passengers = int(input("¿Son todos los pasajeros VIP? (Ingrese 1 para sí, 2 para no): "))
            if all_passengers == 1:
                boarding_queue.put("VIP")
            elif all_passengers == 2:
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
            check_in = int(input("¿Vas a hacer check-in? (Ingrese 1 para sí, 2 para no): "))
            if check_in == 1:
                print("Realizando check-in...")
            elif check_in == 2:
                print("Sin check-in.")
            else:
                print("Opción no válida. Por favor, ingrese 1 o 2.")

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

        another_passenger = int(input("¿Desea agregar otro pasajero? (Ingrese 1 para sí, 2 para no): "))
        if another_passenger != 1:
            break

    print("\nLista de pasajeros en la cola de embarque:")
    while not boarding_queue.empty():
        print(boarding_queue.get())

if __name__ == "__main__":
    boarding_process()
