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


from DISClib.DataStructures.arraylist import getElement
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
import datetime as dt
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
    obras_artista = lt.newList()
    posicion = 0
    while posicion < lt.size(catalogo["Artist"]) and nombre_artista != lt.getElement(catalogo["Artista"],posicion)["DisplayName"]:
        posicion += 1
    constituenID_artista = lt.getElement(catalogo["Artista"],posicion)["ConstituentID"]
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento