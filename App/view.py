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
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listado cronologico de artistas")
    print("3- Listado cronologico de adquisiciones")
    print("4- Clasificar las obras de un artista por tecnica")
    print("5- Clasificar obras por nacionalidad de sus creadores")
    print("6- Mover Obra de un departamento")
    print("7- Proponer una nueva exposición")
    print("8- Organizar una muestra de obras por fecha")
    print("0- Salir")

catalogo = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        print("Cargando información de los archivos ....")
        catalogo = controller.InitCatalog()
        controller.loadArtist(catalogo)
        controller.loadArtwork(catalogo)
        print(lt.getElement(catalogo["Artista"],lt.size(catalogo["Artista"])))
        print(lt.getElement(catalogo["Artista"],lt.size(catalogo["Artista"])-1))
        print(lt.getElement(catalogo["Artista"],lt.size(catalogo["Artista"])-2))
        print(lt.getElement(catalogo["Obra"],lt.size(catalogo["Artista"])))
        print(lt.getElement(catalogo["Obra"],lt.size(catalogo["Artista"])-1))
        print(lt.getElement(catalogo["Obra"],lt.size(catalogo["Artista"])-2))
        print("Se cargaron " + str(lt.size(catalogo["Artista"]))+" artistas")
        print("Se cargaron " + str(lt.size(catalogo["Obra"]))+" obras")
    
    elif int(inputs) == 2:
        año_inicio = int(input("Ingrese el año en el que desea iniciar: "))
        año_final = int(input("Ingrese el año en el que desea terminar: "))
        print(controller.initdateartist(año_inicio,año_final,catalogo))
    
    elif int(inputs) == 3:
        año_inicio = int(input("Ingrese el año en el que desea iniciar: "))
        año_final = int(input("Ingrese el año en el que desea terminar: "))
        total_obras, purchase, primeras_3,ultimas_3 = controller.initdateartwork(año_inicio,año_final,catalogo)
        print("En esas fechas ubo: ",total_obras," obras")
        print("De esas obras ",purchase," fueron compradas")
        print("¡¡PRIMEROS 3!!")
        posicion = 1
        while posicion <= lt.size(primeras_3):
            obra = lt.getElement(primeras_3,posicion)
            print("*"*50)
            print("Titulo : ", obra["Title"])
            print("Fecha : ", obra["Date"])
            print("Medio : ", obra["Medium"])
            print("Dimensiones : ",obra["Dimensions"])
            posicion += 1
        posicion = 1
        print("¡¡ULTIMAS 3!!")
        while posicion <= lt.size(ultimas_3):
            obra = lt.getElement(ultimas_3,posicion)
            print("*"*50)
            print("Titulo : ",obra["Title"])
            print("Fecha : ",obra["Date"])
            print("Medio : ",obra["Medium"])
            print("Dimensiones : ",obra["Dimensions"])
            posicion += 1
    elif int(inputs) == 4:
        nombre_artista = input("Ingrese el nombre del artista: ")
        total_obras,total_tecnicas,tecnica_usada,obras_tecnica = controller.initArtworkvArtist(nombre_artista,catalogo)
        print(nombre_artista," hizo ",total_obras," obras")
        print(nombre_artista," uso ", total_tecnicas," tecnicas")
        print(nombre_artista," usaba mayormente ",tecnica_usada," como tecnica")
        while posicion < lt.size(obras_tecnica):
            obra = lt.getElement(obras_tecnica,posicion)
            print("*"*25)
            print("Titulo : ",obra["Title"])
            print("Fecha : ",obra["Date"])
            print("Medio : ",obra["Medium"])
            print("Dimensiones : ",obra["Dimensions"])
            posicion += 1
    
    
    elif int(inputs) == 8:
        print("¿Que Algoritmo desea utilizar?")
        print("1- Insertion Sort")
        print("2- Merge Sort")
        print("3- Quick Sort")
        print("4- Shell Sort")
        ordenamiento = int(input("Ingrese el algoritmo que le interesa: "))
        size = int(input("Cuantos datos le interesa tomar: "))
        time, sorted_list = controller.initordenamientodataAdquire(catalogo,ordenamiento,size)
        print("El resultado fue:\n",sorted_list)
        print("El proceso tardo: ", time, "ms")
    else:
        sys.exit(0)
sys.exit(0)