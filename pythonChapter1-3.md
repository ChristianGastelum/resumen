# **Resumen de capitulos 1-3 de Python**
## Operadores
* Suma +
* Resta -
* Multiplicacion *
* Division /
* Exponenciacion **
* Operador de Bits XOR ^

Los operadores <<,>>, &, |, y ^ son operadores de bits. Ademas, pueden ser utilizados con numeros. Los cuales son tratados como un *string* de bits, escritos en binario. [Pagina de Operador de bit](https://wiki.python.org/moin/BitwiseOperators)

* X << Y. Regresa *X* con los bits cambiados a la izquierda por *Y* lugares y al lado derecho son ceros. Es lo mismo que multiplicar X * (2 ** Y).

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
* **~** Realiza el complmento de X.
* **^** Realiza el exclusivo *OR*. Si cada bit en el output es el mismo que el correspondiente bit en *X* y *Y* es 0, y es el complemento del bit en *X* y en ese bit en *Y* es 1.

## Think Python, 2nd Edition

Los lenguajes de programacion son lenguajes formales. Los cuales son disenados para una aplicacion en especifico. Un ejemplo de esto, es la notacion matematica y el lenguaje para representar las estructuras de las moleculas. 
Los lenguajes formales tienden a tener una serie de reglas de sintaxis. Las reglas de sintaxis se pueden ver en dos formas **toquens** y **estructura**. Tokens son elementos basicos del lenguaje, como palabras, numeros. Uno de los problemas con la expresion  **3+ = 3 % 6** es que **%**no es un toquen legal. La segunda regla es la forma en que los toquens son combinados.

**Parsing** es la accion de leer una oracion, donde tienes que decifrar la estructura.

## Python Essential

El fundamento para la programacion en Python es **Read-Evaluate-Print Loop** (**REPL**). Aunque se puedan realizar otras tareas es esencialmente lo mismo ya que interactura con *REPL*.

Una expresion por si misma es un declaracion. Mientras que el valor de una expresion no sea *None*, REPL nos mostrata el valor de la expresion. Esta simple expresion nos permite realizar cosas como las siguientes en la consola de Python:

```python
>>> 355/113
3.1415929203539825
```

### Pydoc

Pydoc es una aplicacion para mirar la mirar documentacion. La cual se ejecuta en la terminal del sistema operativo. Pydoc tiene dos modos de operacion:
    
* Puede mostrar documentacion de un paquete o modulo en especifico.
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

La primera version importa el modulo completo y crea el modulo como un objeto en el *namespace*. Para poder utilizar clases o funciones se debe de utilizar *x.math(), x.sin()*.

La segunda version tambien importa el modulo, pero solo introduce los nombres seleccionados al *namespace*.

### Python Package Index - PyPI

Desarrolladores pueden registrar sus modulos de Python en PyPI. [PyPI](https://pypi.python.org)


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

Se utiliza la funcion *int* ya que es necesario convertir la variable *num* en entero para poder realizar la operacion.

```
class int(object)
Convert a number or string to an integer, or return 0 if no arguments are given. If x is floating point, the conversion truncates towards zero. If x is outside the integer range, the function returns a long instead. 
 
If x is not a number or if base is given, then x must be a string or Unicode object representing an integer literal in the given base.The literal can be preceded by '+' or '-' and be surrounded by whitespace. The base defaults to 10. Valid bases are 0 and 2-36. Base 0 means to interpret the base from the string as an integer literal. 
>>> int('0b100', base=0)

```
### Core Style: Keep user interaction outside of functions

Las funciones deberan de mantenerse "limpias", estas deberan de ser usadas solamente para tomar parametros y proveer resultados. La excepcion a esta regla es si se crean funciones especializadas para obtener informacion del usuario o para mostrar informacion. **Como buena practica es recomendable separadas funciones en dos categorias:**

* Funciones que realizan( Interactuan con el usuario)
* Funciones que calculan (usualmente regresan resultados)


### Comments
Existen un tipo especial de comentarios llamados *docstrings* o *string documentales*. Estos comentarios pueden ser agregados al inicio de modulos, clases o funciones. A diferencia de comentarios comunes, *docstrings* pueden ser accesados en tiempo de ejecucion y puede ser usado para generar automaticamente documentacion.