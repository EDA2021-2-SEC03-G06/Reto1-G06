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
 """

from DISClib.ADT.list import size
from os import read
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def InitCatalog():
    return model.NewCatalog()
# Funciones para la carga de datos
def loadArtist(catalogo):
    booksfile = cf.data_dir + "Artists-utf8-large.csv"
    file = csv.DictReader(open(booksfile,encoding = "utf-8"))
    for Artist in file :
        model.addArtist(catalogo,Artist)

def loadArtwork(catalogo):
    booksfile = cf.data_dir + "Artworks-utf8-large.csv"
    file = csv.DictReader(open(booksfile,encoding = "utf-8"))
    for Artwork in file :
        model.addArtwork(catalogo,Artwork)
# Funciones de ordenamiento
def initordenamientodataAdquire(catalogo,ordenamiento,size):
    if ordenamiento == 1:
        orden = model.insertion_sort(catalogo["Obra"],size,model.compareDateAcquired)
    elif ordenamiento == 2:
        orden = model.merge_sort(catalogo["Obra"],size,model.compareDateAcquired)
    elif ordenamiento == 3:
        orden = model.quick_sort(catalogo["Obra"],size,model.compareDateAcquired)
    elif ordenamiento == 4:
        orden = model.shell_sort(catalogo["Obra"],size,model.compareDateAcquired)
    return orden    
# Funciones de consulta sobre el catálogo
def initdateartist(año_inicio,año_final,catalogo):
    return model.dateartist(año_inicio,año_final,catalogo)
def initdateartwork(año_inicio,año_final,catalogo):
    return model.dateArtwork(año_inicio,año_final,catalogo)
def initArtworkvArtist(nombre_artista,catalogo):
    return model.ArtworkvArtist(nombre_artista,catalogo)