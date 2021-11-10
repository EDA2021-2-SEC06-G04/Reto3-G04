"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp
from DISClib.Algorithms.Sorting import mergesort
import datetime
assert config

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los avistamientos
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    catalog = {'encuentros': None,
                'datetime': None,
                'ciudad': None,
                'duracion': None

                }

    catalog['encuentros'] = lt.newList('SINGLE_LINKED')
    catalog['ciudad'] = mp.newMap(maptype='PROBING')
    catalog['duracion'] = om.newMap(omaptype='RBT')

                                    
    return catalog

# Funciones para agregar informacion al catalogo

def addEncuentro(catalog, encuentro):
    """Agrega un reporte a la lista de reportes
    y actualiza los índices dal catálogo con el nuevo reporte
    """
    lt.addLast(catalog['encuentros'], encuentro)
    if not mp.contains(catalog['ciudad'],encuentro['city']):
        mp.put(catalog['ciudad'],encuentro['city'],om.newMap())
    #print(catalog['ciudad'])
    #print(encuentro['city'])
    om.put(me.getValue(mp.get(catalog['ciudad'],encuentro['city'])),encuentro['datetime'],encuentro)
    if not om.contains(catalog['duracion'],float(encuentro['duration (seconds)'])):
        #om.put(catalog['duracion'],float(encuentro['duration (seconds)']),lt.newList(datastructure='ARRAY_LIST',cmpfunction=cmppaisciudad))
        om.put(catalog['duracion'],float(encuentro['duration (seconds)']),om.newMap(omaptype='BRT',comparefunction=cmppaisciudad))
    if not om.contains(me.getValue(om.get(catalog['duracion'],float(encuentro['duration (seconds)']))),encuentro['country'] + '-' + encuentro['city']):
        #om.put(catalog['duracion'],float(encuentro['duration (seconds)']),lt.newList(datastructure='ARRAY_LIST',cmpfunction=cmppaisciudad))
        om.put(me.getValue(om.get(catalog['duracion'],float(encuentro['duration (seconds)']))), encuentro['country'] + '-' + encuentro['city'],lt.newList('ARRAY_LIST'))
    lt.addLast(me.getValue(om.get(me.getValue(om.get(catalog['duracion'],float(encuentro['duration (seconds)']))),encuentro['country'] + '-' + encuentro['city'])),encuentro)

    return catalog

# Funciones para creacion de datos

# Funciones de consulta
#Requerimiento 1
def ciudadmayor(catalog):
    mayor = None
    #print(mp.keySet(catalog['ciudad']))
    for ciudad in lt.iterator(mp.keySet(catalog['ciudad'])):
        if (mayor == None) or ((om.size(me.getValue(mp.get(catalog['ciudad'],ciudad)))) > (om.size(me.getValue(mp.get(catalog['ciudad'],mayor))))):
            mayor = ciudad
    return mayor

#Requerimiento 2
def rangosegundos(catalog,min,max):
    lista = lt.newList('ARRAY_LIST')
    i = min
    while i <= max:
        arbol = me.getValue(om.get(catalog['duracion'],i))
        llaveselementos = lt.iterator(om.keySet(arbol))
        for elemento in llaveselementos:
            #print(om.get(arbol,elemento))
            encuentros = lt.iterator(me.getValue(om.get(arbol,elemento)))
            for encuentro in encuentros:
                lt.addLast(lista,encuentro)
        i = om.ceiling(catalog['duracion'],i + 0.1)
    return lista

def ciudadHeight(catalog,ciudad):
    """
    Altura del arbol
    """
    return om.height(me.getValue(mp.get(catalog['ciudad'],ciudad)))


def ciudadSize(catalog,ciudad):
    """
    Numero de elementos en el indice
    """
    return om.size(me.getValue(mp.get(catalog['ciudad'],ciudad)))

# Funciones utilizadas para comparar elementos dentro de una lista

def comparedatetime(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def cmppaisciudad(encuentro1,encuentro2):
    """
    Compara dos combinaciones país-ciudad en orden alfabético
    """
    encuentro1 = encuentro1.split('-')
    encuentro2 = encuentro2.split('-')

    if (encuentro1[1] == encuentro2[1]):
        if (encuentro1[0] == encuentro2[0]):
            return 0
        if (encuentro1[0] > encuentro2[0]):
            return 1
        else:
            return -1
    elif (encuentro1[1] > encuentro2[1]):
        return 1
    else:
        return -1

# Funciones de ordenamiento



