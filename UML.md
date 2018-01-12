# Teach Yourself UML in 24 Hours

## Part I Getting Started

### Hour 1 Introducing the UML

El propósito de los diagramas es presentar múltiples puntos de vista de un sistema; este conjunto se llama **modelo**.  Un modelo es un conjunto de diagramas UML que pueden ser examinados, evaluar y modificar para poder entender y desarrollar un sistema.

#### Class Diagram 

Una **clase** es una categoría o un grupo de cosas que tienen el mismo atributo y el mismo comportamiento. **El rectangulo es el icono que representa una clase**.

> Cualquier cosa dentro de la clase *lavadoras* tiene atributos como marca, modelo, numero de serie, capacidad, etc.. Comportamientos de las cosas en esta clase incluyen las funciones: "aceptar ropa", "aceptar detergente", "encendido" y "apagado".


![clase](https://github.com/KillLoGiC/resumen/blob/master/images/clase.png)

Nótese el espacio entre el nombre de la clase, atributos, y funciones. Adicionalmente, en UML el nombre de una clase inicia con mayúscula. Atributos y funciones, la primera letra de su nombre inicia con minúscula. 

#### Object Diagram 

Un **objeto** es una instancia de una clase, es una cosa especifica la cual tiene valores específicos de los atributos de la clase. Un *objecto* se representa con un rectángulo y su nombre es subrayado.

> Una lavadora puede tener una marca Mabe, un modelo 834nx, numero de serie 971029384 y una capacidad 20 kg.

![objeto](https://github.com/KillLoGiC/resumen/blob/master/images/objeto.PNG)

El nombre de la instancia inicia con minúscula. El nombre de la izquierda de los dos puntos es el nombre de la instancia y el de la derecha es el nombre de la clase. Adicionalmente, es posible tener un objeto anónimo, como se muestra en la instancia de la derecha.


#### Use Case Diagram 

Un **uso de caso** es una descripción del sistema desde el punto de vista del usuario.

![caso de uso](https://github.com/KillLoGiC/resumen/blob/master/images/casodeusp.PNG)

La figura corresponde al usuario o **actor**. La elipse representa el **caso de uso**. El actor( la entidad que inicializa el caso de uso ) puede ser una persona u otro sistema.


#### State Diagram 

En cualquier momento, un objeto puede tener un **estado**. 

![estado](https://github.com/KillLoGiC/resumen/blob/master/images/estado.PNG)

#### Sequence Diagram 

Los diagramas de clase y objetos representan información estática. El **diagrama de secuencia** muestra las interacciones.

> Utilizando el ejemplo de las lavadoras, los componentes de la lavadora incluye: una alarma, tubería de agua, tambor girador. Estos son objetos.

¿Qué pasa cuando se invoca  el *uso de caso* "lavar ropa"?. Asumiendo que ya se completaron las funciones "añadir ropa", "añadir detergente" y "encendido".

1. Al inicio de "remojado", el agua entra al tambor utilizando la tubería del agua.
2. El tambor permanece estacionario por 5 minutos.
3. AL final de "remojado", se deja de añadir agua.
4. Al inicio de "lavado", el tambor empieza a moverse por 15 min.
5. Al final de "lavado", el tambor desecha el agua.
6. El tambor deja de girar.
7. Al inicio de "enjuagado", se añade agua.
8. El tambor inicia su movimiento
9. Después de 15 min. ya no se vierte mas agua.
10. Al final de "enjuagado", el tambor desecha el agua.
11. El tambor deja de girar.
12. Al inicio de "secado", el tambor gira por 5 min.
13. Al final de "secado", el tambor deja de girar.
14. La ropa esta limpia. 

Suponiendo que alarma, tubería de agua, y tambor son objetos. Asumiendo que cada objeto tiene una o mas funciones. Los objetos trabajan juntos mandándose mensajes. Cada mensaje es una perdición  *sender-objetct* a *receiver-object*. 

- **Alarma** puede tener las siguientes funciones:
    - Tiempo para remojado
    - Tiempo para lavado 
    - Tiempo para enjuagado
    - Tiempo para secado

- **Tubería de agua**:
    - Verter agua 
    - Detener flujo del agua.

- **Tambor**:
    - Almacenar agua 
    - Girar hacia adelante y hacia atrás
    - Girar según las manecillas del reloj
    - Detener rotación
    - Bombear agua 

En el diagrama que se presenta en la siguiente sección, se muestra como se utilizan estas funciones para crear un **diagrama  de secuencia**. 


#### Activity Diagram 

Las actividades que ocurren dentro de un *caso de uso* o dentro de comportamiento de un objeto típicamente ocurre en secuencia.


#### Communication Diagram 

Los elementos de un sistema trabajando en conjunto para alcanzar los objetivos del sistema. Se utiliza el *diagrama de secuencia* para realizar esa tarea.


![Diagrama de Secuencia](https://github.com/KillLoGiC/resumen/blob/master/images/diagramaDeSecuencia.PNG)

#### Deployment Diagram 

El diagrama de despliegue muestra la arquitectura física. Puede representar computadoras, y sus conexiones entre ellas, también, muestra el software utilizado en estas. Cada computadora es representada por un **cubo**.

![Diagrama de Despliegue](https://github.com/KillLoGiC/resumen/blob/master/images/deployDiagram.PNG)

#### Interface

Una interfaz es una clase que solo tiene funciones y no tiene atributos. Es un conjunto de comportamientos que se desea utilizar en múltiples ocasiones. UML utiliza el icono de clase con la palabra clave **<< Interfaz >>**.

#### Stereotypes

Los estereotipos permiten crear elementos basados en otros ya existentes. Se puede pensar como un tipo de alteracion de un elemento para generar otro.

#### Dictionaries

Los diccionarios permiten mantener un registro de todos los elementos creados en un modelo: clases, casos de uso, componentes, entre otros. Los diccionarios solo pueden trabajar con elementos ya existentes y con estereotipos basados en estos elementos.


### Hour 2 Understanding Object-Orientation

Un **objeto** es una instancia de una **clase**. Un objeto tiene una **estructura**. Osea, tiene **atributos** (propiedades) y comportamientos. Un comportamiento de un objeto consiste de **funciones**. **Atributos** y **funciones** juntos son llamados **caracteristicas**. 

> Como objetos en la clase *Personas*, cada uno tiene estos atributos: altura, peso, y edad. Además, realizamos las siguientes operaciones: comer, dormir, leer, escribir, hablar, entre otros.


Una clase es una plantilla para crear objetos.


#### Abstractioon

Abstracción significa, filtrar las propiedades y operaciones de objetos, hasta que queden las necesarias.

#### Inheritance

Lavadoras, refrigeradores, microondas son aparatos electrodomésticos. Se podría decir que, estos son una *subclase* de la clase *aparatos electrodomésticos*. **Las subclases heredan las propiedades de la clase, adicionalmente, tiene que tener sus propios atributos y funciones**.

#### Polimorphism

En algunas ocasiones, en diferentes clases pueden existir funciones con el mismo nombre.


#### Encapsulation

Cuando un objeto realiza sus funciones y estas funciones son escondidas.

#### Associations

Esto sucede cuando un objeto esta relacionado con otros de alguna forma.

#### Aggregation

Agregación involucra una fuerte relación entre los objetos.

##### Composition

Una composición existe cuando un componente cuando están dentro de un objeto compuesto.

> Una camisa esta compuesta por: cuerpo, cuello, mangas, botones. Si quitamos el cuerpo el cuello se vuelve inservible. 



