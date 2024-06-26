import random, math, json

def cargar_csv(path: str) -> list:
    """Recibe una dirección de memoria, carga el csv en una lista 
    de diccionarios y devuelve esa lista


    Args:
        path (str): Dirección de memoria

    Returns:
        Lista(list): Una lista de diccionarios3
    """
    with open(path, "r", encoding = "utf-8") as archivo:
        lista = []
        encabezado = archivo.readline().strip("\n").split(",")
        for linea in archivo.readlines():
            peliculas = {}
            linea = linea.strip("\n").split(",")
            id, titulo, genero, rating = linea 
            
            peliculas["id"] = int(id)
            peliculas["titulo"] = titulo
            peliculas["genero"] = genero
            peliculas["rating"] = int(rating)
            lista.append(peliculas)

        return lista
    
def mostrar_peliculas(peliculas: list):
    """Recibe una lista de diccionarios y la muestra en pantalla. No devuelve nada

    Args:
        peliculas (list): Las peliculas a mostrar
    """
    print("ID           TITULO                       GENERO      RATING")
    for i in range(len(peliculas)):
        print(f" {peliculas[i]["id"]:3}    {peliculas[i]["titulo"]:<30}   {peliculas[i]["genero"]:<8}      {peliculas[i]["rating"]:2}")


def mapear_pelicula(lista: list, funcion):
    """Recibe una lista de diccionarios y una funcion.
    Mapea la lista y no devuelve nada

    Args:
        lista (list): La lista a mapear
        funcion (funct): La funcion que mapea la lista
    """
    for i in range(len(lista)):
        funcion(lista, i)

def asignar_rating(lista: list, pelicula: int):
    """Recibe una pelicula y le asigna un numero del 1 al 10 y un decimal

    Args:
        lista (list): La lista a asignar
        pelicula (int): La pelicula del valor que se va a cambiar
    """
    lista[pelicula]["rating"] = round(random.uniform(1, 10), 1)



def asignar_genero(lista: list, pelicula: int):
    """Recibe una generi y le asigna unode acuerdo a un número aleatorio entre 1 y 4.

    Args:
        lista (list): La lista a asignar
        pelicula (str): La pelicula del genero que se va a cambiar
    """
    numero = random.randint(1, 4)
    if numero == 1:
        genero = "drama"
    elif numero == 2:
        genero = "comedia"
    elif numero == 3:
        genero = "acción"
    elif numero == 4:
        genero = "terror"

    lista[pelicula]["genero"] = genero

def filtrar_genero(lista:list, genero: str, path: str):
    """Recibe una lista, un genero y una dirrecion de memoria, 
    crea un archivo csv y guarda las peliculas del genero correspondiente

    Args:
        lista (list): La lista a escribir
        genero (str): EL genero a filtrar
        path (str): La dirrecion de memoria donde crear el archivo
    """
    with open(f"{path}p.e.comedias.csv", "w", encoding = "utf-8") as archivo:
        archivo.write("ID           TITULO                   GENERO      RATING\n")
        for i in range(len(lista)):
            if lista[i]["genero"] == genero:
                id = f"{lista[i]["id"]:3}  "
                genero = lista[i]["genero"]
                titulo = f"  {lista[i]["titulo"]:<30} " 
                rating = f"       {lista[i]["rating"]:2}\n"

                archivo.write(id)
                archivo.write(titulo)
                archivo.write(genero)
                archivo.write(rating)


def rating_max(lista: list):
    """Recibe una lista, calcula cual es la pelicula con el 
    rating mas alta, devuelve el nombre y rating de esta

    Args:
        lista (list): La lista a comparar

    Returns:
        float: El titulo la pelicula
        str: El rating de la pelicula
    """
    titulo_max = "Ninguno"
    rating_max = 0
    bandera = True
    for i in range(len(lista)):
        if lista[i]["rating"] > rating_max or bandera:
            bandera = False
            titulo_max = lista[i]["titulo"]
            rating_max = lista[i]["rating"]

    return titulo_max, rating_max

def cambiar_peliculas(lista, i, j):
    """Recibe una lista y dos peliculas,
    las cambia de lugar, 
    no devuelve nada

    Args:
        lista (_type_): La lista con las peliculas
        i (int): Primer pelicula
        j (int): Segunda pelicula
    """
    for clave, valor in lista[i].items():
        aux = lista[i][clave]
        lista[i][clave] = lista[j][clave]
        lista[j][clave] = aux


def ordenar_genero_rating_dsc(lista: list):
    """Recibe una lista,
    ordena la lista por genero dentro de este por rating descendiente
    no devuelve nada

    Args:
        lista (list): La lista a ordenar
    """
    for i in range(len(lista) -1):
        for j in range(i + 1, len(lista)):
            if lista[i]["genero"] == lista[j]["genero"]:
                if lista[i]["rating"] < lista[j]["rating"]:
                    cambiar_peliculas(lista, i, j)
            elif lista[i]["genero"] > lista[j]["genero"]:
                cambiar_peliculas(lista, i, j)


def guardar_peliculas_json(lista: list, path: str):
    with open(f"{path}/p.e.ordenadas.json", "w", encoding = "utf-8") as archivo:
        json.dump(lista, archivo, ensure_ascii = False, indent = 4)

