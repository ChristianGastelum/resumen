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



* &
* |
* ^
## Think Python, 2nd Edition

