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
import datetime
assert config

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    catalog = {'encuentros': None,
                'datetime': None
                }

    catalog['encuentros'] = lt.newList('SINGLE_LINKED')
    catalog['ciudad'] = mp.newMap(maptype='PROBING',
                                    )
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
    return catalog

# Funciones para creacion de datos

# Funciones de consulta

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

# Funciones de ordenamiento


