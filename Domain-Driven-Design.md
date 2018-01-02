#Domain Driven Design

## 3 Model Driven Design
Es de fundamental importancia crear un modelo que se encuentre fuertemente arraigado al dominio, el cual deberá reflejar los conceptos esenciales del dominio con gran exactitud.

El lenguaje *Oblicuo* deberá ser utilizado durante el proceso de modelado para facilitar la comunicación entre especialistas del dominio y desarrolladores del software.

### ¿Cómo se debe de realizar la transición del modelo a código?

El modelo deberá ser construido teniendo en cuenta las consideraciones de diseño y software. Esto, con el propósito de diseñar un modelo el cual puede ser expresado apropiadamente en software. Para esto, es necesario que los desarrolladores sean involucrados en el desarrollo del modelo. En otras palabras, aquellos que se encarguen de desarrollar el código deberán conocer el modelo, y deberán sentirse responsables por su **integridad**. Éstas personas deberán de tener en cuenta que al realizar un cambio en el código tiene implicaciones en el modelo, de lo contrario, podrían modificar el código hasta que ya no tenga relación con el modelo. 

La programación orientada a objetos es utilizada para la implementación del modelo, ya que ambos están basados en el mismo paradigma.  OOP  provee clases de objetos y asociaciones de clases, instancias de objetos, y mensajes entre ellos.


### Layered Architecture

![Imagen](https://github.com/KillLoGiC/resumen/blob/master/images/screenshot_20171228_142937.png "")

Cuando se crea una aplicación de software, una gran parte de la aplicación no esta directamente relacionada con el dominio, pero es parte de la misma infraestructura o los servidores.

Cuando se desarrolla un software complejo es recomendable dividirlo en **capas**, por lo que al desarrollar dentro de estas se tiene una mayor coherencia en las dependencias de las capas inferiores.

El siguiente patrón de arquitectura trata de proveer acoplamiento ligero (*loose coupling*). ***Concentrar todo el código relacionado al modelo del dominio en una capa y aislarlo de la interfaz de usuario, aplicación, y infraestructura***. 

Los **objetos de dominio** son libres de responsabilidad de mostrarse, almacenarse, administración de tareas de aplicación, lo cual permite enfocarse a expresar el modelo de dominio.


| User Interface (*Presentation Layer*)| Application layer| Domain Layer| Infraestructure Layer|
|:----------|:---------------|:-------------|:--------------|
|Responsable de presentar información al usuario e interpretar comandos del usuario. |Coordina la actividad de la aplicación. Ademas no contiene la lógica del negocio. Por ultimo, puede mantener el estado de las tareas en progreso. |Contiene información del dominio. El estado de los objetos es mantenido aquí. | Actúa como la librería de las otras capas. Provee **comunicación entre capas, implementa persistencia en los objetos, contiene librerías para la interfaz de usuario, etc.**  |


Es importante dividir una aplicación en capas, y establecer reglas de interacción entre ellas. *Domain Layer* deberá enfocarse únicamente a problemas del dominio. No deberá involucrarse con actividades de infraestructura. 

Un ejemplo típico sobre la interacción entre capas:
> El usuario desea reservar un vuelo, y utiliza un servicio que se encuentra en la *application layer*. La aplicación obtiene los objetos de dominio de la capa de infraestructura e invoca métodos en ellos. Una vez que los objetos del dominio hayan realizado todas las validaciones , la aplicación manda los cambios a la capa de infraestructura.


## Entities

Existe una categoría de objetos los cuales tienen una entidad, la cual permanece la misma a través el estado del software. Tales objetos son llamados **entidades**. Ejemplo:

> Si se quisiera implementar el concepto persona, probablemente se crearía una clase Persona con una seria de atributos: nombre, fecha de nacimiento, lugar de nacimiento, etc. **¿Alguno de estos atributos es la identidad de persona?**. 

Nombre, fecha de nacimiento, lugar de nacimiento pueden ser utilizados como identidad, ya que pueden existir múltiples personas con los mismos atributos. **Un objeto debe ser distinguido de otros objetos aunque estos puedan tener los mismos atributos**.


Otro ejemplo seria el sistema de cuentas de un banco:
> Cada cuenta tiene su propio número. Una cuenta puede ser identificada por este número. 

Este número permanece sin cambios a lo largo de la vida del sistema lo cual asegura **continuidad**

Por lo tanto, implementar entidades en software significa crear identidad. Un ejemplo de esto es el numero de seguro social. **Usualmente la identidad puede ser es un atributo de un objeto, una combinación de atributos, un atributo especialmente creado para preservar y expresar identidad o también un comportamiento**. Es importante que dos objetos con diferentes identidades puedan ser identificados fácilmente por el sistema, y dos objetos con la misma identidad ser considerados como el mismo por el sistema. Existen diferentes formas de crear              identidad.

* ID puede ser creada automáticamente por un modulo, y usada internamente.
* Puede ser una llave primaria en una tabla dentro de una base de datos.


Entidades son de suma importancia en el dominio (*domain model*), y estos deberán ser considerados desde el inicio del proceso de modelado del dominio.

## Value Objects

 Entidades son objetos necesarios en el modelo del dominio. ¿Todos los objetos deberían tener una identidad?. Aunque esta opción por más tentadora que parezca, tiene consecuencias, las cuales pueden afectar el modelo del dominio y el rendimiento de la aplicación.

> Una aplicación de dibujo. El usuario puede dibujar cualquier punto y linea de cualquier grosor, estilo y color. Es útil crear una clase de objeto llamado Punto, y el programa pueda crear una instancia de esta clase por cada punto. En el cual, cada punto tendrá dos atributos los que almacenarán las coordenadas de la pantalla y el lienzo. ¿Es necesario que cada punto tenga una identidad?. ¿Tiene continuidad?.

Hay casos donde necesitamos almacenar atributos de un elemento del dominio. Por lo que, no es de mucha importancia que objeto es, sino que atributos tiene. **Un objeto que es usado para describir ciertos aspectos de un dominio, y el cual no tiene identidad, es llamado *Value Object***.

*Value Objects* pueden ser creados y descartados fácilmente. Además, 
es sumamente recomendable que estos objetos sean *inmutables*. Lo cual, permite que sean compartidos, además, de que manifiestan integridad.

> Un sistema de reservaciones de vuelos puede crear objetos para cada vuelo.  Uno de los atributos puede ser el código de vuelo. Un cliente puede reservar un destino. Otro cliente quiere reservar en el mismo vuelo. El sistema decide reusar el objeto, el cual mantiene el código de vuelo, por que es el mismo vuelo.


Una regla de oro: ***Si Value Object puede ser compartido, este debe ser inmutables***. Estos valores pueden contener otros *Value Objects*, y pueden contener referencias a entidades. Atributos pueden ser agrupados en diferentes objetos. Atributos seleccionados para crear un *Value Object* deberán formar un concepto en conjunto.

> Un cliente puede ser asociado con un nombre, calle, cuidad y un estado.

Es mejor si se almacena la dirección en un objeto por separado, y el objeto cliente almacena una referencia de tal objeto. Calle, cuidad y estado deben de tener un objeto para ellos, ya que pertenecen juntos conceptualmente.




![imagen](https://github.com/killlogic/resumen/blob/master/images/Sketch.png)
