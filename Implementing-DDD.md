# Implementing Domain-Driven Design by Vaughn Vernon
        
## Author: Christian Eder Gastélum Reyes

> We strive to produce quality in the software we develop. We achieve some quality by using test to help us avoid delivering software with a fatal number of bugs. Yet, even if we could produce completely bug-free software, that in itself does not necessarily mean that a quality software model is designed.   *The software model—the way the software expresses the solution to the business goal being sought—could still suffer greatly*

### Chapter 1. Getting Started With DDD

Los fundamentos principales de DDD están basados en la discusión, escuchar, entendimiento, descubrimiento, y valores de negocio, todo esto para poder centralizar el conocimiento. Si eres capaz de *entender el negocio* en el cual se basará, por lo menos podrá participar en el modelado del software y podrá participar en  el proceso de crear el  **lenguaje universal**.

 Durante este proceso de creado del **lenguaje universal** es necesario entablar conversaciones con *expertos del dominio*.
Los *expertos del dominio* son aquellos que conocen como funciona el negocio. Un * experto del domino*  no esta basado en  "títulos". Ya que, existen personas que conocen su area de negocio bastante bien. Por lo tanto, ellos pueden proveer información vital para el **lenguaje universal**.

#### ¿Qué es un modelo del dominio?
Es un modelo basado en software, el cual esta basado en un dominio de negocio. También considerado como *modelo objeto*, donde existen objetos, los cuales tienen datos y comportamientos en base al negocio. Crear un *modelo del domino* es esencial para poder utilizar DDD. Utilizando DDD los *modelos del dominio* tienden a ser pequeños y enfocados.

#### ¿Por qué se debería utilizar DDD? 

- Permitir que los  expertos del dominio y desarrolladores trabajen en conjunto, lo cual producirá  un software que este basado  en el negocio. 
-  Centralizar el conocimiento es clave, porque con esto la empresa es capaz de garantizar la comprensión del software.
- > The design is the code, and the code is the design. 
- DDD provee técnicas de desarrollo de software, las cuales se encargan del diseño estratégico y táctico. **Diseño estratégico** ayuda a entender cuales son las inversiones que se tiene realizar con el software, que tipo de software existe para poder obtener un software rápido y seguro. **Diseño táctico** ayuda a desarrollar un solo *modelo de la solución*.

#### Aspectos principales  de DDD
1. Acerca a los expertos del dominio y desarrolladores para trabajar en conjunto para reflejar el modelo mental del experto. Al trabajar juntos los expertos del dominio y desarrolladores su principal objetivo es crear un lenguaje universal. Este lenguaje permitirá tener una mejor comunicación y un mayor entendimiento  sobre el dominio del negocio.
2. DDD aborda las iniciativas estratégicas de la empresa.  Aunque DDD incluya técnicas de análisis, esta mas enfocado con la estrategia  de dirección de la empresa. Los aspectos técnicos de la estrategia del diseño tiene como objetivo crear *bounding system* y preocupaciones de negocios.
3. Tácticas de diseño permiten a los desarrolladores  producir un software que  esta correctamente codificado en base a los conocimientos de los expertos del  dominio,  es escalable, y permite cómputo distribuido. 


#### Grapping with the Complexity of your Domain

Primordialmente se debe de utilizar DDD en areas esenciales del negocio. *You invest in the nontrivial, the more complex stuff, the most valuable and important stuff that promises to return the greatest dividends*. Por esta razón se le llama *Core domain*. Este  y sus sub dominios son a los cuales se debe de enfocar  toda la atención. 

#### Bounded Context
Is un límite conceptual alrededor de una aplicación o un sistema finito. La razón detrás de este límite es acentuar que cada término, frase u oración (lenguaje universal) dentro del dominio tiene un significado específico. 


#### Ubiquitous Language

El lenguaje universal es un lenguaje compartido por un equipo que trabaja dentro de un dominio. El lenguaje esta enfocado en como se maneja el negocio y como opera.
