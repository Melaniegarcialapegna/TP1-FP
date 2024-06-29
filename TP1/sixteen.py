
import random

def crear_tablero(n_filas: int, n_columnas: int) -> list[list[int]]:
    tablero=[]
    numero = 0
    for fila in range(n_filas):
        filas=[]
        for columna in range(n_columnas):
            numero += 1
            filas.append(numero)
        tablero.append(filas)
    return tablero

def rotar_positivo(lista)-> list[int]:
    numeros_rotados=[]
    for numero in lista[1:]:
        numeros_rotados.append(numero)
    numeros_rotados.append(lista[0])
    return numeros_rotados
  
def rotar_negativo(lista)-> list[int]:
    numeros_rotados=[]
    numeros_rotados.append(lista[-1])
    for numero in lista[:-1]:
        numeros_rotados.append(numero)
    return numeros_rotados

def generar_columna(tablero, columna)-> list[int]:
    numeros_columnas_1=[]
    for filas in tablero:
        numeros_columnas_1.append(filas[columna])
    return numeros_columnas_1
  
def generar_fila(tablero, fila)-> list[int]:
    return tablero[fila]

def remplazar_columna(tablero, lista, columna):
    contador_lista = 0
    while contador_lista < len(lista):
        for lst in tablero:
            agregar_numero = lista[contador_lista]
            lst[columna]= agregar_numero
            contador_lista+=1

def reemplazar_fila(tablero, lista, fila):
    tablero[fila]= lista

def rotar_arriba(tablero: list[list[int]], columna: int) -> bool:
    if 0<= columna < len(tablero[0]):
        remplazar_columna(tablero, rotar_positivo(generar_columna(tablero, columna)), columna)
        return True
    return False

def rotar_abajo(tablero: list[list[int]], columna: int) -> bool:
    if 0<= columna < len(tablero[0]):
        remplazar_columna(tablero, rotar_negativo(generar_columna(tablero, columna)), columna)
        return True
    return False

def rotar_izquierda(tablero: list[list[int]], fila: int) -> bool:
    if 0<= fila < len(tablero):
        reemplazar_fila(tablero, rotar_positivo(generar_fila(tablero, fila)), fila)
        return True
    return False

def rotar_derecha(tablero: list[list[int]], fila: int) -> bool:
    if 0<= fila < len(tablero):
        reemplazar_fila(tablero, rotar_negativo(generar_fila(tablero, fila)),fila)
        return True
    return False

def esta_ordenado(tablero: list[list[int]]) -> bool:
    contador = 1
    for fila in tablero:
        for columna in fila:
            if columna != contador:
                return False
            contador += 1
    return True

def mezclar_tablero(tablero: list[list[int]]):
    cantidad_veces=random.randint(200,400)
    contador_rotaciones=0
    cantidad_filas= len(tablero)
    cantidad_columnas= len(tablero[0])
    while cantidad_veces!= contador_rotaciones:
        tipo_rotacion=random.randint(1,4)
        fila_random=random.randint(0,cantidad_filas-1)
        columna_random=random.randint(0,cantidad_columnas-1)

        if tipo_rotacion==1:
            rotar_izquierda(tablero,fila_random)

        elif tipo_rotacion==2:
            rotar_derecha(tablero,fila_random)

        elif tipo_rotacion==3:
            rotar_arriba(tablero,columna_random)

        elif tipo_rotacion==4:
            rotar_abajo(tablero,columna_random)

        contador_rotaciones+=1
