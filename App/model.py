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


from DISClib.DataStructures.arraylist import getElement, size
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import shellsort as ss
import datetime as dt
import time as chronos
assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def NewCatalog():
    catalogo = {"Artista":None,
                "Obra": None}
    catalogo["Artista"] = lt.newList()
    catalogo["Obra"] = lt.newList()
    return catalogo
# Funciones para agregar informacion al catalogo
def addArtist(catalogo,Artist):
    lt.addLast(catalogo["Artista"],Artist)
def addArtwork(catalogo,Artwork):
    lt.addLast(catalogo["Obra"],Artwork)
# Funciones para creacion de datos
def ArtworkvArtist(nombre_artista,catalogo):
    obras_artista = {}
    total_obras = 0
    total_medios = 0
    posicion = 0
    while posicion < lt.size(catalogo["Artist"]) and nombre_artista != lt.getElement(catalogo["Artista"],posicion)["DisplayName"]:
        posicion += 1
    constituenID_artista = lt.getElement(catalogo["Artista"],posicion)["ConstituentID"]
    for obra in catalogo["Obra"]:
        if obra["ConstituentID"] == constituenID_artista:
            if obra["Medium"] in obras_artista:
                lt.addlast(obras_artista[obra["Medium"]],obra)
            else:
                obras_artista[obra["Medium"]] = lt.newList()
                lt.addLast(obras_artista[obra["Medium"]],obra["Medium"])
                total_medios += 1
            total_obras += 1
    medio_n = 0
    nombre = ""
    for llave in obras_artista.keys:
        if lt.size(obras_artista[llave]) > medio_n:
            medio_n = lt.size(obras_artista[llave])
            nombre = llave
    return (total_obras,total_medios,nombre,obras_artista[nombre])
    
# Funciones de consulta
def dateArtwork(fecha_inicio,fecha_fin,catalogo):
    obras_rango = lt.newList
    obras_purchase = 0
    for obra in catalogo["Obra"]:
        fecha = obra["Date"]
        if dt.datetime.strptime(fecha,"%Y") > fecha_inicio and dt.datetime.strptime(fecha,"%Y") > fecha_fin:
            lt.addLast(obras_rango,obra)
            if obra["CreditLine"] == "Purchase":
                obras_purchase += 1
    tamaño = lt.size(obras_rango)
    obras_sorted = shell_sort(obras_rango,tamaño,compareData)
    return(tamaño,obras_purchase,lt.subList(obras_sorted,1,3),lt.subList(obras_sorted,lt.size(obras_sorted)-3))
# Funciones utilizadas para comparar elementos dentro de una lista
def compareDateAcquired(obra1,obra2):
    return (dt.datetime.strptime(obra1["DateAcquired"],"%Y-%m-%d") > dt.datetime.strptime(obra2["DateAcquired"],"%Y-%m-%d"))
def compareData(obra1,obra2):
    return (dt.datetime.strptime(obra1["Date"],"%Y") > dt.datetime.strptime(obra2["Date"],"%Y"))
# Funciones de ordenamiento
def insertion_sort(catalogo,size,cmpfuncion):
    sub_list = lt.subList(catalogo["Obra"], 1, size)
    start_time = chronos.process_time()
    sorted_list = ins.sort(sub_list,cmpfuncion)
    stop_time = chronos.process_time()
    time = (stop_time - start_time)*1000
    return (time,sorted_list)

def merge_sort(catalogo,size,cmpfuncion):
    sub_list = lt.subList(catalogo["Obra"], 1, size).copy
    start_time = chronos.process_time()
    sorted_list = ms.sort(sub_list,cmpfuncion)
    stop_time = chronos.process_time()
    time = (stop_time - start_time)*1000
    return (time,sorted_list)

def quick_sort(catalogo,size,cmpfuncion):
    sub_list = lt.subList(catalogo["Obra"], 1, size).copy
    start_time = chronos.process_time()
    sorted_list = qs.sort(sub_list,cmpfuncion)
    stop_time = chronos.process_time()
    time = (stop_time - start_time)*1000
    return (time,sorted_list)

def shell_sort(catalogo,size,cmpfuncion):
    sub_list = lt.subList(catalogo["Obra"], 1, size).copy
    start_time = chronos.process_time()
    sorted_list = ss.sort(sub_list,cmpfuncion)
    stop_time = chronos.process_time()
    time = (stop_time - start_time)*1000
    return (time,sorted_list)