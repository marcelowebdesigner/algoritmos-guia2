# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 08:38:40 2025

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
    
    def __str__(self):
        return f"{self._dni:8} | {self._nom}"

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

class Cliente(Persona):
    def __init__(self, dni, nombre, promotor, tipoSeguro):
        super().__init__(dni, nombre)
        self._promotor = promotor
        self._seguros = [tipoSeguro]
    
    def addTipoSeguro(self, seguro):
        self._seguros.append(seguro)
    
    def getSeguros(self):
        return self._seguros
    
    def getPromotor(self):
        return self._promotor

def main():
    # Creamos el promotor con datos fijos
    prom = Promotor(24317128, "Diego de la Vega")
    
    # Leemos el archivo con los clientes
    with open('clientes.txt', 'r', encoding='utf8') as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")
            if len(datos) == 3:
                dni = int(datos[0].strip())
                nombre = datos[1].strip()
                seguros = [s.strip() for s in datos[2].split("|")]
                
                # Creamos el cliente con el primer seguro
                cli = Cliente(dni, nombre, prom, seguros[0])
                
                # Agregamos los seguros adicionales si los hay
                for seguro in seguros[1:]:
                    cli.addTipoSeguro(seguro)
                
                # Agregamos el cliente al promotor
                prom.addCliente(cli)
    
    # Mostramos los datos del promotor
    print(f"{prom}")
    print("Listado de clientes:")
    for cli in prom.getClientes():
        print(f"{cli}")
        print("Productos contratados:")
        for s in cli.getSeguros():
            print(f"\t{s}")

if __name__ == '__main__':
    main()
