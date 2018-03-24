"""
Este script lee un input de una serie de numeros y la imprime
en estilo pantalla de LCD teniendo en cuenta el tamanho que
entra por la entrada estandar del programa.
Mas detalles en el README del proyecto y en cada funcion.
"""
#Imports
import sys
from impresora import *

def lectura():
    """
    Lee de entrada estandar linea por linea.
    El formato esperado de cada linea es:
        size,numero
    De la forma:
        5,1542
    Se termina con 0,0. Ejemplo:
        5,1542
        2,123
        0,0
    Primero se leen todas las lineas y se guarda en memoria.
    Esto se debe a que la salida debe ser apartada de la entrada.
    Es decir, primero se lee todo y luego se imprime todo.
    """
    for linea in sys.stdin:
        #Puede contener espacios o saltos de linea
        linea = linea.strip()
        linea = linea.split(',')
        size = linea[0]
        numero = linea[1]
        if not (esNumero(size) and esNumero(numero)):
            #print('La entrada {},{} no es valida'.format(size,numero))
            continue

        if size == '0' and numero == '0':
            #print('Ha finalizado el programa con un "0,0"')
            break
        if size == '0':
            #print('La entrada {},{} no es valida; size no debe ser 0'.format(size,numero))
            break
        lineas.append((size,numero))

def escritura():
    """
    Escribe el output del programa en consola.
    Se quiere que los numeros listados se escriban
    en el estilo de una pantalla LCD.
    Se utiliza el caracter "_" para simbolos horizontales
    y el caracter "|" para simbolos verticales.
    Cada dígito tiene las siguientes medidas:
        columnas: size+2
        filas: 2*size + 3
    Entre cada impresion debe haber una linea blanca.
    """
    for linea in lineas:
        size = int(linea[0])
        numero = linea[1]
        #Se procesan los "techos"
        techo(size, numero)
        cuerpoSuperior(size, numero)
        mitad(size, numero)
        cuerpoInferior(size, numero)
        piso(size, numero)
        print()



def esNumero(posible_numero):
    """
    Funcion auxiliar. Recibe un string y decide si es un numero.
    args:
        posible_numero: string a evaluar.
    retorna boolean True or False.
    """
    try:
        int(posible_numero)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    """
    Si se corre este script, se ejecutan
    las funciones en el orden correcto.
    """
    lectura()
    escritura()