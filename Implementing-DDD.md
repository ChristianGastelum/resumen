# Implementing Domain-Driven Design by Vaughn Vernon
        
## Author: Christian Eder Gastélum Reyes
 
> We strive to produce quality in the software we develop. We achieve some quality by using test to help us avoid delivering software with a fatal number of bugs. Yet, even if we could produce completely bug-free software, that in itself does not necessarily mean that a quality software model is designed.   *The software model—the way the software expresses the solution to the business goal being sought—could still suffer greatly*

 ### Chapter 1. Getting Started With DDD

Los fundamentos principales de DDD están basados en la discusión, escuchar, entendimiento, descubrimiento, y valores de negocio, todo esto para poder centralizar el conocimiento. Si eres capaz de *entender el negocio* en el cual se basará, por lo menos podrá participar en el modelado del software y podrá participar en  el proceso de crear el  **lenguaje ubicuo**. (ubicuo. Está presente a un mismo tiempo en todas partes)
 

 Durante este proceso de creado del **lenguaje ubicuo** es necesario entablar conversaciones con *expertos del dominio*.
Los *expertos del dominio* son aquellos que conocen como funciona el negocio. Un * experto del domino*  no esta basado en  "títulos". Ya que, existen personas que conocen su área de negocio bastante bien. Por lo tanto, ellos pueden proveer información vital para el **lenguaje ubicuo**.

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
5. Los límites son claros, los cuales son planteados alrededor de los modelos.
    
   Los desarrolladores son  orientados a utilizar  un enfoque  de negocio.  
6. La arquitectura empresarial es mejor organizada.
    
    Cuando los límites del contexto son bien definidos y cuidadosamente particionados, todos los equipos  tienen un  claro entendimiento  de *donde* y  *por que* las integraciones son necesarias. Los límites son  explícitos,  y las relaciones entre ellos también. 
7. Ágil, iterativo(repetitivo), modelado continuo es usado.
    
    El objetivo de DDD es refinar el modelo mental de los expertos del dominio a un modelo útil para el negocio.
8. Nuevas herramientas, estratégica y tácticas, son utilizadas.
    
    El límite contextual da al equipo límites de modelado en donde se crea una solución para un problema especifico en el dominio. Dentro de un límite contextual un lenguaje ubicuo es creado. Este, es utilizado por el equipo y en el modelo del software. Dentro de un límite de modelado pueden utilizar tácticas: *Aggregates, Entidades, Objeto Valor, Servicios, Eventos del Dominio, entre otros*.


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

![Un dominio con subdominios y límite de contextos](https://github.com/KillLoGiC/resumen/blob/master/images/dominioSubdominio.png)

Nótese que existen tres sistemas físicos  esenciales para la existencia del dominio del negocio, y solo dos  son internos. 

Estos dos sistemas  representan dos  limités de contexto. 
Dentro del límite de contexto existen múltiples modelos de dominio(catálogo ordenes, facturación, envíos) aunque no estén separados. Estos dominios fueron fusionados dentro de un modelo de software. Lo cual  dificulta agregar nuevas funcionalidades, ya que existen dependencias.
Dentro de las dificultades que presenta una empresa pequeña es el límite de fondos y almacén. La empresa no debe de sobre invertir en productos si no se están vendiendo bien. 

Lo que podría ayudar en un futuro a la empresa seria contar con un sistema que se base en oferta-demanda de artículos basado en tendencias pasadas para poder tenerlos en inventario. Tal sistema de *previsión* podría consistir de un *dominio central*, porque no es un problema simple de resolver, y tenerlo podría establecer una ventaja. **El subdominio de *Ordenes* y  el límite de contexto de *Inventario* integrado con *previsión* podrán proveer historial de ventas**.

En algunas ocasiones un subdominio puede estar conformado de un conjunto de algoritmos. Tales subdominios pueden ser separados del dominio central usando *Módulos*.

Nótese que el límite contextual no necesariamente esta en un subdominio, sino que puede estar en varios.

#### Real-World Domains and Subdomains

Los dominios tienen *problem space* y *solution space*. El espacio del problema nos permite pensar en una estrategia de negocio para solucionarlo, mientras que el espacio de la solución se enfoca en como  podemos implementar software para resolver el problema. 

- El espacio del problema es la parte del dominio que necesita ser desarrollado para poder proveer un nuevo Dominio Central. Para evaluar el espacio del problema es necesario examinar los subdominios que *existen actualmente y los cuales son necesarios*. Por lo tanto, el espacio del problema es la combinación del Dominio Central y los subdominios que debe de usar. Los subdominios nos permiten tener ver diferentes partes del dominio que son necesarias para poder resolver el problema.
- El espacio de la solución es uno o mas límites  del contexto, y  un conjunto de modelos de software. Esto es porque el límite de contexto es una solución especifica, *realization view*. El límite del contexto es utilizado para  crear una solución en software 

Uña meta deseable es poder alinear un subdominio con un límite de contexto en relación uno-a-uno. Esto permite segregar modelos de dominio en áreas bien definidas en áreas de negocio basado por su objetivo. En un dominio complejo se puede utilizar una vista de evaluación(*assessment view*) para poder entender nuestro espacio del problema. Lo cual, nos permite dividir conceptual mente un límite de contexto en dos o mas subdominios, o múltiples límites de contextos.

#### Before we can execute a specific solution, we need to make an assessment of the problem space and the solution space. 

- ¿Cuál es el nombre o la visión estratégica del dominio central?
- ¿Qué conceptos se deben de considerar como parte de la estratégica del dominio central?
- ¿Cuáles son los dominios de soporte y genéricos necesarios para el dominio central?
- ¿Quiénes deberán de trabajar en cada área del dominio?
- ¿Es posible crear los equipos de trabajo?


Una vez que se tiene un buen entendimiento del espacio del problema, es tiempo de pensar en el espacio de la solución. El espacio de la solución esta influenciado por tecnologías y sistemas existentes. Aquí, es necesario pensar en términos claramente separados del límite del contexto por que estamos mirando el lenguaje ubicuo.

- ¿Cuáles son los software que existen actualmente, pueden ser reutilizados?
- ¿Cuáles son los vienes que necesitamos adquirir o crear?
- ¿Cómo están conectados entre ellos, o integrados?
- ¿Es necesario tener una integración adicional?
- ¿Dado los vienes existentes y los que deben ser creados, Cuál es el esfuerzo requerido?
- ¿Poner en acción el plan estratégico y todos los proyectos secundarios tienen una alta probabilidad de éxito, o uno de ellos puede causar el retraso o falla del proyecto?
- ¿Los términos del lenguaje ubicuo donde están involucrados son totalmente diferentes ?
- ¿Cómo son mapeados o traducidos los términos y conceptos entre los límites de los contextos?
- ¿Cuáles de los límites del contexto contienen conceptos que abordan el Dominio central y cuales patrones serán usados para modelarlo?

#### Making Sense of Bounded Contexts 

Un límite de contexto es un límite explicito en donde el modelo del dominio existe. El modelo del dominio expresa un Lenguaje ubicuo como modelo de software. Los límites son creados porque cada conceptos dentro del modelo, con sus propiedades y operaciones tienen un significado especial. 

Es común que dentro de dos diferentes modelos, objetos con el mismo o nombre similar tengan diferentes significados. Cuando un límite es puesto al rededor de dos modelos, el significado de cada concepto en cada Contexto es exacto. En consecuencia, un límite de contexto es principalmente un límite lingüístico.

## Chapter 3. Context Maps 

#### Drawing Context Maps 

Un *mapa contextual* captura el terreno existente. Primero, debes de mapear el presente, no imaginar el futuro. Sí,  la visión cambia durante el transcurso del proyecto, el mapa se puede actualizar. 

Existen múltiples patrones de organización e integración, que existen comúnmente entre dos límites de contexto.

- **Partnership**: Es una relación de cooperación entre equipos en dos contextos. Los equipos deben de cooperar en la evolución de sus interfaces para adaptar el desarrollo que se necesita en ambos sistemas. 
- **Shared Kernel**: Se comparte una parte del modelo y asocia formas de código con interdependencias. Es necesario designar  límites   en  subconjuntos  del modelo del dominio donde los equipos  acuerden. 
- **Customer-Supplier Development**: Cuando dos equipos están en una relación *proveedor-cliente*, donde el equipo *proveedor* puede tener éxito independientemente del equipo *cliente*. En el caso contrario, el equipo *cliente* necesita del equipo *proveedor* para su éxito.
- **Conformist**: Cuando dos equipos de desarrolladores tienen una relación proveedor-cliente, pero el equipo proveedor no tiene interés de ayudar al otro equipo.
- **Anticorruption Layer**: Las capas de traslado pueden ser simples cuando es el puente entre dos bien definidos límites de contexto. Pero cuando la comunicación o el control no es adecuado en un *shared kernel*, el traslado puede ser muy complejo. Como cliente *downstream*, crea una capa aislada que provee al sistema funcionalidades del sistema *upstream* en términos del modelo del dominio. Un servicio de dominio (*Domain Service*) puede ser definido en el contexto del cliente por cada tipo de capa de anticorrupción. Si se utiliza REST, un servicio de dominio del cliente accede a un *Open Host Service OHS*. El servidor responde produciendo una representación como *Published Language*.  La capa de anti corrupción del cliente traduce la representación a un objeto de dominio en el contexto local.
- **Open Host Service**: Define un protocolo que da acceso a tu subsistema como un conjunto de servicios. Abre el protocolo para todo aquel que necesite integrarlo pueda utilizarlo. Mejora y expande el protocolo para que pueda soportar nuevos requerimientos.  Este patrón puede ser implementado utilizando recursos **REST**, los cuales el límite del dominio del cliente puede utilizar.
- **Published Language**: El traslado entre modelos de dos límites de contextos requiere un lenguaje en común. Utiliza un lenguaje bien documentado que pueda expresar la información necesaria del dominio. Puede ser implementado de varias maneras, ya sea utilizando XML, JSON o en algunas ocasiones HTML. También puede ser utilizado como **Event-Driven Architecture**.
- **Separate Ways**: Debemos ser despiadados cuando se trate de definir términos. Si dos conjuntos de funcionalidad no tiene una relación significativa, pueden estar separados. Integración puede ser costosa, y puede en algunas ocasiones tener pocos beneficios. Si es posible, declara un límite de contextos sin ninguna conexión entre ellos, lo cual permite al desarrollador encontrar soluciones simples y especializadas dentro de un alcance.
- **Big Ball of Mud**: Esto sucede cuando los modelos son mezclados y sus límites son inconsistentes. Modelar límites acerca este desastre y diseñarlo es una *big ball of mud*. 


Comúnmente la integración de sistemas se basa en RPC. A diferencia de una llamada local, una llamada remote tiene gran potencial de de legración de rendimiento o falla. Cuando el sistema al cual se le realiza la llamada no esta disponible, la petición no es exitosa. Lo cual genera un gran nivel de dependencia. Para poder reducir este nivel es necesario utilizar estrategias, tales como *out-of-band*, asíncrono, procesos por eventos.

Un gran nivel de autonomía puede ser alcanzado cuando el *estado dependiente* se encuentra en el sistema local. Esto puede verse como *cache* de objetos. En lugar de esto, se crea objetos en el dominio local, traduciéndolos de la petición realizada al modelo *upstream*. Para poder obtener el estado es necesario crear llamadas  RPC bien definidas , o peticiones REST pero cuando sea necesario sincronizar cambios con un modelo remoto, la mejor forma de realizar esto es a través de notificaciones *message-oriented*. Estas notificaciones pueden ser enviadas utilizando un servicio de bus o cola de mensajes, o publicada via REST.

### Chapter 4 Architecture
Una de las grandes ventajas de DDD es que no requiere el uso específico de una arquitectura. Ya que se ha creado el dominio Central, el cual reside en el limite de contexto, esto permite a una o varias arquitecturas jugar un papel en el sistema. Algunas arquitecturas pueden influenciar el modelo del dominio y tener un gran efecto. El objetivo es *use just the right choices and combinations of architecture and architecture patterns*.

La demanda de  la calidad de software deberá  alentar al uso de estilos de arquitecturas y patrones.  Los seleccionados deberán proveer o exceder los requisitos de calidad  

#### layers
El patrón de arquitectura de capas es considera por muchos como el abuelo de todos. Soporte N-sistemas y es comúnmente utilizado en la web, empresas, y aplicaciones de escritorio. 

**Separa la expresión del modelo del dominio y la lógica de negocio, y elimina cualquier dependencia de infraestructura, interfaz de usuario, o lógica de aplicación que no sea lógica de negocio. Divide software complejo en capas. Desarrolla un diseño dentro de cada capa que sea coherente y depende únicamente de la capa anterior.

El dominio central reside en una capa en la arquitectura. Arriba esta la interfaz de usuario UI, y capas de aplicación. Debajo de todo esta la capa de infraestructura.

![Capas ](https://github.com/KillLoGiC/resumen/blob/master/images/layers.png)

La interfaz de usuario contiene únicamente código de direcciones de vista de usuarios (*user view*) y solicitud.  **No deberá contener lógica de dominio/negocio**. Si la interfaz de usuario utiliza objetos del modelo del dominio, generalmente es limitado a representar los datos. Si se utiliza este acercamiento, un *modelo de Presentacion* puede ser utilizado para prever el conocer acerca de objetos del dominio. *Open Host Service OHS* puede ser utilizado para proveer invocaciones remotas de una API.

*Application Services* residen en la capa de aplicación. Estos son diferente de *servicios del dominio*. Por lo tanto, carecen de lógica de dominio. Pueden controlar transacciones y seguridad. Ademas, pueden estar encargados de notificaciones basado en eventos. **Las *Application Services* en este capa son los clientes directos del modelo del dominio, aunque estos no posean lógica de negocios. Estos permanecen ligeros y coordinan operaciones realizadas en objetos del dominio, como **Aggregates**. Comúnmente la función de *Application Services* es aceptar parámetros de la UI, utiliza *Repository* para obtener una instancia de *Aggregates*, y entonces ejecuta operaciones en el.

Cuando un nuevo *Aggregates* deba ser creado,  *Application Services* utilizará  una *Factory* o un constructor para ser instanciado y, después,  utilizar el correspondiente repositorio. 

Cuando el modelo del dominio es diseñado para publicar *Domain events*, la capa de aplicación puede subscribirse a un numero de eventos. Haciendo esto permite que los eventos sean almacenados, reenviado. Esto permite al modelo del dominio que se enfoque únicamente a su núcleo y permite a *Domain Event Publisher* de mantenerse ligero y libre de dependencias de infraestructura. 

#### Hexagonal or Port and Adapters

Permite a a múltiples clientes interactuar con el sistema.
> Necesitas un nuevo cliente?. Agrega un adaptador para transformar el input del cliente a uno que sea entendido por la API interna de la aplicacion. 

**Un adaptador es creado para transformar los resultados de una aplicacion a una salida aceptable**.
Existen dos areas primarias, *outside* y *inside*. La parte exterior permite a los clientes enviar entradas(*input*) y tambien provee mercanismos de persistencia de datos, almacena las salida de la aplicacion(base de datos), o lo envia (*messaging*)
