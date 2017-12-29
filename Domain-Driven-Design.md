# Domain Driven Design

## 3 Model Driven Design
Es de fundamental importancia crear un modelo que se encuentre fuertemente arraigado al dominio, el cual deberá reflejar los conceptos esenciales del dominio con gran exactitud.

El lenguaje *Oblicuo* deberá ser utilizado durante el proceso de modelado para facilitar la comunicación entre especialistas del dominio y desarrolladores del software.

### ¿Cómo se debe de realizar la transición del modelo a código?

El modelo deberá ser construido teniendo en cuenta las consideraciones de diseño y software. Esto, con el propósito de diseñar un modelo el cual puede ser expresado apropiadamente en software. Para esto, es necesario que los desarrolladores sean involucrados en el desarrollo del modelo. En otras palabras, aquellos que se encarguen de desarrollar el código deberán conocer el modelo, y deberán sentirse responsables por su **integridad**. Éstas personas deberán de tener en cuenta que al realizar un cambio en el código tiene implicaciones en el modelo, de lo contrario, podrían modificar el código hasta que ya no tenga relación con el modelo. 

La programación orientada a objetos es utilizada para la implementación del modelo, ya que ambos están basados en el mismo paradigma.  OOP  provee clases de objetos y asociaciones de clases, instancias de objetos, y mensajes entre ellos.


### Layered Architecture

![Imagen](~/Pictures/screenshot_20171228_142937.png)
Cuando se crea una aplicación de software, una gran parte de la aplicación no esta directamente relacionada con el dominio, pero es parte de la misma infraestructura o los servidores.
