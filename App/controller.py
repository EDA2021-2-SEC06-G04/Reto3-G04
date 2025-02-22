﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog, file):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    file = cf.data_dir + file
    input_file = csv.DictReader(open(file, encoding="utf-8"),
                                delimiter=",")
    for encuentro in input_file:
        model.addEncuentro(catalog, encuentro)
    return catalog

# Funciones de ordenamiento


# Funciones de consulta sobre el catálogo

def ciudadmayor(catalog):
    "Retorna el nombre de la ciudad con mayor numero de encuentros"
    return model.ciudadmayor(catalog)

def rangosegundos(catalog,min,max):
    "Retorna una lista con todos los elementos con duraciones en segundos entre los máximo y mínimo dados"
    return model.rangosegundos(catalog,float(min),float(max))

def rangofechas(catalog,min,max):
    "Retorna una lista con todos los encuentros sucedidos entre las dos fechas que entran por parámetro"
    return model.rangofechas(catalog,min,max)

def ciudadHeight(catalog,ciudad):
    """
    Altura del indice (arbol)
    """
    return model.ciudadHeight(catalog,ciudad)


def ciudadSize(catalog,ciudad):
    """
    Numero de nodos en el arbol
    """
    return model.ciudadSize(catalog,ciudad)
