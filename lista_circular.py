class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza

    def imprimir(self):
        if self.esta_vacia():
            print("La lista esta vacia.")
            return

        actual = self.cabeza
        print("Lista de Turnos:")
        while True:
            print(f"- {actual.dato}")
            actual = actual.siguiente
            if actual == self.cabeza:
                break

    def buscar(self, dato):
        if self.esta_vacia():
            return False
        
        actual = self.cabeza
        while True:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False

    def eliminar(self, dato):
        if self.esta_vacia():
            return

        actual = self.cabeza
        anterior = None

        while True:
            if actual.dato == dato:
                break
            anterior = actual
            actual = actual.siguiente
            if actual == self.cabeza:
                print(f"El turno/elemento '{dato}' no se encontro en la lista.")
                return

        if actual == self.cabeza and actual.siguiente == self.cabeza:
            self.cabeza = None
            return

        if actual == self.cabeza:
            ultimo = self.cabeza
            while ultimo.siguiente != self.cabeza:
                ultimo = ultimo.siguiente
            self.cabeza = self.cabeza.siguiente
            ultimo.siguiente = self.cabeza
        else:
            anterior.siguiente = actual.siguiente


if __name__ == "__main__":
    turnos = ListaCircular()

    print("=== REGISTRO DE TURNOS DE ATENCION ===")
    turnos.agregar("Turno 1: Juan Perez")
    turnos.agregar("Turno 2: Maria Lopez")
    turnos.agregar("Turno 3: Carlos Gomez")
    turnos.agregar("Turno 4: Ana Martinez")

    turnos.imprimir()

    print("\n--- Busqueda de Turno ---")
    busqueda = "Turno 2: Maria Lopez"
    if turnos.buscar(busqueda):
        print(f"Encontrado: {busqueda}")
    else:
        print(f"No encontrado: {busqueda}")

    print("\n--- Atendiendo / Eliminando Turno ---")
    print("Atendiendo a Juan Perez (Turno 1)...")
    turnos.eliminar("Turno 1: Juan Perez")

    print("\nLista actualizada despues de atender:")
    turnos.imprimir()
