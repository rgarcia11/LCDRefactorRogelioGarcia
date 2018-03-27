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
Se realizó el programa desde cero.

### Funcionamiento
Parámetros para dibujar un número: size y el número. Size define el tamaño en el que se debe dibujar el número.

Se dividieron los dígitos en cinco secciones. Cada dígito tiene un techo, una parte superior, una mitad, una parte inferior y un piso.
Techo: se componen totalmente de espacios (" ") o de guiones bajos ("\_"). Al lado izquierdo y derecho del techo hay siempre un espacio (" ").
Mitad y piso: similar a techo, se componen principalmente de espacios (" ") o de guiones bajos ("\_"), pero adicionalmente tienen a su lado izquierdo y derecho un espacio (" ") o una barra ("|").
Parte superior e inferior: pueden componerse de varias líneas, dependiendo de size. Cada línea tiene un símbolo al lado izquierdo y derecho, que puede ser espacio (" ") o barra ("|"), y entre ellos un número de espacios que depende de size.

Por ejemplo, el dígito 9 con size 2:

<pre>
 ___      techo: un espacio, dos guiones bajos y otro espacio
|   |     parte superior: dos lineas iguales; una barra, tres espacios y otra barra.
|   |     
|___|     mitad: una barra, tres guiones bajos y otra barra
    |     parte inferior: dos lineas iguales; cuatro espacios y una barra.
    |
 ___|     piso: un espacio, dos guiones bajos y una barra
</pre>

Como se puede ver, el techo siempre tiene dos espacios en los límites izquierdo y derecho, la mitad tiene los mismos símbolos que la parte superior a sus lados izquierdo y derecho, respectivamente, y el piso comparte los lados izquierdo y derecho con la parte inferior del dígito.

Para saber qué elemento utilizar al dibujar una de las partes de un dígito, se tienen cinco diccionarios, uno por cada parte del dígito. Ahí se define si un nueve tiene dos barras al lado izquierdo y derecho en la parte superior, pero solo una barra en el lado derecho la parte inferior.

<pre>
Si se quiere agregar un caracter adicional, se agrega a este diccionario y se modifican las verificaciones del input del programa para aceptarlo.
</pre>

### Input
El programa únicamente recibe parejas de dos números separados por comas. Cada pareja debe ser separada por un salto de línea. El programa siempre finaliza con "0,0". El único error en el input que acepta el programa son espacios laterales, por ejemplo " 10 , 129038 ". Se asume que estos espacios son involuntarios, y no afectan el entendimiento de la intención del usuario.
* Ejemplo de input correcto:
<pre>
1,9
3,0123456789
10,951
 10 , 18 
0,0
</pre>

* Ejemplos de inputs incorrectos, caracteres no permitidos, size > 10, size = 0, letras:
<pre>
10:534
10'531
10//531
11,5
0,5
10,5a5
 10 , 129038  
0,0
</pre>

### Output
Se ingresan las siguientes líneas (nota, para probarlo con el código, es posible que se necesite copiar el input ejemplo y pegarlo en un editor de texto, y luego volver a copiar y  pegarlo en el programa):

Out:
<pre>
1,9
3,0123456789
10,951
0,0
</pre>

In:
<pre>
 _
| |
|_|
  |
 _|

 ___       ___  ___       ___  ___  ___  ___  ___
|   |    |    |    ||   ||    |        ||   ||   |
|   |    |    |    ||   ||    |        ||   ||   |
|   |    |    |    ||   ||    |        ||   ||   |
|   |    | ___| ___||___||___ |___     ||___||___|
|   |    ||        |    |    ||   |    ||   |    |
|   |    ||        |    |    ||   |    ||   |    |
|   |    ||        |    |    ||   |    ||   |    |
|___|    ||___  ___|    | ___||___|    ||___| ___|

 __________  __________
|          ||                      |
|          ||                      |
|          ||                      |
|          ||                      |
|          ||                      |
|          ||                      |
|          ||                      |
|          ||                      |
|          ||                      |
|          ||                      |
|__________||__________            |
           |           |           |
           |           |           |
           |           |           |
           |           |           |
           |           |           |
           |           |           |
           |           |           |
           |           |           |
           |           |           |
           |           |           |
 __________| __________|           |
</pre>

### Otras consideraciones
El unico cambio que se hizo fue imprimir "\_" en lugar de "-", dado que en el enunciado se especificada "-" pero en el ejemplo se mostraba "\_", y el guión bajo es más legible.
