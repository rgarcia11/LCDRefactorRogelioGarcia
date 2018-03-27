# LCDRefactorRogelioGarcia

## Intención
El enunciado del problema es el siguiente:
> # LCD refactor
>
>
> Objetivo: Crear un programa que imprime números en estilo de una pantalla LCD
>
> Entrada: La entrada contiene varias líneas. Cada línea contiene 2 números separados por coma. El primer número representa el tamaño de la impresión (entre 1 y 10, esta variable se llama “size”). El segundo número es el número a mostrar en la pantalla. Para terminar, se debe digitar 0,0. Esto terminará la aplicación.
>
> Salida: Imprimir los números especificados usando el caracter “-“ para los caracteres horizontales, y “|” para los verticales. Cada dígito debe ocupar exactamente size+2 columnas y 2*size + 3 filas.
>
> Entre cada impresión debe haber una línea blanca.
>
> Ejemplo:
> Entrada:
>
> 2,12345
>
> 3,67890
>
> 0,0
>
>   
> Salida:   

  <pre>  
   _ _  _ _        _ _
|     |    | |  | |
|  _ _| _ _| |__| |_ _
| |        |    |     |
| |_ _  _ _|    |  _ _|

 _ _ _  _ _ _   _ _ _   _ _ _   _ _ _
|            | |     | |     | |     |
|            | |     | |     | |     |
|_ _ _       | |_ _ _| |_ _ _| |     |
|     |      | |     |       | |     |
|     |      | |     |       | |     |
|_ _ _|      | |_ _ _|  _ _ _| |_ _ _|

</pre>

## Descripción del proyecto
### Generalidades
El código fue realizado en Python 3.6.1. Correrlo en versiones anteriores, particularmente Python2, puede generar errores.

El código se encuentra comentado en su totalidad. Hay cuatro scripts en python:
LCD.py --> script principal del proyecto. Se debe correr este script para dar inicio al programa.
definiciones.py --> define cómo se van a imprimir los números.
impresora.py --> hace uso de definiciones.py para dar el formato de impresión. En este script se define el output que será impreso en LCD.py.
testImpresora.py --> script de pruebas unitarias que verifica el correcto funcionamiento de la impresora. Este script se corre por aparte.

En general, se priorizó obtener un código sencillo y altamente modificable.

### Funcionamiento
Se dividieron los dígitos en cinco secciones. Cada dígito tiene un techo, una parte superior, una mitad, una parte inferior y un piso.
Techo: se compone totalmente de espacios (" ") o de guiones bajos ("\_")

El unico cambio que se hizo fue imprimir "\_" en lugar de "-"
