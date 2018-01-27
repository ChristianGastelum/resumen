# Implementing Domain-Driven Design by Vaughn Vernon
        
## Author: Christian Eder Gastélum Reyes

> We strive to produce quality in the software we develop. We achieve some quality by using test to help us avoid delivering software with a fatal number of bugs. Yet, even if we could produce completely bug-free software, that in itself does not necessarily mean that a quality software model is designed.   *The software model—the way the software expresses the solution to the business goal being sought—could still suffer greatly*

 ### Chapter 1. Getting Started With DDD

Los fundamentos principales de DDD están basados en la discusión, escuchar, entendimiento, descubrimiento, y valores de negocio, todo esto para poder centralizar el conocimiento. Si eres capaz de *entender el negocio* en el cual se basará, por lo menos podrá participar en el modelado del software y podrá participar en  el proceso de crear el  **lenguaje ubicuo**. (ubicuo. Está presente a un mismo tiempo en todas partes)
 

 Durante este proceso de creado del **lenguaje ubicuo** es necesario entablar conversaciones con *expertos del dominio*.
Los *expertos del dominio* son aquellos que conocen como funciona el negocio. Un * experto del domino*  no esta basado en  "títulos". Ya que, existen personas que conocen su area de negocio bastante bien. Por lo tanto, ellos pueden proveer información vital para el **lenguaje ubicuo**.

#### ¿Qué es un modelo del dominio?
Es un modelo basado en software, el cual esta basado en un dominio de negocio. También considerado como *modelo objeto*, donde existen objetos, los cuales tienen datos y comportamientos en base al negocio. Crear un *modelo del domino* es esencial para poder utilizar DDD. Utilizando DDD los *modelos del dominio* tienden a ser pequeños y enfocados.

#### ¿Por qué se debería utilizar DDD? 

- Permitir que los  expertos del dominio y desarrolladores trabajen en conjunto, lo cual producirá  un software que este basado  en el negocio. 
-  Centralizar el conocimiento es clave, porque con esto la empresa es capaz de garantizar la comprensión del software.
- > The design is the code, and the code is the design. 
- DDD provee técnicas de desarrollo de software, las cuales se encargan del diseño estratégico y táctico. **Diseño estratégico** ayuda a entender cuales son las inversiones que se tiene realizar con el software, que tipo de software existe para poder obtener un software rápido y seguro. **Diseño táctico** ayuda a desarrollar un solo *modelo de la solución*.

#### Aspectos principales  de DDD
1. Acerca a los expertos del dominio y desarrolladores para trabajar en conjunto para reflejar el modelo mental del experto. Al trabajar juntos los expertos del dominio y desarrolladores su principal objetivo es crear un lenguaje ubicuo. Este lenguaje permitirá tener una mejor comunicación y un mayor entendimiento  sobre el dominio del negocio.
2. DDD aborda las iniciativas estratégicas de la empresa.  Aunque DDD incluya técnicas de análisis, esta mas enfocado con la estrategia  de dirección de la empresa. Los aspectos técnicos de la estrategia del diseño tiene como objetivo crear *bounding system* y preocupaciones de negocios.
3. Tácticas de diseño permiten a los desarrolladores  producir un software que  esta correctamente codificado en base a los conocimientos de los expertos del  dominio,  es escalable, y permite cómputo distribuido. 


#### Grapping with the Complexity of your Domain

Primordialmente se debe de utilizar DDD en areas esenciales del negocio. *You invest in the nontrivial, the more complex stuff, the most valuable and important stuff that promises to return the greatest dividends*. Por esta razón se le llama *Core domain*. Este  y sus sub dominios son a los cuales se debe de enfocar  toda la atención. 

#### Bounded Context
Is un límite conceptual alrededor de una aplicación o un sistema finito. La razón detrás de este límite es acentuar que cada término, frase u oración (lenguaje ubicuo) dentro del dominio tiene un significado específico. 


#### Ubiquitous Language

El lenguaje ubicuo es un lenguaje compartido por un equipo que trabaja dentro de un dominio. El lenguaje esta enfocado en como se maneja el negocio y como opera.
![Lenguaje Universal](https://github.com/KillLoGiC/resumen/blob/master/images/lenguajeUniversal.PNG)

#### How do you capture this all-important Ubiquitous Language?

- Dibujar el modelo físico y conceptual, adicionalmente etiquetarlo con nombres y acciones. Estos dibujos son principalmente informales pero pueden contener aspectos formales de modelado. Al inicio del modelo es mejor evitar utilizar UML para evitar complicaciones.
- Crear un glosario de terminos con definiciones simples. Agregar termines alternativos, incluir opciones adicionales 

> *In the end it is team speech and the model in the code that are the most enduring and the only guaranteed current denotations of the Ubiquitous Language*

**El modelo del software incorpora sustantivos, adjetivos, verbos y expresiones formales**. 

#### Basic concepts of Ubiquitous Language:
- Ubicuo significa que se encuentra en todos lados, tal como se habla entre el equipo y expresado en un mismo dominio.
- El lenguaje ubicuo esta limitado a un contexto dentro de un dominio.
- Pueden haber multiples límites contextuales los cuales son integrados por *mapas contextuales*, cada uno de estos tiene su propio lenguaje ubicuo, y algunos terminos coincidir. 


#### Value and benefits of DDD 

1. Organizaciones ganan un modelo útil de su dominio.
    
    El objetivo de DDD es invertir todos los esfuerzos en lo que importa más del negocio. Se enfoca en el dominio central (*Core domain*). Otros modelos existen para dar soporte al dominio central.
2. Una definición refinada y precisa del negocio es desarrollado.
    
    Cuando el modelo es refinado una y otra vez, se desarrolla  un mejor entendimiento  el cual se puede utilizar como herramienta de análisis. 
3. Expertos del dominio contribuyen al diseño del software. 
    
    Cuando los expertos comparten sus conocimientos entre ellos, permite crear un mejor entendimiento del negocio. Esto, ayuda a el crecimiento de la empresa. Adicionalmente, los desarrolladores comparten un lenguaje ubicuo con los expertos. 
4. Mejor experiencia de usuario.
    
    Usualmente, la retroalimentación del usuario puede transformarse en un mejor reflejo del modelo del dominio. Cuando el software deja mucho al entendimiento del usuario, los usuarios necesitan ser entrenados para poder utilizarlo. En esencia, el usuario solo transfiere su entendimiento del software a datos, los cuales son introducidos al software. Estos datos son guardados. Sí el usuario no entiende exactamente que  es lo que necesita introducir, entonces, los resultados no son los correctos. 
5. Los limites son claros, los cuales son planteados alrededor de los modelos.
    
   Los desarrolladores son  orientados a utilizar  un enfoque  de negocio.  
6. La arquitectura empresarial es mejor organizada.
    
    Cuando los limites del contexto son bien definidos y cuidadosamente particionados, todos los equipos  tienen un  claro entendimiento  de *donde* y  *por que* las integraciones son necesarias. Los limites son  explícitos,  y las relaciones entre ellos también. 
7. Ágil, iterativo(repetitivo), modelado continuo es usado.
    
    El objetivo de DDD es refinar el modelo mental de los expertos del dominio a un modelo útil para el negocio.
8. Nuevas herramientas, estratégica y tácticas, son utilizadas.
    
    El limite contextual da al equipo limites de modelado en donde se crea una solución para un problema especifico en el dominio. Dentro de un limite contextual un lenguaje ubicuo es creado. Este, es utilizado por el equipo y en el modelo del software. Dentro de un limite de modelado pueden utilizar tácticas: *Aggregates, Entidades, Objeto Valor, Servicios, Eventos del Dominio, entre otros*.


**Un dominio es modelado a través de software, por lo que es necesario tener cuidado que objeto realiza que**. Esto se trata de diseñar el comportamiento de los objetos. Si, es necesario que los comportamientos sean llamados apropiadamente de acuerdo al lenguaje ubicuo. Cada comportamiento de los objetos debe ser considerado.

### Chapter 2. Domains, Subdomains, and Bounded Contexts

Un Dominio a grandes rasgos es *que es lo que hace la organización y en que mundo lo hace*. Cuando se desarrolla un software para una empresa, se esta trabajando en su dominio. El dominio de una empresa esta compuesta de subdominios Cuando se desarrolla un software para una empresa, se esta trabajando en su dominio. El dominio de una empresa esta compuesta de subdominios.

#### Subdomains and Bounded Contexts at Work

Caso de estudio.
> Una tienda al por menor(*retail*) vende productos en linea. Los productos pueden ser cualquier cosa. Para realizar negocios en este dominio, la compañía  debe de  presentar un catálogo de productos a los clientes, debe de permitir realizar ordenes, debe de recibir pagos de los productos vendidos, y debe de hacer el envió de los productos comprados.

El dominio de esta empresa tiene cuatro subdominios:
- Catálogo de productos
- Ordenes
- Facturación
- Envíos

![Un dominio con subdominio y limite de contextos](ttps://github.com/KillLoGiC/resumen/blob/master/images/dominioSubdominio.png)
