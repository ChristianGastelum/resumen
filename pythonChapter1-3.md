# **Resumen de capitulos 1-3 de Python**
## Operadores
* Suma +
* Resta -
* Multiplicacion *
* Division /
* Exponenciacion **
* Operador de Bits XOR ^

Los operadores <<,>>, &, |, y ^ son operadores de bits. Esto es, pueden ser utilizados con numeros. Pero estos son tratados como un *string* de bits, escritos en binario. [Pagina de Operador de bit](https://wiki.python.org/moin/BitwiseOperators)

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
* & Realiza un *AND* de bit. Por cada bit en el output es 1 si corresponden los bits de *X* y los de *Y*, de lo contrario regresa 0.
* | Realiza un *OR* de bit. Por cada bit en el output es 0 si corresponden los bits de *X* y los de *Y*, de lo contrario regresa 1.
* ~ Realiza el complmento de X.
* ^ Realiza el exclusivo *OR*. Si cada bit en el output es el mismo que el correspondiente bit en *X* y *Y* es 0, y es el complemento del bit en *X* y en ese bit en *Y* es 1.

## Think Python, 2nd Edition

Los lenguajes de programacion son lenguajes formales. Los cuales son disenados para una aplicacion en especifico. Un ejemplo de esto, es la notacion matematica y el lenguaje para representar las estructuras de las moleculas. 
Los lenguajes formales tienden a tener una serie de reglas de sintaxis. Las reglas de sintaxis se pueden ver en dos formas **toquens** y **estructura**. Tokens son elementos basicos del lenguaje, como palabras, numeros. Uno de los problemas con la expresion  **3+ = 3 % 6** es que **%**no es un toquen legal. La segunda regla es la forma en que los toquens son combinados.

**Parsing** es la accion de leer una oracion, donde tienes que decifrar la estructura.
