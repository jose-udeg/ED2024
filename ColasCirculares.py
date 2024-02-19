import os
os.system('cls' if os.name == 'nt' else 'clear')

# Definición de la clase Nodo, que representa los nodos individuales de la cola
class Nodo:
    def __init__(self, data):
        #Inicializa un nuevo nodo con el dato proporcionado.

            #data: El dato almacenado en el nodo.
        self.data = data
        self.siguiente = None  # Puntero al siguiente nodo
        self.anterior = None   # Puntero al nodo anterior

# Definición de la clase ColaDobleCircular, que implementa la cola doble circular
class ColaDobleCircular:
    def __init__(self):
        #Inicializa una nueva cola doble circular vacía.
        self.cabeza = None  # Puntero a la cabeza de la cola
        self.cola = None    # Puntero a la cola de la cola

    def insertar_frente(self, data):
        """
        Inserta un elemento al frente de la cola.

        Args:
            data: El dato a insertar.
        """
        nuevo_nodo = Nodo(data)
        if not self.cabeza:  # Si la cola está vacía
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.cola.siguiente = self.cabeza  # Conecta el último nodo con el primero
        self.cabeza.anterior = self.cola    # Conecta el primer nodo con el último
        print("Insertado", data, "al frente.")
        self.mostrar_movimientos()

    def insertar_final(self, data):
        """
        Inserta un elemento al final de la cola.

        Args:
            data: El dato a insertar.
        """
        nuevo_nodo = Nodo(data)
        if not self.cabeza:  # Si la cola está vacía
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.cola.siguiente = self.cabeza  # Conecta el último nodo con el primero
        self.cabeza.anterior = self.cola    # Conecta el primer nodo con el último
        print("Insertado", data, "al final.")
        self.mostrar_movimientos()

    def eliminar_frente(self):
        #Elimina el elemento al frente de la cola.
        if not self.cabeza:
            print("La cola está vacía. No hay nada que eliminar.")
            return
        data = self.cabeza.data
        if self.cabeza == self.cola:  # Si solo hay un elemento
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = self.cola
            self.cola.siguiente = self.cabeza
        print("Eliminado", data, "del frente.")
        self.mostrar_movimientos()

    def eliminar_final(self):
        #Elimina el elemento al final de la cola.
        if not self.cabeza:
            print("La cola está vacía. No hay nada que eliminar.")
            return
        data = self.cola.data
        if self.cabeza == self.cola:  # Si solo hay un elemento
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = self.cabeza
            self.cabeza.anterior = self.cola
        print("Eliminado", data, "del final.")
        self.mostrar_movimientos()

    def mostrar_movimientos(self):
        #Muestra los elementos de la cola.
        print("Cola Actual: ", end="")
        actual = self.cabeza
        while actual:
            print(actual.data, end=" ")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print()

# Ejemplo de uso
cola = ColaDobleCircular()
cola.insertar_frente(1)
cola.insertar_final(2)
cola.insertar_frente(3)
cola.eliminar_frente()
cola.eliminar_final()
