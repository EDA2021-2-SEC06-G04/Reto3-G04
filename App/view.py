"""
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
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
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
        print('El total de avistamientos es: ' + str(lt.size(catalog['encuentros'])))
        print('Los 5 primeros avistamientos cargados son:')
        i = 1
        while i <= 5:
            print(lt.getElement(catalog['encuentros'],i))
            i += 1
        print('Los 5 ultimos avistamientos cargados son:')
        i = 0
        while i <= 4:
            print(lt.getElement(catalog['encuentros'],lt.size(catalog['encuentros']) - i))
            i += 1
    
    elif int(inputs[0]) == 3:
        ciudad = input("Ingrese una ciudad: ")
        print('\nHay ' + str(mp.size(catalog['ciudad'])) + ' ciudades donde se reportaron avistamientos.\n')
        ciudadmayor = controller.ciudadmayor(catalog)
        encuentrosciudadmayor = om.size(me.getValue(mp.get(catalog['ciudad'],ciudadmayor)))
        print('La ciudad con mas avistamientos fue ' + ciudadmayor + ' con ' + str(encuentrosciudadmayor) + ' avistamientos.\n')
        avistamientos = me.getValue(mp.get(catalog['ciudad'],ciudad))
        print('Los primeros 3 avistamientos en la ciudad de ' + ciudad + ' son:\n')
        i = 0
        while i <= 2:
            print('Datetime: ' + om.get(avistamientos,(om.select(avistamientos,i)))['value']['datetime'] + '    Ciudad: ' + om.get(avistamientos,(om.select(avistamientos,i)))['value']['city'] + '    País: ' + om.get(avistamientos,(om.select(avistamientos,i)))['value']['country'] + '     Forma: ' + om.get(avistamientos,(om.select(avistamientos,i)))['value']['shape'] + '    Duración: ' + om.get(avistamientos,(om.select(avistamientos,i)))['value']['duration (seconds)'] + '\n\n')
            i += 1
        print('Los últimos 3 avistamientos registrados en la ciudad de ' + ciudad + ' son:\n')
        i = 3
        while i >= 1:
            print('Datetime: ' + om.get(avistamientos,(om.select(avistamientos,om.size(avistamientos) - i)))['value']['datetime'] + '    Ciudad: ' + om.get(avistamientos,(om.select(avistamientos,om.size(avistamientos) - i)))['value']['city'] + '    País: ' + om.get(avistamientos,(om.select(avistamientos,om.size(avistamientos) - i)))['value']['country'] + '     Forma: ' + om.get(avistamientos,(om.select(avistamientos,om.size(avistamientos) - i)))['value']['shape'] + '    Duración: ' + om.get(avistamientos,(om.select(avistamientos,om.size(avistamientos) - i)))['value']['duration (seconds)'] + '\n\n')
            i -= 1

    elif int(inputs[0]) == 4:
        lim_inferior = input('Ingrese el limite inferior en segundos: ')
        lim_superior = input('Ingrese el limite superior en segundos: ')
        mayorduracion = om.maxKey(catalog['duracion'])
        print('Los avistamientos mas largos fueron de ' + str(mayorduracion) + ' segundos, y fueron ' + str(om.size(me.getValue(om.get(catalog['duracion'],mayorduracion)))) + ' en total.')
        avistamientos = controller.rangosegundos(catalog,lim_inferior,lim_superior)
        print('Hay ' + str(lt.size(avistamientos)) + ' avistamientos en el rango de tiempo.')
        print('Los primeros 3 avistamientos en el rango son:\n')
        i = 1
        #print(avistamientos)
        while i <= 3:
            print('Datetime: ' + lt.getElement(avistamientos,i)['datetime'] + '    Ciudad: ' + lt.getElement(avistamientos,i)['city'] + '    País: ' + lt.getElement(avistamientos,i)['country'] + '     Forma: ' + lt.getElement(avistamientos,i)['shape'] + '    Duración: ' + lt.getElement(avistamientos,i)['duration (seconds)'] + '\n\n')
            i += 1
        print('Los últimos 3 avistamientos en el rango son:\n')
        i = 2
        while i >= 0:
            print('Datetime: ' + lt.getElement(avistamientos,lt.size(avistamientos) - i)['datetime'] + '    Ciudad: ' + lt.getElement(avistamientos,lt.size(avistamientos) - i)['city'] + '    País: ' + lt.getElement(avistamientos,lt.size(avistamientos) - i)['country'] + '     Forma: ' + lt.getElement(avistamientos,lt.size(avistamientos) - i)['shape'] + '    Duración: ' + lt.getElement(avistamientos,lt.size(avistamientos) - i)['duration (seconds)'] + '\n\n')
            i -= 1
       
    else:
        sys.exit(0)
sys.exit(0)
