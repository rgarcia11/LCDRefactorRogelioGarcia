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
    techo = ''
    for digito in numero:
        techo += ' '+switch_techo[digito]*size+' '
    print(techo)

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
    cuerpoSuperior = ''
    for digito in numero:
        cuerpoSuperior += switch_cuerpo_superior[digito][0] + (' '*size) + switch_cuerpo_superior[digito][1]
    print((cuerpoSuperior+'\n')*size, end='', flush=True)

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
    mitad = ''
    for digito in numero:
        mitad += switch_cuerpo_superior[digito][0] + switch_mitad[digito]*size + switch_cuerpo_superior[digito][1]
    print(mitad)


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
    cuerpoInferior = ''
    for digito in numero:
        cuerpoInferior += switch_cuerpo_inferior[digito][0] + (' '*size) + switch_cuerpo_inferior[digito][1]
    print((cuerpoInferior+'\n')*size, end='', flush=True)


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
    piso = ''
    for digito in numero:
        piso += switch_cuerpo_inferior[digito][0] + switch_piso[digito]*size + switch_cuerpo_inferior[digito][1]
    print(piso)
