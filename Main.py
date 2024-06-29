
import sixteen

def pedir_dimensiones_tablero():
    ya_paso = False
    while True:
            if not ya_paso:
                N=input("•Ingrese el alto del juego: ")
                if not validar_dimensiones(N):
                        print("Porfavor ingrese un numero entre 2 y 9")
                        continue
                else:
                    ya_paso=True
            M=input("•Ingrese el ancho del juego: ")
            if not validar_dimensiones(M):
                    print("Porfavor ingrese un numero entre 2 y 9")
                    continue
            return int(N) , int (M)

def validar_dimensiones (numero):
    if numero.isdigit():
        numero= int(numero)
        return 2 <= int(numero) <= 9

def mostrar_tablero(tablero):
    """Muestra al usuario la lista de listas en formato de tablero con sus respectivos indices"""
    print("")
    indices=[]
    indices.append("  |")
    for i in range(len(tablero[0])):
        indices.append(str(i))
    print(indices[0],end="")
    for indice in indices[1:]:
        print("| ",indice , end=" ")
    print()
  
    separador="  "
    separar_indices_superiores="====="
    for i in range(len(tablero[0])):
        separador += str(separar_indices_superiores.rjust(0,"="))
    print(separador)

    contador_indice=0
    for filas in tablero:

        contador=0
        for columnas in filas:
            if len(str(columnas))== 1:

                if contador==0:
                    print( contador_indice,"|| ",columnas , end=" ")
                    contador_indice+=1
                    contador+=1
                else:
                    print( "| ",columnas , end=" ")                
            else:

                if contador==0:
                    print(contador_indice,"||",columnas , end=" ")
                    contador_indice+=1
                    contador+=1
                else:
                    print( "|",columnas , end=" ")

        print()
    print()

def armar_tablero():
    """Arma el tablero con los datos ingresados en 'pedir_dimensiones_tablero' y luego lo mezcla"""
    N , M = pedir_dimensiones_tablero()
    tablero = sixteen.crear_tablero(N, M)
    sixteen.mezclar_tablero(tablero)
    return tablero

def validar_ingreso_usuario(ingreso_usuario,tablero):
    """Se encarga de validar que el usuario ingrese valores validos y de que esa fila/columna sea rotable. La variable 'datos' se divide en dos, el primer elemento(datos[0]) hace referencia al tipo de rotacion y el segundo elemento(datos[1]) indica en que columna/fila se debe efectuar dicha rotacion"""
    validacion = False 
    datos= ingreso_usuario.split(",")
    if not len(datos)==2 or len(datos[1]) != 1:
        return validacion
    else:
        rotaciones_para_filas="adAD"
        rotaciones_para_columnas="wsWS"
        ingresos_validos = rotaciones_para_filas + rotaciones_para_columnas
        if datos[0] in ingresos_validos:
            if datos[1].isdigit():
                datos[1] = int(datos[1])
                cant_filas = len(tablero)
                cant_columnas= len(tablero[0])

                if datos[0] in rotaciones_para_filas :
                    if 0<=datos[1]< cant_filas:
                        validacion= True

                elif datos[0] in rotaciones_para_columnas :
                    if  0<=datos[1]< cant_columnas:
                        validacion= True

    return validacion
  
def rotar_tablero(ingreso_usuario,tablero):
    datos=ingreso_usuario.split(",")
    """ 'datos [0]' hace referencia al ripo de rotacion y 'datos[1]' a la fila o columna"""
    datos[1]= int(datos[1])
    datos[0]= datos[0].lower()
    if datos[0]=="a":
        sixteen.rotar_izquierda(tablero,datos[1])

    elif datos[0]=="d":
        sixteen.rotar_derecha(tablero,datos[1])

    elif datos[0]=="w":
        sixteen.rotar_arriba(tablero,datos[1])

    elif datos[0]=="s":
        sixteen.rotar_abajo(tablero,datos[1])
    return tablero  

def main():
    print("Bienvenid@ a SIXTEEN !!! \nRealice distintas rotaciones para lograr ordenar el tablero. Buena suerte:)\n")
    tablero= armar_tablero()
    mostrar_tablero(tablero)

    print("Opciones para rotar el tablero:\n  •w -> 'Arriba'  •s -> 'Abajo'  •a -> 'Izquierda'  •d -> 'Derecha'")
    print("\nLa forma correcta de ingreso es:\n •'rotacion','indice'  Ejemplo: •w,4")
    print("\nPara salir del juego presione:\n  •e ->'Exit'")

    condicion=False
    while condicion == False:
        ingreso_usuario=input("Ingreso: •")
        ingreso_usuario = ingreso_usuario.strip()

        salida= "eE"
        if ingreso_usuario not in salida or ingreso_usuario == "": 


            ingreso= True
            while ingreso==True:

                if ingreso_usuario not in salida or ingreso_usuario == "":
                    if validar_ingreso_usuario(ingreso_usuario,tablero)==False:
                        print("\n--> Su ingreso es invalido <-- ")
                        print("\nLa forma correcta de ingreso es:\n •'rotacion','indice'  Ejemplo: •w,4")
                        print("\nPara salir del juego presione:\n  •e ->'Exit'")
                        ingreso_usuario=input("Ingreso: •")
                    else:
                        ingreso= False
                else:
                    print("Suerte la proxima!")
                    return 

            rotar_tablero(ingreso_usuario,tablero)
            mostrar_tablero(tablero)
            condicion=sixteen.esta_ordenado(tablero)
            continue 

        else:
            print("Suerte la proxima!")
            return 
    print("Lograste ordenarlo:D")       
    return 

main()
