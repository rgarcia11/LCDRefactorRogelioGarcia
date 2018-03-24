"""
Este script solo debe ser importado como un modulo,
no ocurre nada al ejecutarlo.
"""
from definiciones import *

def techo(size, numero):
    """
    Escribe la primera linea de cada digito.
    Esta linea puede ser vacia en algunos casos, como el 1, 4.

    args:
        size: escala con la que se quiere imprimir el numero.
        numero: el numero que se quiere imprimir. Puede componerse
            de varios digitos.
    """
    for digito in numero:
        print(' ',end='',flush=True)
        for tam in range(0,size):
            print(switch_techo[digito],end='',flush=True)
        print(' ',end='',flush=True)
    print('')

def cuerpoSuperior(size, numero):
    """
    Escribe las lineas entre la primera y la mitad.
    El numero de lineas impresas es igual a size.
    El numero de espacios insertados entre los bordes
    izquierdo y derecho del numero es igual a size.
    El borde izquierdo esta dado por:
        switch_cuerpo_superior[digito][0]
    El borde derecho por:
        switch_cuerpo_superior[digito][1]

    args:
        size: escala con la que se quiere imprimir el numero.
        numero: el numero que se quiere imprimir. Puede componerse
            de varios digitos.
    """
    for tam in range(0, size):
        for digito in numero:
            print(switch_cuerpo_superior[digito][0],end='',flush=True)
            for tam2 in range(0,size):
                print(' ',end='',flush=True)
            print(switch_cuerpo_superior[digito][1],end='',flush=True)
        print('')

def mitad(size, numero):
    """
    Escribe el contenido del medio de cada numero.
    Este puede ser una linea, como en el numero 2, 3, etc.,
    o puede estar vacio, como en el 1 y el 0.

    args:
        size: escala con la que se quiere imprimir el numero.
        numero: el numero que se quiere imprimir. Puede componerse
            de varios digitos.
    """
    for digito in numero:
        print(switch_cuerpo_superior[digito][0],end='',flush=True)
        for tam in range(0,size):
            print(switch_mitad[digito],end='',flush=True)
        print(switch_cuerpo_superior[digito][1],end='',flush=True)
    print('')

def cuerpoInferior(size, numero):
    """
    Escribe las lineas entre la linea de la mitad y la ultima linea.
    El numero de lineas impresas es igual a size.
    El numero de espacios insertados entre los bordes
    izquierdo y derecho del numero es igual a size.
    El borde izquierdo esta dado por:
        switch_cuerpo_inferior[digito][0]
    El borde derecho por:
        switch_cuerpo_inferior[digito][1]

    args:
        size: escala con la que se quiere imprimir el numero.
        numero: el numero que se quiere imprimir. Puede componerse
            de varios digitos.
    """
    for tam in range(0, size):
        for digito in numero:
            print(switch_cuerpo_inferior[digito][0],end='',flush=True)
            for tam2 in range(0,size):
                print(' ',end='',flush=True)
            print(switch_cuerpo_inferior[digito][1],end='',flush=True)
        print('')

def piso(size, numero):
    """
    Escribe la ultima linea de cada numero.
    Este puede ser una linea, como en el numero 5, 6, etc.,
    o puede estar vacio, como en el 1 y el 4.

    args:
        size: escala con la que se quiere imprimir el numero.
        numero: el numero que se quiere imprimir. Puede componerse
            de varios digitos.
    """
    for digito in numero:
        print(switch_cuerpo_inferior[digito][0],end='',flush=True)
        for tam in range(0,size):
            print(switch_piso[digito],end='',flush=True)
        print(switch_cuerpo_inferior[digito][1],end='',flush=True)
    print('')
