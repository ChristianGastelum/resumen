# Domain Driven Design

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


| Interfaz de Usuario(*Capa de Presentación*)|  Capa de Aplicación|  Capa del Dominio|  Capa de Infraestructura|
|:----------|:---------------|:-------------|:--------------|
|Responsable de presentar información al usuario e interpretar comandos del usuario. |Coordina la actividad de la aplicación. Ademas no contiene la lógica del negocio. Por ultimo, puede mantener el estado de las tareas en progreso. |Contiene información del dominio. El estado de los objetos es mantenido aquí. | Actúa como la librería de las otras capas. Provee **comunicación entre capas, implementa persistencia en los objetos, contiene librerías para la interfaz de usuario, etc.**  |


Es importante dividir una aplicación en capas, y establecer reglas de interacción entre ellas. *Capa del Dominio* deberá enfocarse únicamente a problemas del dominio. No deberá involucrarse con actividades de infraestructura. 

Un ejemplo típico sobre la interacción entre capas:
> El usuario desea reservar un vuelo, y utiliza un servicio que se encuentra en la * capa de aplicación*. La aplicación obtiene los objetos de dominio de la capa de infraestructura e invoca métodos en ellos. Una vez que los objetos del dominio hayan realizado todas las validaciones , la aplicación manda los cambios a la capa de infraestructura.


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

Es mejor si se almacena la dirección en un objeto por separado, y el objeto cliente almacena una referencia de este objeto. Los atributos Calle, ciudad y estado deben de tener un objeto para ellos, ya que pertenecen juntos conceptualmente.


![imagen](https://github.com/killlogic/resumen/blob/master/images/Sketch.png)

## Services

Durante el análisis del dominio, es posible encontrarse con algunos aspectos que no son fáciles de convertir en objetos. **Los objetos, por lo general, contienen atributos y un estado, éste ultimo, se utiliza para administrar el objeto y  mostrar su comportamiento**. Cuando se desarrolla el *ubiquitous language*, se introducen conceptos claves del dominio, como los *sustantivos*. Los *verbos* los cuales se asocian con sus correspondientes *sustantivos* y son utilizados como parte del comportamiento de los objetos. Aunque, en algunas ocasiones algunos verbos no pertenecen a ningún objeto. Estos, representan un comportamiento importante del dominio. Por ejemplo:

> Para transferir dinero de una cuenta a otra; la función debería estar en la cuenta que envía o en la que recibe. La función no debería estar en ninguna de las dos.

Lo mejor es declararla como *Servicio*. Los objetos que no cuentan con *estado*, solo tienen el propósito de proveer funcionalidad al dominio. Estos servicios pueden ser agrupados, de acuerdo, a las funcionalidades de *entidades* y *value objects*. La declaración de *servicios* ayuda a crear una clara distinción en el dominio, ya que encapsula un concepto. **Los *servicios* actúan como interfaces para proveer operaciones**. Por lo que, un *servicio* usualmente se convierte en un punto de conexión para muchos objetos.

Un *servicio* no debe reemplazar una operación la cual pertenece aun objeto de dominio. Los servicios tienen tres características:

* La operación realizada por un *servicio* se refiere aun concepto del dominio el cual no pertenece a una entidad o *object value*.
* La operación realizada se refiere a otros objectos en el dominio.
* La operación no tiene estado (*stateless*).

 Cuando se utilizan *servicios* es importante mantener * capa del dominio* aislada. Ya que es muy fácil de confundirse entre los servicios de esta capa o de las otras.
Para poder reconocer a que capa pertenecen los servicios se puede utilizar lo siguiente: 
 * Si la operación es realizada conceptualmente pertenece a * capa de aplicación*
 * Si la operación es sobre objetos del dominio, y esta estrictamente relacionado con el dominio, y  satisface una necesidad de este, entonces pertenece a * capa del dominio*.


Ejemplo:
> Una aplicación para reportes. Los reportes utilizan datos almacenados en una base de datos, y estos son generados utilizando una plantilla. El resultado final es una pagina HTML la cual es mostrada en el navegador del usuario.

En este ejemplo la  *capa de interfaz de usuario* es incorporada en las paginas web y permite a los usuarios entrar, y seleccionar el reporte deseado. La *capa de aplicación* se encuentra entre *capa de UI* , el dominio y la infraestructura. La cual interactúa con la base de datos(*capa de infraestructura*) durante las operaciones de acceso, e interactúa con *capa del dominio* cuando es necesario crear reportes. La *Capa del dominio* contiene lo esencial deo dominio, objetos directamente relacionados a los reportes. La *capa de infraestructura* permite el acceso a la base de datos y archivos.

Cuando el usuario selecciona crear un reporte, el selecciona un nombre. Este es un **reportID**, este valor es transferido a través de *capa de aplicación* a *capa del dominio*. La *capa del dominio*  es responsable de crear y regresar el reporte. Ya que, los reportes utilizan plantillas, **un *servicio* puede ser creado, y su función seria obtener la plantilla correspondiente al *reportID***.  Este servicio se localizaría en la *capa del dominio*. Utilizará la capa de infraestructura para retirar las plantillas de los discos duros.


## Modules


Llega un momento cuando el modelo es difícil de describirlo por completo, y entender sus relaciones e interacciones entre sus diferentes partes. Por esta razón, es necesario organizar el modelo en *módulos*. Los módulos son utilizados como métodos de organización en base a conceptos o tareas en orden para reducir complejidad.

Otra razón para utilizar *módulos* es para mejorar la calidad del código. Es altamente aceptable que el código tenga un nivel alto de cohesión  y bajo nivel de acoplamiento. Aunque la cohesión inicia en el nivel de clases y métodos. Es recomendable agrupar clases relacionadas  en módulos para mejorar el nivel de cohesión. Existen varios tipos de cohesión. Los dos tipos más usados son:
* Cohesión comunicacional. Es alcanzada cuando las partes de un modulo operan en los mismos datos.
* Cohesión funcional. Es alcanzada cuando las partes de un modulo trabajan en conjunto para realizar una tarea bien definida.

Los módulos deberán de estar hechos de elementos, los cuales tengan su funcionalidad o lógica  unidas, lo cual asegura cohesión. Los módulos deberán de tener interfaces bien definidas, las cuales permitirán acceder a otros módulos. 

***Como regla de oro: Escoge módulos que cuentan una historia del sistema y contenga un conjunto de concepto con cohesión***.


## Aggregates

Los Objetos del dominio tienen un conjunto de estados durante su ciclo de vida. En donde, son creados, asignados a memoria, usados y luego destruidos. Este ciclo de vida si no es apropiadamente administrado puede tener un impacto negativo en el modelo del dominio. *Aggregate* es un patrón de diseño del dominio, el cual es utilizado para definir propiedad(*ownership*) y limites.

Existen varios tipos de relaciones:
* uno a uno 
* uno a muchos 
* muchos a muchos 

 El número de relaciones debe ser reducido todo lo posible.

1. Relaciones las cuales no son esenciales para el modelo deberán ser removidas.
2. Multiplicidad puede ser reducida al agregar restricciones.
3. En muchas ocasiones relaciones bilaterales pueden ser transformadas en relaciones simples. Ejemplo:
> Cada automóvil tiene un motor, y cada motor tiene un automóvil donde funciona. 

Esto puede ser solucionado fácilmente considerando que los automóviles tienen un motor, no de la otra manera.

> Un sistema bancario mantiene y procesa datos de sus usuarios. Estos datos incluyen datos personales, como nombre, dirección, teléfono, y datos de cuenta: numero de cuenta, balance, etc.. Cuando el sistema almacena o elimina información acerca del cliente, necesita estar seguro que todas las relaciones hayan sido eliminadas.

Si muchos objetos mantienen tales referencias, es difícil de asegurar que sean eliminadas.

Las *invariantes* son aquellas reglas las cuales tienen que ser satisfechas cuando los datos cambian.

*Aggregate* es un grupo de objetos asociados, los cuales son considerados como una unidad considerando el cambio de datos.*Aggregate* separa utilizando límites (*boundary*), los cuales separan los objetos internos de los externos. Cada *aggregate* tiene una raíz. La raíz es una entidad, y es el único objeto accesible desde el exterior. La raíz puede mantener referencias a otros objetos *aggregate*, pero los objetos externos solo pueden mantener referencias hacia el objeto raíz. 

### ¿Cómo es que *aggregate* asegura la integridad de datos y ejecutan las reglas invariantes?
Ya que otros objetos pueden mantener referencias solamente a la raíz, esto significa que estos objetos pueden cambiar directamente a los objetos dentro de *aggregate*. Lo único que pueden hacer es cambiar la raíz, o decir a la raíz que realice ciertas acciones. La raíz es capas de cambiar otros objetos, pero esa operación es contenida dentro de *aggregate* y es controlable.


Si los objetos de *aggregate* son almacenados dentro de una base de datos, solo la raíz deberá ser obtenida mediando consultas.

La entidad raíz es tiene una identidad global, y es responsable de mantener las invariantes. Entidades internas solo tienen identidad local.

Un ejemplo de agregación:
> El cliente es la raíz de *aggregate*, y todos los otros objetos son internos. Si la dirección es necesitada, una copia puede ser dada a los objetos externos.


![aggregate](https://github.com/KillLoGiC/resumen/blob/master/images/aggregate.png)

## Factories

Cuando un objeto del cliente quiere crear otro objeto, llama al constructor y posiblemente da parámetros. Pero, cuando la construcción de un objeto es laborioso, la creación de un objeto involucra tener conocimiento de la estructura interna, y las relaciones de los objetos internos y sus reglas. Esto significa que cada objeto del cliente necesita mantener información sobre el objeto construido. Si el cliente pertenece a la capa de aplicación, una funcionalidad de la capa del dominio es movida fuera de esta, esto puede tener grandes repercusiones.

*Fabricas* son utilizadas para encapsular el conocimiento necesario para crear objetos, ademas, se pueden utilizar para crear *aggregates*. 

Hay diferentes formas de implementar:
* Factory method.
    Es un objeto el cual contiene y esconde el conocimiento necesario para crear otro objeto. Esto es útil cuando el cliente quiere crear un objeto el cual pertenece a un *aggregate*. La solución  es agregar un metodo a la raiz de *aggregate*, la cual se encarga de la creacion del objeto, imponen las reglas invariantes, y regresan una referencia al objeto, o una copia. 

![factories](https://github.com/KillLoGiC/resumen/blob/master/images/factories.png)

El 


    
* Abstract Factory.





### Simple factory pattern
```Python 
from abc import ABCMeta, abstractmethod
 
class Animal(metaclass = ABCMeta):
    @abstractmethod
    def do_say(self):
         pass
 
 
class Dog(Animal):
    def do_say(self):
       print("Bhow Bhow!!")

 
class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


##Forest factory defined
class ForestFactory(object):
    def make_sound(self,object_type):
        return eval(object_type)().do_say()

#client code 
if __name__ == '__main__':
  ff = ForestFactory()
    animal = input("cat or dog")
    ff.make_sound(animal)
```
