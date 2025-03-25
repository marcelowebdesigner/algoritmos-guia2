# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 08:40:49 2025

@author: marce
"""

class Persona:
    def __init__(self, dni, nombre):
        self._dni = int(dni)
        self._nom = nombre.strip()

    def getDNI(self):
        return self._dni

    def getNombre(self):
        return self._nom

    def __lt__(self, other):
        return self._dni < other._dni

    def __le__(self, other):
        return self._dni <= other._dni

    def __gt__(self, other):
        return self._dni > other._dni

    def __ge__(self, other):
        return self._dni >= other._dni

    def __eq__(self, other):
        return self._dni == other._dni

    def __ne__(self, other):
        return self._dni != other._dni

    def __str__(self):
        return f"{self._dni:8} | {self._nom}"


class Cliente(Persona):
    def __init__(self, dni, nombre, promotor, seguro):
        super().__init__(dni, nombre)
        self._promotor = promotor
        self._seguros = [seguro.strip()]

    def addTipoSeguro(self, seguro):
        self._seguros.append(seguro.strip())

    def getSeguros(self):
        return self._seguros

    def getPromotor(self):
        return self._promotor


class Promotor(Persona):
    def __init__(self, dni, nombre):
        super().__init__(dni, nombre)
        self._clientes = []

    def addCliente(self, cliente):
        self._clientes.append(cliente)

    def getCntClientes(self):
        return len(self._clientes)

    def getClientes(self):
        return self._clientes

    def __str__(self):
        return f"Promotor: {self.getNombre()}"

    def ordenarClientes(self):
        self._ordenar_quickSort(self._clientes, 0, len(self._clientes) - 1)

    def _ordenar_quickSort(self, lista, inicio, fin):
        if inicio < fin:
            pi = self._partition(lista, inicio, fin)
            self._ordenar_quickSort(lista, inicio, pi - 1)
            self._ordenar_quickSort(lista, pi + 1, fin)

    def _partition(self, lista, inicio, fin):
        pivot = lista[fin]
        i = inicio - 1
        for j in range(inicio, fin):
            if lista[j] < pivot:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
        return i + 1

    def buscarCliente(self, dni):
        izquierda, derecha = 0, len(self._clientes) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            if self._clientes[medio].getDNI() == dni:
                return self._clientes[medio]
            elif self._clientes[medio].getDNI() < dni:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return None


def main():
    prom = Promotor(24317128, "Diego de la Vega")

    with open("clientes.txt", "r", encoding="utf-8") as file:
        for line in file:
            datos = line.strip().split(";")
            if len(datos) >= 3:
                dni = datos[0].strip()
                nombre = datos[1].strip()
                seguros = [s.strip() for s in datos[2].split("|")]

                cliente_obj = Cliente(dni, nombre, prom, seguros[0])
                for seguro in seguros[1:]:
                    cliente_obj.addTipoSeguro(seguro)

                prom.addCliente(cliente_obj)

    prom.ordenarClientes()

    print(f"{prom}")
    print("Listado de clientes:")
    for cli in prom.getClientes():
        print(f"{cli.getDNI()} - {cli.getNombre()}")

    while True:
        dni_ingresado = int(input("\nIngrese un DNI para buscar (0 o negativo para salir): "))
        if dni_ingresado <= 0:
            break

        cliente_encontrado = prom.buscarCliente(dni_ingresado)
        if cliente_encontrado:
            print(f"\nCliente encontrado:\n{cliente_encontrado}")
            print("Seguros contratados:")
            for seguro in cliente_encontrado.getSeguros():
                print(f"\t- {seguro}")
        else:
            print("Cliente no encontrado.")

if __name__ == "__main__":
    main()
