# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 08:34:52 2025

@author: marce
"""

class Persona:
    def __init__(self, dni, nombre):
        self._dni = dni
        self._nom = nombre
    
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
        return f"{self._dni:>8} | {self._nom}"

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
        return self._nom

class Cliente(Persona):
    def __init__(self, dni, nombre, promotor, tipo_seguro):
        super().__init__(dni, nombre)
        self._promotor = promotor
        self._seguros = [tipo_seguro]
    
    def getPromotor(self):
        return self._promotor
    
    def addTipoSeguro(self, tipo_seguro):
        self._seguros.append(tipo_seguro)
    
    def getSeguros(self):
        return self._seguros

def main():
    # Creamos el promotor
    prom = Promotor(24317128, "Diego de la Vega")
    
    # Creamos un cliente, vinculándolo al promotor
    cli01 = Cliente(11765989, "Carlos Avellaneda", prom, "Seguro de Vida")
    prom.addCliente(cli01)
    
    # Creamos el segundo cliente
    cli02 = Cliente(23547896, "Analía Mendizábal", prom, "Seguro Automotor (NPE 321)")
    cli02.addTipoSeguro("Seguro de Vida")
    prom.addCliente(cli02)
    
    # Creamos el tercer cliente
    cli03 = Cliente(19874563, "Joaquín Mendez", prom, "Seguro Automotor (AB 321 ZF)")
    prom.addCliente(cli03)
    
    # Mostramos los datos del promotor
    print(f"{prom}")
    
    # Y el listado de sus clientes
    print("Listado de clientes:")
    for cli in prom.getClientes():
        print(f"{cli}")
        print("Productos contratados:")
        for s in cli.getSeguros():
            print(f"\t {s}")

if __name__ == "__main__":
    main()
