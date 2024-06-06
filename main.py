# Iván Sacks 2024 Parcial 1
# 1) Cargar archivo .CSV: Se pedirá el nombre del archivo y se cargará en una lista de
# diccionarios los elementos
# del mismo.
# 2) Imprimir lista: Se imprimirá por pantalla la tabla con los datos de las películas.
# 3) Asignar rating: Se deberá hacer uso de la función map. La cual recibirá la lista y una
# función que asignará a la película un valor de rating flotante entre 1 y 10 con 1 decimal
# calculado de manera aleatoria se mostrará por pantalla el mismo.
# 4) Asignar género: Se deberá hacer uso de la función map. La cual recibirá la lista y una
# función que asignará a la película un género de acuerdo a un número aleatorio entre 1 y 4.
# 1: drama
# 2: comedia
# 3: acción
# 4: terror
# 5) Filtrar por género: Se deberá pedir un género y escribir un archivo igual al original, pero
# donde solo aparezcan películas del género seleccionado. El nombre del archivo será p.e. comedias.csv
# 6) Ordenar películas: Se deberá mostrar por pantalla un listado de las películas ordenadas por
# género y dentro de las del mismo género que aparezcan ordenadas por rating descendente.
# 7) Informar Mejor Rating: Mostrar el titulo y el rating de la película con más rating
# 8) Guardar películas: Se deberá guardar el listado del punto anterior en un archivo JSON.
import os
from modulo_funciones import *

path_0 = os.getcwd()
path = os.path.join(path_0, "Iv-n_Sacks_Parcial_LABA112/movies.csv")

programa = True
menu_opciones = ("Que desea hacer?\n"
                "1: Cargar CSV\n"
                "2: Imprimir lista\n"
                "3: Asignar rating\n"
                "4: Asignar género\n"
                "5: Filtrar por género\n"
                "6: Ordenar películas\n"
                "7: Informar Mejor Rating\n"
                "8: Guardar películas\n"
                "9: Salir\n")

while programa:
    
    opcion = input(menu_opciones)
    try:
        opcion = int(opcion)
    except:
        raise ValueError("Por favor, ingrese numeros solamente")
    
    while opcion < 1 or opcion > 9:
        opcion = input(f"Por favor ingrese numeros validos {menu_opciones}")

    match opcion:
        case 1:
            #1
            peliculas = cargar_csv(path)
        case 2:
            #2
            mostrar_peliculas(peliculas)
        case 3:
            #3
            mapear_pelicula(peliculas, asignar_rating)
        case 4: 
            #4
            mapear_pelicula(peliculas, asignar_genero)
        case 5:
            #5
            genero = input("Ingrese el genero que quieres filtrar: drama, comedia, acción, terror ")

            while genero != "drama" and genero != "comedia" and genero != "acción" and genero != "terror":
                genero = input("Rengrese el genero que quieres filtrar: drama, comedia, acción, terror ")

            filtrar_genero(peliculas, genero, path_0)
        case 6:
            #6
            ordenar_genero_rating_dsc(peliculas)
        case 7:
            #7
            titulo_max, rt_max = rating_max(peliculas)
            mostrar_peliculas(peliculas)
            print(f"La pelicula con mayor rating es: {titulo_max} con: {rt_max}.pts de rating")
        case 8:
            #8
            guardar_peliculas_json(peliculas, path_0)
        case 9:
            programa = False

