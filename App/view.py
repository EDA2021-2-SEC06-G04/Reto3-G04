﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Crear el catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Contar los avistamientos de una ciudad")
    print("4- Contar los avistamientos por duración")
    print("5- Contar los avistamientos por hora/minutos del día")
    print("6- Contar los avistamientos en un rango de fechas")
    print("7- Contar los avistamientos de una zona geográfica")
    print("0- Salir")


file = 'UFOS-utf8-small.csv'
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # catalog es el controlador que se usará de acá en adelante
        catalog = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de UFOS ....")
        controller.loadData(catalog, file)
        #print('Crimenes cargados: ' + str(controller.crimesSize(catalog)))
        #print('Altura del arbol: ' + str(controller.indexHeight(catalog)))
        #print('Elementos en el arbol: ' + str(controller.indexSize(catalog)))
        #print('Menor Llave: ' + str(controller.minKey(catalog)))
        #print('Mayor Llave: ' + str(controller.maxKey(catalog)))
    
    elif int(inputs[0]) == 3:
        ciudad = input("Ingrese una ciudad: ")
        print('Altura del arbol: ' + str(controller.ciudadHeight(catalog,ciudad)))
        print('Elementos en el arbol: ' + str(controller.ciudadSize(catalog,ciudad)))

    else:
        sys.exit(0)
sys.exit(0)
