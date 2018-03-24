"""
Se definen utilidades para el script.

lineas: lista donde se guardan linea a linea las entradas leidas
    Las entradas se guardan en forma de tupla (size,numero).
switch_techo: diccionario con la definicion para la primera
    linea de cada numero.
switch_cuerpo_superior: diccionario con la definicion
    para la parte superior (debajo de la primera linea) de
    cada numero. (los bordes laterales superiores)
switch_mitad: diccionario con la definicion para la parte
    media de cada numero. (sin contar bordes)
switch_cuerpo_inferior: diccionario con la definicion
    para la parte inferior (debajo de la linea media) de
    cada numero. (bordes laterales inferiores)
switch_piso: diccionario con la definicion de la ultima linea
    de cada numero.

"""
lineas = []
switch_techo = {'1':' ','2':'_','3':'_','4':' ','5':'_','6':'_','7':'_','8':'_','9':'_','0':'_'}
switch_cuerpo_superior = {'1':' |','2':' |','3':' |','4':'||','5':'| ','6':'| ','7':' |','8':'||','9':'||','0':'||'}
switch_mitad = {'1':' ','2':'_','3':'_','4':'_','5':'_','6':'_','7':' ','8':'_','9':'_','0':' '}
switch_cuerpo_inferior = {'1':' |','2':'| ','3':' |','4':' |','5':' |','6':'||','7':' |','8':'||','9':'| ','0':'||'}
switch_piso = {'1':' ','2':'_','3':'_','4':' ','5':'_','6':'_','7':' ','8':'_','9':'_','0':'_'}
