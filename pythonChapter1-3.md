# **Resumen de capítulos 1-3 de Python**
## Operadores
* Suma +
* Resta -
* Multiplicación *
* División /
* Expotenciación **
* Operador de Bits XOR ^

Los operadores <<,>>, &, |, y ^ son operadores de bits. Ademas, pueden ser utilizados con números. Los cuales son tratados como un *string* de bits, escritos en binario. [Pagina de Operador de bit](https://wiki.python.org/moin/BitwiseOperators)

 X << Y. Regresa *X* con los bits cambiados a la izquierda por *Y* lugares y al lado derecho son ceros. Es lo mismo que multiplicar X * (2 ** Y).

     **Ejemplos**:

    2 << 2 Donde:

        2 * (2 ** 2) = 8 (10000)

    7 << 2. Donde:

        7 * (2 ** 2) = 28 (0001 1100)
* X >> Y. Regresa *X* con los bits cambiados a la derecha por *Y* lugares y al lado izquierdo son ceros. Es lo mismo que multiplicar X * (2 ** Y).

    **Ejemplos**:

    2(0010) >> 2(0010) Donde:

        2 * (2 ** 2) = 0

    96(0110 0000) >> 2(0010) Donde:

        96 * (2 ** 2) = 384 (0001 1100 0000) Si se agregan a la izquierda da como resultado 384 pero, como los valores se agregan a la derecha quedan como 24 (0001 1000)

        000**1 11**00 0000 = 384 Valor agregado a la izquierda

         0000 *0110* 0000 = 96 Original

        0000 000**1 1**000 = 24 Valor agregado a la izquierda.
* **&** Realiza un *AND* de bit. Por cada bit en el output es 1 si corresponden los bits de *X* y los de *Y*, de lo contrario regresa 0.
* **|** Realiza un *OR* de bit. Por cada bit en el output es 0 si corresponden los bits de *X* y los de *Y*, de lo contrario regresa 1.
* **~** Realiza el complemento de X.
* **^** Realiza el exclusivo *OR*. Si cada bit en el output es el mismo que el correspondiente bit en *X* y *Y* es 0, y es el complemento del bit en *X* y en ese bit en *Y* es 1.

## Think Python, 2nd Edition

Los lenguajes de programación son lenguajes formales. Los cuales son diseñados para una aplicación en especifico. Un ejemplo de esto, es la notación matemática y el lenguaje para representar las estructuras de las moléculas. 
Los lenguajes formales tienden a tener una serie de reglas de sintaxis. Las reglas de sintaxis se pueden ver en dos formas **toquen** y **estructura**. Tokens son elementos básicos del lenguaje, como palabras, números. Uno de los problemas con la expresión  **3+ = 3 % 6** es que **%**no es un toquen legal. La segunda regla es la forma en que los toquens son combinados.

**Parsing** es la acción de leer una oración, donde tienes que descifrar la estructura.

## Python Essential

El fundamento para la programación en Python es **Read-Evaluate-Print Loop** (**REPL**). Aunque se puedan realizar otras tareas es esencialmente lo mismo ya que interactúa con *REPL*.

Una expresión por si misma es un declaración. Mientras que el valor de una expresión no sea *None*, REPL nos mostrará el valor de la expresión. Esta simple expresión nos permite realizar cosas como las siguientes en la consola de Python:

```python
>>> 355/113
3.1415929203539825
```

### Pydoc

Pydoc es una aplicación para mirar la mirar documentación. La cual se ejecuta en la terminal del sistema operativo. Pydoc tiene dos modos de operación:
    
* Puede mostrar documentación de un paquete o módulo en especifico.
    ```
    python3 -m pydoc math
    ```
* Puede iniciar un servidor web.
    ```
    python3 -m pydoc -b
    ```

### Import packages from the standard library
Las dos variaciones mas comunes son:
* import x
* from x import y, z

La primera versión importa el módulo completo y crea el módulo como un objeto en el *namespace*. Para poder utilizar clases o funciones se debe de utilizar *x.math(), x.sin()*.

La segunda versión también importa el módulo, pero solo introduce los nombres seleccionados al *namespace*.

### Python Package Index - PyPI

Desarrolladores pueden registrar sus módulos de Python en PyPI. [PyPI](https://pypi.python.org)


## Core Python Programming 2nd Edition Wesley Chun

```
raw_input(...)
    raw_input([prompt]) -> string
    
    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading.
```

``` Python
num = raw_input('Introduzca un numero: ')
print('El doble del numero : %d' % (int(num) * 2 ))
```

Se utiliza la función *int* ya que es necesario convertir la variable *num* en entero para poder realizar la operación.

```
class int(object)
Convert a number or string to an integer, or return 0 if no arguments are given. If x is floating point, the conversion truncates towards zero. If x is outside the integer range, the function returns a long instead. 
 
If x is not a number or if base is given, then x must be a string or Unicode object representing an integer literal in the given base.The literal can be preceded by '+' or '-' and be surrounded by whitespace. The base defaults to 10. Valid bases are 0 and 2-36. Base 0 means to interpret the base from the string as an integer literal. 
>>> int('0b100', base=0)

```
### Core Style: Keep user interaction outside of functions

Las funciones deberán de mantenerse "limpias", estas deberán de ser usadas solamente para tomar parámetros y proveer resultados. La excepción a esta regla es si se crean funciones especializadas para obtener información del usuario o para mostrar información. **Como buena practica es recomendable separadas funciones en dos categorías:**

* Funciones que realizan( Interactúan con el usuario)
* Funciones que calculan (usualmente regresan resultados)
 ### Comments

 El comentario *Documentation string* también llamado *doc string* puede agregar comentario al inicio de un módulo, clase o función. Ademas, a diferencia de los comentarios comunes *doc strings* pueden ser accedidos en tiempo de ejecución.


### List, Tuples and Dictionaries

Listas y tuplas pueden ser vistas como arreglos con los cuales se pueden almacenar un numero arbitrario de objetos. Los valores almacenados en estos arreglos pueden ser accedidos mediante el índice.
* Listas **[ ]**. Sus elementos y tamaño pueden cambiar.
* Tuplas **( )**. Sus elementos no pueden ser actualizados
* Dictionaries **{}**. Funcionan como matrices asociativas o hashes.Están formados por pares *Key-Value*.
