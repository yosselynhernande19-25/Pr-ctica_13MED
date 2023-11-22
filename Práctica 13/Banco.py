from queue import Queue

class Banco:
    def __init__(self):
        self.cola_clientes = Queue()

    def llegada_cliente(self, nombre_cliente):
        self.cola_clientes.put(nombre_cliente)
        print(f"{nombre_cliente} ha llegado al banco. Número de clientes en espera: {self.cola_clientes.qsize()}")

    def atender_clientes(self):
        while not self.cola_clientes.empty():
            cliente_actual = self.cola_clientes.get()
            print(f"Atendiendo a {cliente_actual}. Número de clientes en espera: {self.cola_clientes.qsize()}")

if __name__ == "__main__":
    banco = Banco()

    # Simulación de llegada de clientes
    banco.llegada_cliente("Cliente1")
    banco.llegada_cliente("Cliente2")
    banco.llegada_cliente("Cliente3")

    # Simulación de atención de clientes
    banco.atender_clientes()
