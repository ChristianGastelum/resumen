# Implementing Domain-Driven Design by Vaughn Vernon
        
## Author: Christian Eder Gastélum Reyes
 
> We strive to produce quality in the software we develop. We achieve some quality by using test to help us avoid delivering software with a fatal number of bugs. Yet, even if we could produce completely bug-free software, that in itself does not necessarily mean that a quality software model is designed.   *The software model—the way the software expresses the solution to the business goal being sought—could still suffer greatly*

 ### Chapter 1. Getting Started With DDD

Los fundamentos principales de DDD están basados en la discusión, escuchar, entendimiento, descubrimiento, y valores de negocio, todo esto para poder centralizar el conocimiento. Si eres capaz de *entender el negocio* en el cual se basará, por lo menos podrá participar en el modelado del software y podrá participar en  el proceso de crear el  **lenguaje ubicuo**. (ubicuo. Está presente a un mismo tiempo en todas partes)
 

 Durante este proceso de creado del **lenguaje ubicuo** es necesario entablar conversaciones con *expertos del dominio*.
Los *expertos del dominio* son aquellos que conocen como funciona el negocio. Un *experto del domino*  no esta basado en  "títulos". Ya que, existen personas que conocen su área de negocio bastante bien. Por lo tanto, ellos pueden proveer información vital para el **lenguaje ubicuo**.

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
Es un límite conceptual alrededor de una aplicación o un sistema finito. La razón detrás de este límite es acentuar que cada término, frase u oración (lenguaje ubicuo) dentro del dominio tiene un significado específico. 


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
    
    Cuando los límites del contexto son bien definidos y cuidadosamente particionados, todos los equipos  tienen un  claro entendimiento  de *donde* y  *porqué* las integraciones son necesarias. Los límites son  explícitos,  y las relaciones entre ellos también. 
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

#### Layers
El patrón de arquitectura de capas es considera por muchos como el abuelo de todos. Soporte N-sistemas y es comúnmente utilizado en la web, empresas, y aplicaciones de escritorio. 

**Separa la expresión del modelo del dominio y la lógica de negocio, y elimina cualquier dependencia de infraestructura, interfaz de usuario, o lógica de aplicación que no sea lógica de negocio. Divide software complejo en capas. Desarrolla un diseño dentro de cada capa que sea coherente y depende únicamente de la capa anterior**.

El dominio central reside en una capa en la arquitectura. Arriba está la interfaz de usuario UI, y capas de aplicación. Debajo de todo esta la capa de infraestructura.

![Capas ](https://github.com/KillLoGiC/resumen/blob/master/images/layers.png)

La interfaz de usuario contiene únicamente código de direcciones de vista de usuarios (*user view*) y solicitud.  **No deberá contener lógica de dominio/negocio**. Si la interfaz de usuario utiliza objetos del modelo del dominio, generalmente es limitado a representar los datos. Si se utiliza este acercamiento, un *modelo de Presentacion* puede ser utilizado para prever el conocer acerca de objetos del dominio. *Open Host Service OHS* puede ser utilizado para proveer invocaciones remotas de una API.

*Application Services* residen en la capa de aplicación. Estos son diferente de *servicios del dominio*. Por lo tanto, carecen de lógica de dominio. Pueden controlar transacciones y seguridad. Además, pueden estar encargados de notificaciones basado en eventos. **Las *Application Services* en este capa son los clientes directos del modelo del dominio, aunque estos no posean lógica de negocios. Estos permanecen ligeros y coordinan operaciones realizadas en objetos del dominio, como **Aggregates****. Comúnmente la función de *Application Services* es aceptar parámetros de la UI, utiliza *Repository* para obtener una instancia de *Aggregates*, y entonces ejecuta operaciones en el.

Cuando un nuevo *Aggregates* deba ser creado,  *Application Services* utilizará  una *Factory* o un constructor para ser instanciado y, después,  utilizar el correspondiente repositorio. 

Cuando el modelo del dominio es diseñado para publicar *Domain events*, la capa de aplicación puede subscribirse a un numero de eventos. Haciendo esto permite que los eventos sean almacenados, reenviado. Esto permite al modelo del dominio que se enfoque únicamente a su núcleo y permite a *Domain Event Publisher* de mantenerse ligero y libre de dependencias de infraestructura. 

#### Hexagonal or Port and Adapters

Permite a a múltiples clientes interactuar con el sistema.
> Necesitas un nuevo cliente?. Agrega un adaptador para transformar el input del cliente a uno que sea entendido por la API interna de la aplicación. 

**Un adaptador es creado para transformar los resultados de una aplicación a una salida aceptable**.
Existen dos áreas primarias, *outside* y *inside*. La parte exterior permite a los clientes enviar entradas(*input*) y también provee mecanismos de persistencia de datos, almacena las salida de la aplicación(base de datos), o lo envía (*messaging*)

![Arquitectura Hexagonal](https://github.com/KillLoGiC/resumen/blob/master/images/hex.png)

#### Design the Application Inside per Fucntional Requirements

Cuando se utiliza la arquitectura hexagonal, se diseña la aplicación con el caso de uso en mente, no el numero de clientes a soportar. Cualquier numero o tipo de clientes puede pedir varios puertos, pero cada adaptador delega a la aplicación utilizando la misma API.

La aplicación recibe peticiones a través de su API publica. Los  limites de la aplicación o *hexagono interno*, es también un uso de caso. En otras palabras, se debe crear usos de casos basados en requerimientos de la aplicación, no por el numero de clientes o salidas.

> Cuando la aplicación recibe una petición a través de su API, utiliza el modelo del dominio para completar las peticiones, lo cual involucra a la lógica del negocio. En consecuencia, la API de la aplicación publica un conjunto de *Application Services*. *Application Services* son los clientes directos del modelo del dominio, al igual si se utilizara la arquitectura de capas.

Es posible considerar la implementación de Repositorios como adaptadores persistentes, los cuales proveen el acceso a instancias Aggregates anteriormente creadas y almacenar nuevas. Adicionalmente, es posible tener implementaciones de repositorios para bases de datos relacionales, almacenamiento de documentos, cache distribuido, almacenamiento en memoria. Si la aplicación envía un Evento de Dominio para afuera, podría utilizar un Adaptador diferente para mensajería. 

#### Representation State Transfer --REST 
Es una abstracción de los elementos arquitectónicos dentro del sistema distribuido hypermedia. *REST* ignora los detalles de los componentes implementados y sintaxis del protocolo para enfocarse en los roles de componentes, limitaciones dentro de sus interacciones con otros componentes, y la interpretación de datos significativos.

##### Stateless
La interacción cliente-servidor: no debe de guardar estados en la comunicación. Tal que, cada  petición del cliente al servidor deberá contener toda la información necesaria para entender  la petición, y no puede  tomar ventaja del contexto almacenado en el servidor. 
##### Cache
Para poder mejorar la eficiencia de la red, se agrega la limitación *cache* para formar *client-cache-stateless-server*.La limitación cache requiere que los datos dentro de la respuesta  a la petición , sean  etiquetados implícitamente o explícitamente, como  cache o no-cache. 

#### Key aspects of a RESTful HTTP Server

Los recursos son el concepto clave. Un diseñador de sistemas decide que componentes serán accesibles desde el exterior, y  se asignan una entidad distinta. En general, cada recurso tiene un *URI*, el cual deberá apuntar a un recurso (las cosas que son alcanzables desde el exterior). Los recursos tienen representaciones, interpretaciones de sus estados, en uno o mas formatos.

El siguiente concepto clave es la comunicación sin estados (*stateless communication*), utilizando mensajes auto descriptivos. Como una petición HTTP, la cual contiene toda la información que el servidor necesita. Es importante que el cliente y el servidor no dependan de peticiones individuales para establecer una sesión. Esto permite acceder a cada recurso independientemente de otras peticiones, este aspecto ayuda a un mejor escalamiento.


Aspectos claves de REST:
- Cada recurso tiene un URL, y cada URL apunta a un recurso que es expuesto.
- Comunicación sin estados. Utiliza mensajes auto descriptivos. Como una *HTTP Request*, el cual lleva toda la información necesaria por el servidor. Esto permite acceder a cada recurso independientemente de otras peticiones, este aspecto ayuda alcanzar un escalamiento masivo.
- Si se toman los objetos como recursos, a diferencia de otras arquitectura. Los métodos para invocar son fijos. Cada objeto soporta la misma interfaz. En RESTful HTTP, los métodos son *GET, PUT, POST, DELETE*.

#### REST and DDD 

Hay dos acercamientos para combinar DDD y RESTful HTTP: 
1. Crear un limite de contexto separado para la capa de interfaces del sistema y usar estrategias para acceder al Dominio central desde el modelo de interfaz del sistema. Ejemplo:
    >  Se crea un sistema que administra un grupo de trabajo, incluyendo   sus tareas,  horarios/citas, sub grupos, y todos los procesos necesarios para administrarlo. Se diseña  un modelo de dominio, el cual no contiene detalles de infraestructura, y captura el lenguaje ubicuo  e  implementa la lógica del negocio. Para publicar una interfaz  a este dominio, se provee una interfaz remote como un conjunto de recursos *RESTful*. 

Hacer esto nos permite realizar cambios en el dominio central para después decidir si, cada cambio deberá ser reflejado en el modelo de interfaz del sistema y, si es así, la mejor forma de mapearlo.

2. Es recomendado cuando se utilizan tipos de media. Si es necesario soportar un tipo especifico de media no solo por una interfaz del sistema pero una categoría con interacciones similares a cliente-servidor, un modelo del dominio puede ser creado para representar cada tipo de media. 

Estos dos acercamientos tienen diferentes propósitos dependiendo de los términos de reusabilidad. Mientras mas especifica sea la solución se utiliza el primer acercamiento. Si la solución es mas general, y requiere estandarización se utiliza la segunda opción, *media-type-centric*.

#### Event-Driven Architecture

**Es la arquitectura de software que promueve la producción, detección, consumo de, y reacciones a eventos**.

Los Eventos del dominio, modelan explícitamente procesos del negocio.
#### Long-Running Process aka Saga

Tres acercamientos para el diseno de *Long-Running Process*:

- Diseña el proceso como una tarea compuesta, la cual es rastreada por un componente ejecutivo este graba los pasos y la completud de la tarea utilizando **objetos persistentes**. 
- Diseña el proceso como un conjunto de parejas de *Aggregates*, las cuales colaborarán en un conjunto de actividades. Una o mas instancias de *aggregates* actuará como el *ejecutivo* y mantendrá el estado del proceso.
- Diseña el proceso sin estados *stateless* donde, cada *message handler* debe de complementar cada evento recibido con información de progreso realizado al siguiente mensaje. El estado del proceso es mantenido solo en el cuerpo de cada mensaje enviado de colaborador a colaborador.

### Chapter 5 Entities

Se diseña un concepto del dominio como una entidad cuando es importante su individualidad, cuando es necesario distinguirlo de otros objetos en el sistema. Una entidad es única y tiene la capacidad de ser cambianda continuamente sobre un periodo de tiempo.

Cuando un objeto es distinguido por su identidad, y no por sus atributos, has esto su principal definición. Mantén las definiciones de clases simples y enfocarte en la continuidad del ciclo de vida e identidad. Define un medio para distinguir cada objetos sin importar su forma o historia.

#### Unique Identity

En vez de enfocarnos en los atributos o comportamientos, desmantela la definición del objeto entidad hasta la característica mas intrínseca, particularmente aquellos o mas comúnmente usados para encontrarlo. Agrega solo el comportamiento que es esencial al concepto y a los atributos que requiere el comportamiento.

**Los objetos valor pueden almacenar identificadores únicos**. Estos son inmutables, lo cual asegura estabilidad de identidad, y cualquier comportamiento especifico del tipo identidad es centralizado. 

Consideraciones para la creación de identidades:
- El usuario provee uno o mas valores originales únicos como entrada a la aplicación. La aplicación debe de asegurarse que estos son únicos.
- La aplicación internamente genera una entidad utilizando un algoritmo que asegure la singularidad de este.
- la aplicación depende de un almacenamiento persistente, como una base de datos, para generar un identidad única.
- Otro limite de contexto ya ha determinado la identidad única. Es su entrada o es seleccionada por el usuario.

La generación de identidad puede ocurrir ya sea en la construcción del objeto, o después, como parte del almacenamiento persistente.

#### Construction
Cuando se crea una nueva instancia de una entidad, es deseable utilizar un constructor para capturar el estado de la entidad y, además, para poder Identificarla y permitir a los clientes encontrarla. Si se diseña correctamente un constructor. Este toma por lo menos el UI como parámetro. Si la entidad es consultada de otra forma, como nombre o descripción, también es posible agregarlos a los parámetros del constructor.

En algunas ocasiones una entidad mantiene una o más *invariants*. Las cuales son un estado que deben mantenerse idéntico a lo largo del ciclo de vida de la entidad. 

Por definicion de la entidad, no es necesario mantener los cambios a los cuales es expuesta en su ciclo de vida. Solo se tiene que dar soporte al continuo cambio de estados.

La forma mas practica para alcanzar un buen sistema de cambios es utilizando *Domain events* y *Event Store*. Se crea un unico tipo de evento para cada cambio de estado importante, el cual es ejecutado en un *aggregates*. Los eventos son publicados cuando sea completado. Un subscriptor se registra para revicir cada evento producido por el modelo. Cuando lo recibe, el subscriptor guarda el evento en un *event store*.

### Chapter 6 Value Objects

Un valor puede tener una existencia larga o corta. Es solo un valor que viene y se va cuando se le necesita.
#### How do we determine if a domain concept sould be modeled as a Value?

Es necesario prestar mucha atención a sus características. Cuando solo prestas atención a los atributos de un elemento en el modelo, clasificarlo como *Value object*. Hazlo expresar sus atributos que transmite y da la funcionalidad relacionada.Trata el objeto valor como inmutable. No le des una entidad y evita complexidad de diseño solo para mantener entidades.

#### Value Characteristics

Cuando se este decidiendo si un conceptos es un valor, tu debes de determinar, si posee la mayoria de estas caracteristicias:

- Puede ser medible, contable, o describe una cosa en el dominio.

    Cuando se tiene un verdadero objeto valor en el dominio, no es una cosa del dominio. Al contrario, es un concepto que mide, calcula, o ademas, describe un elemento en el dominio. La edad de una persona. La edad no es un elemento, pero mide o cuantifica el numero de años de una persona. El nombre no es un elemento pero describe como es el nombre de la persona.
- Puede mantenerse inmutable.

    Un objeto que es un valor es inmutable si no cambia después de ser creado.
    
- Puede modelar un concepto al unir atributos como una unidad integral.
    
    Un objeto valor puede poseer uno o varios atributos individuales, donde cada uno esta relacionado entre si. Cada atributo contribuye al todo. Si, se separa un atributo de los otros cada atributo falla en proveer cohesión. Es diferente a agrupar en conjunto de atributos en un objeto. Ejemplo. El valor 50,000 dolares tiene dos atributos: 50,000 y dolares. Estos atributos por separado no tienen un significado especial. Estos atributos juntos son un concepto que describen una medida monetaria. 

- Puede ser completamente reemplazados cuando las medidas o descripciones cambien.
    
    Si el modelo tiene un valor inmutable deberá mantenerse como referencia por una entidad mientras que el estado actual describa el estado actual del *whole value*. Si deja de ser cierto, el valor es completamente reemplazado por un nuevo valor, el cual represente el estado actual.  **No se debe de utilizar un método para cambiar el estado de un valor. Ya que violaría la cualidad de inmutabilidad. Es preferible reemplazar el valor por completo *whole value*, asignando el objeto a otra nueva instancia.**
- Puede ser comparado cuando otros utilizando *Value equality*.
    
    Cuando una instancia de objeto valor es comparado con otra instancia, un examen de equidad es empleado. A lo largo del sistema hay muchas instancias valor que son iguales, y aun así no son el mismo objeto. Equidad es determinada al comparar el tipo de objetos y sus atributos. Si ambos tipos y atributos son iguales, el valor es considerado igual.
- Suministra a sus colaboradores con *Side-Effect-Free Behavior*
    
    **Una función es una operación de un objeto que produce un resultado pero sin modificar su propio estado**. Ya que, al no ocurrir modificaciones cuando se ejecuta una operación especifica, entonces esa operación no tiene efectos secundarios *side-effect*.

**Cuando un método de un objeto valor tenga como parámetro una entidad, el resultado deberá poder usarse para que la entidad se modifique en sus propios términos**.


#### Testing Value Objects

Para enfatizar *test-first*, se presentan pruebas antes de proveer la implementación de objetos valor. Estas pruebas están basadas en el diseño del modelo del dominio, ya que se proveen ejemplos de como un cliente usara cada objeto. En este punto esta mas enfocado en demostrar como varios objetos del modelo del dominio serán usados por el cliente y que esperan estos clientes cuando los utilicen. Es esencial asumir la perspectiva del cliente cuando se diseña un modelo en orden de capturar conceptos esenciales.

Siempre hay que diseñar nuestro modelo de datos por el bien del modelo del dominio, y no al contrario.

### Chapter 7 Services

Un servicio en el dominio es una operación sin estados *stateless* que cumple una función especifica del dominio. El mejor indicio de que debemos crear un servicio en el modelo del dominio es cuando la operación que se necesita realizar esta fuera de lugar como un método en un **aggregates** o un **value object**. 

**No queremos lógica del negocio en una *Application service* queremos la lógica en un *Domain Service*.** La diferencia entre un *application service* y un *domain service* es que la aplicación, es le cliente del dominio del modelo, lo cual naturalmente es el cliente del servicio del modelo.

**Cuando una proceso significativo o trasformación en el dominio no es responsabilidad de una entidad o un valor objeto, es necesario agregar una operación autónoma en el modelo, la cual se declarará como un servicio**. **Es necesario definir la interfaz en términos del lenguaje del modelo y estar seguro que el nombre de la operación sea parte del lenguaje ubicuo. Ademas el servicio debe ser autónomo**.

El modelo del dominio generalmente tiene que lidiar con comportamientos detallados, los cuales son están enfocados en un aspecto especifico del negocio, un servicio en el dominio tendería a pegarse a principios similares.

Se pueden utilizar servicios para:

- Realizar procesos significativos al negocio.
- Trasformar un objeto del dominio de una composición a otra.
- Calcular un valor requerido por una salida de uno o  más de un objeto del dominio.


Un servicio en el dominio es bienvenido a utilizar repositorios cuantas veces sea necesario, pero acceder repositorios de una instancia de un *aggregates* no es recomendable.

### Chapter 8 Domain Events 

Un *Domain Event* es utilizado para capturar una accion que ha sucedido en el dominio. 

Eventos que deben ser emitidos a servicios externos, donde el sistema de la empresa ha sido divido e incidencias deben ser comunicadas a lo largo de límites de contexto.

Algunas palabras calves que nos ayudan a determinar el posible uso de eventos cuando se habla con un experto del dominio:

- "Cuando" *When*
- "Sí eso pasa" *If that happens*
- "Informarme si..."*Inform me if*, "notificarme si" *Notify me if*
- "Una acción de" *An occurrence of*

Los eventos pueden eliminar la necesitad de *two phase commits* y respaldar las reglas de *aggregates*. Una regla de *aggregates* dice que solo una instancia debe ser modificada en una sola transacción, y todos los otros cambios dependientes deberán suceder en transacciones separadas.  Esta división de tareas ayuda a proveer un mejor escalamiento y rendimiento de entre servicios.

Cuando se modela un evento, hay que nombrarlos de acuerdo a sus propiedades dentro del lenguaje ubicuo en el limite de contextos donde se origino. Si un evento es el resultado de ejecutar una operación en un *aggregates*, el nombre es derivado del comando ejecutado. El comando es la causa del evento, por lo tanto, el nombres del evento debe mencionar el comando en tiempo pasado.
```
Command Operation:  BackLogItem#commitTo(Sprint aSprint)
Event Outcome:      BacklogitemCommitted
```
Después de nombrar el evento es necesario agregar la hora cuando el evento ocurrió. Ademas de esto, se puede incluir cualquier cosa que nos permita provocar el evento de nuevo. Esto usualmente incluye la entidad de la instancia de *aggregates* en donde tomó lugar, o la instancia de *aggregates* que lo invoco.

**En un ambiente multiusuario guardar el *ID* siempre es necesario.**

**Un evento es usualmente inmutable**.

Primero que nada, la interfaz de un evento debe expresar el propósito de transmitir sus causas. La mayoría de eventos tiene un constructor que permita una instanciación completa, además de complementar con un *accessor/getter* para cada propiedad.

#### With Aggregate Characteristics

En algunas ocasiones los eventos son diseñados para que sean creados directamente por el usuario. Esto se hace en respuesta a algunas hechos que no son resultados directos del comportamiento ejecutado en una instancia de un *aggregates* en el modelo. **Posiblemente, un usuario del sistema inicia una acción que es considerada un evento por si mismo**. Cuando esto sucede, los eventos pueden ser modelados como *aggregates* y mantener su propio repositorio. Ya que representa acciones pasadas, su repositorio no permitirá su eliminación.

Cuando los eventos son modelados de esta manera, se convierten en parte de la estructura del modelo. 

Cuando un elemento es modelado de esta manera, puede ser publicado vía infraestructura de mensajería al mismo tiempo puede ser agregado a su repositorio. **El cliente podria llamar a un *domain service* para crear un evento, agregarlo a su repositorio, y luego publicarlo a traves de infraestrctura de mensajeria**. 

Una vez que la mensajería guarde exitosamente el nuevo mensaje del evento en su almacenamiento persistente, entonces podría de forma sincrónica mandarlo a una *queue listener, topic/exhange susbscribers* o actores sí se utiliza el modelo de actores.

#### Publishing Events from the Domain Model 

Es necesario evitar exponer al modelo del dominio a cualquier infraestructura de mensajería. Un objeto valor puede poseer uno o varios atributos individuales, donde cada uno esta relacionado entre si. Cada atributo contribuye al todo. Si, se separa un atributo de los otros cada atributo falla en proveer cohesión. Es diferente a agrupar en conjunto de atributos en un objeto. Ejemplo. El valor 50,000 dolares tiene dos atributos: 50,000 y dolares. Estos atributos por separado no tienen un significado especial. Estos atributos juntos son un concepto que describen una medida monetaria. 

### Publisher

Tal vez el uso mas común de eventos es cuando un *aggregate* crea un evento y lo publica. El editor reside en un modulo en el modelo, pero no modela un aspecto del dominio. Mejor dicho, provee un simple servicio a un *aggregate* que necesita notificar a subscriptores de un evento.

**The Application service controls the transaction**.

Mandar un evento utilizando infraestructura de mensajería permite envíos asíncronos a subscriptores foráneos.

##### Spreading the Nes to Remote Bounded Contexts 

Existen diversas formas de hacer que limites de contextos remotos sean avisados de que un evento ha ocurrido en un limite de contexto. Existen un gran número de mensajeros tales como *ActiveMQ, RabbitMQ, Akka, NServiceBus, MassTransit*.

El uso del mecanismos de mensajería entre limites de contexto requiere la adopción de compromiso de consistencia. El cambio en un modelo el cual tiene influencia en cambios en uno o mas modelos no sera consistente por un periodo de tiempo.

#### Messaging Infraestructure Consistency

Al menos dos mecanismos en la solución de mensajería deben de ser siempre consistentes uno con el otro: el almacenamiento persistente utilizado por el modelo del dominio y el almacenamiento persistente de la infraestructura de mensajería utilizada para enviar los eventos publicados por el modelo. Esto es un requisito para asegurar que los cambios que se realicen en lo modelo sean persistentes, el envió de eventos sea garantizado, y si un evento es enviado a través de mensajería, indica la situación actual reflejando el modelo que lo publicó.

#### How is model and Event persistence consistency accomplished?
1. El modelo del dominio y la infraestructura de mensajería comparten el mismo almacenamiento persistente(*data source*). Esto permite los cambios del modelo y la introducción de un nuevo mensaje para enviar bajo la misma transacción local.    
    - Ventaja. Permite un buen rendimiento
    - Desventaja. El almacenamiento del sistema de mensajería debe de estar en la misma base de datos del modelo.
2.  El almacenamiento persistente  del modelo del dominio  y  de la mensajería deben de estar bajo una transacción global o XA (*two-phace commit*).

    - Ventaja. Permite mantener los almacenamientos separados.
    - Desventaja. Las transacciones globales tienen rendimiento pobre.
3. Se crea un almacenamiento especial para eventos en el mismo almacenamiento donde es almacenado el modelo del dominio. Esto es un **Event Store**.
    
    - Ventaja. El almacenamiento no es controlado ni pertenece a la mensajería si no, al limite de contexto. Los componentes foráneos creados utilizan el *event store* para almacenar lo publicado, eliminar publicaciones *unpublished* a través de mecanismos de la mensajería. 
    - Desventajas. El mensajero de eventos debe ser personalizado para poder mandar mensajes utilizando la mensajería, y los clientes deben ser diseñados para  mensajes duplicados.

Se recomienda utilizar mensajería asíncrona para alcanzar un alto grado de independencia entre los sistemas. 

Un evento contiene una cantidad limitada de parámetros y/o estado de *aggregate* que dará suficiente significado que permitirá a los limites de contextos subscritos a reaccionar correctamente.

**Si es necesario replicar conceptos, objetos, y sus asociaciones con otros modelos en el modelo actual, es recomendable utilizar RPC**.

#### Event Store 


Mantener un almacenamiento para todos los eventos del dominio para un limite de contexto tiene varios beneficios. Considere que podría hacer si fueras a almacenar un evento por cada comportamiento de cada comando que es ejecutado.
1. Utilizar un *event store* como cola para publicar todos los eventos a través de mensajería. 
2. Se puede utilizar el mismo *event store* para alimentar el notificado de eventos basado en REST a una lista de clientes.
3. Examinar el historial de resultados de cada comando que ha sido ejecutado en el modelo. Esto podría ayudar a rastrear errores, no solo en el modelo sino en los clientes.
4. Utilizar los datos para análisis del negocio. 
5. Utilizar los eventos para reconstruir cada instancia de *aggregate* cuando sale de un repositorio. 
6. Dada una aplicación del punto anterior, poder deshacer cambios en un *aggregate*.

**Una de las primeras cosas que se necesitan hacer es crear un subscriptor que reciba cada evento que es publicado fuera del modelo**.

#### Publishing Notifications as RESTful Resources

El estilo de notificación REST trabaja mejor cuando es utilizado en un ambiente que sigue las premisas básicas de *Pubhish Subscribe*. Aquí un resumen de los ventajas y desventajas del acercamiento REST:
- Si potencialmente muchos clientes pueden ir a un buen conocido URI para pedir el mismo conjunto de notificaciones, Este acercamiento funciona bien. Esencialmente las notificaciones son enviadas a cualquier numero de clientes. 
- Si uno o mas clientes requieren obtener eventos de múltiples orígenes, REST no es la opción apropiada. Esto describe una cola, donde potencialmente muchos orígenes necesitan notificar a uno o mas clientes, y el orden de recepción importa. Un modelo encuesta *polling model* no es una buena opción para implementar colas.

El acercamiento REST para publicar notificaciones de eventos es distinto a una mensajeria tipica. El *publisher*  no mantienee un conjunto de *subscribers* registrados por que nada es enviado a los grupos interesados. En lugar de esto, los clientes REST obtiene las notificaciones usando URI.

Los clientes utilizan el metodo de HTTP *Get* para obtener el ultimo registro. 

### Chapter 9 Modules

Los modulos en el modelo sirven como un contenedor para clases que son altamente cohesivo con otra. El objetivo debe ser poca union entre clases que estan en diferentes modulos. 

**Escoge modulos que cuenten la historia del sistema que contengan un conjunto de conceptos cohesivos. Esto produce poca union entre modulos, si no es asi, busca una forma de cambiar el modelo para desenredar los conceptos. Da nombres a los modulos para que formen parte al lenguaje ubicuo y los nombres deben reflejar una perspectiva del dominio**.

#### Simple rules for Module Design 

|Module Do's and Don'ts | Why|
|---|----|
| Diseña módulos que encajen con los conceptos de modelado| Típicamente se tiene un modulo por algunos *aggregates*, los cuales son cohesivos, si solo por referencia|
|Nombra a los módulos en base al lenguaje ubicuo| Este es un objetivo básico de DDD, pero también tiende a venir naturalmente si se piensa en los conceptos que son modelados|
|No crear módulos mecánicamente de acuerdo a componentes de tipo o patrones utilizados en el modelo| Nuestro modelo nos e beneficiara si segregamos a todos los *aggregates* en un modulo, todos los servicios en otro modulo, todas las fabricas en otro. Piensa en el dominio , No solo pienses en los tipos de componentes o patrones que usas para resolver el problema que se encuentra enfrente tuyo|
| Diseña a los módulos libres| Asegura que los módulos sean independientes de los otros que tienen los mismos beneficios de las clases. Esto hará que sea fácil de mantener, de separar conceptos|
| Esfuérzate por las dependencias acíclicas en los módulos pares donde se necesita acoplamiento| es raramente posible o practico que los módulos sean completamente independiente entre ellos. Después de todo, un modelo del dominio implica alguna unión. Pero, tu reducirás la unión de los componentes si piensas en los términos de dependencia entre dos módulos pares e unidireccionales (ejemplo, productos dependen de un equipo, pero equipos no dependen de productos)|
| No ser tan estricto con las reglas entre módulos padres e hijos| Es realmente difícil pretender independencia entre módulos  padres e hijos|
| No crees módulos como un concepto estático en el modelo, pero permite que se moldeen con objetos que ellos organizan| Si los conceptos del modelo son maleables y toman diferente forma, comportamiento, y nombres sobre el tiempo, es  muy probable que los módulos que organizan estos mismos conceptos deberán ser creados, renombrados, y borrados de la misma manera. |

#### Module Naming Convertions for the Model 

El nombre de los módulos debe de identificar el limite de contexto. 

Utilizando el ejemplo de SaaSovation se nombraron los módulos de la siguiente manera:

- com.saasovation.identityaccess.domain 
- com.saasovation.collaboration.domain 
- com.saasovation.agilepm.domain 

Esto es compatible con la arquitectura de capas y la arquitectura hexagonal. Con la arquitectura hexagonal se tiene una parte interna de la aplicación, la cual incluya la parte del dominio. ** El compartimiento *domain* puede único a interfaces/clases que sirvan únicamente como contenedores de módulos debajo nivel.

- com.saasovation.identityaccess.domain.model
- com.saasovation.collaboration.domain.model
- com.saasovation.agilepm.domain.model

Aquí es donde las clases del modelo deben ser definidas. Este nivel de paquete puede contener interfaces reutilizables y clases abstractas.

En este ejemplo Saasovation colocara en este modulo interfaces comunes, tales como las utilizadas para la publicación de eventos, clases abstractas para entidades y objetos valor.


### Chapter 10 Aggregates

¿Un *aggregates* es solo un grafo de objetos relacionados bajo un mismo padre? Sí es así,  ¿Existe un limite de objetos que puedan ser permitidos en el grafo? ¿Ya que una instancia de *aggregate* puede  referenciar a otras instancias de *aggregate* la asociación puede navegar, modificando varios objetos a lo largo del viaje? ¿Y de que se trata el concepto de *invariants* y *consistency boundary* ? La respuesta de esta ultima pregunta tiene gran influencia sobre las otras preguntas.

#### Rule: Model True Invariants in Consistency BOundaries

Cuando se trata de descubrir los *aggregates* en un limite de contexto, es necesario entender las verdaderas *invariants* del modelo. Solo con ese conocimiento se puede determinar que objetos deberán ser agrupados en un *aggregate*.

**Una *invariant* es una regla de negocio que debe ser siempre consistente**.  Existen varias formas de consistencia. 

- *Transactional consistency* Es considerada inmediata y atómica.
- *Eventual consistency*

Ejemplo:
```
Si se tiene la operación

    a + b = c 

donde *a* es 2, *b* es 3, *c* debe de ser 5.
De acuerdo a esta regla y condiciones, sí *c* es cualquier cosa pero 5, el sistema *invariant* es violada. 
Para segurar que *c* sea consistente, se disena un limite alrededor de estos atributos especificos del modelo:

    AggregateType1 {
        int a;
        int b;
        int c;

        operations ...
    }
```
Los limites de consistencia aseguran que todo dentro cumplan con un conjunto de reglas *invariants* del negocio no importan que operaciones estén realizando. Por lo tanto, *aggregates* es un sinónimo de **limites de consistencia transaccional**. En el ejemplo anterior *Aggregatetype1* tiene tres atributos tipo *int*, pero cualquier *aggregate* puede tener atributos de diversos tipos.

Cuando se emplea un mecanismo tipo de persistencia, se utiliza una sola transacción para mantener consistencia. Cuando la transacción se ejecuta, todo lo que se encuentre dentro de los limites debe ser consistente. *Un aggregate bien diseñado puede ser modificado de cualquier forma requerida por el negocio con sus *invariants* consistentes dentro de una sola transacción.

El hecho de que los *aggregates* deban ser diseñados con el enfoque de consistencia implica que la interfaz de usuarios deberá concentrar cada pedido para ejecutar un solo comando en una sola instancia de *aggregate*. Si las peticiones del usuario tratan de completar muchas cosas, la aplicación sera forzada a modificar múltiples instancias a la vez.

Por lo tanto, *aggregates* tienen su enfoque en los limites de consistencia y no motivados por el deseo de disenar grafos. 

#### Rule: Design Small *aggregates*

Limitar el *aggregate* a solo la entidad raiz *root entity*  y un numero minimo de atributos y/o propiedades de atributos. El numero  minimo correcto son aquellos los cuales son necesarios.

¿ Pero cuales son necesarios? Aquellos que deben ser consistentes con tros, aunque los expertos del dominio no los especifiquen como reglas.  Por ejemplo:

```
Los atributos Product, name y description. No nos podemos imaginar que nombre y descripción  sean inconsistentes, si son modelados en diferentes aggregates. 
Cuando se cambia el nombre, probablemente también se necesite cambiar la `descripción. 
Sí se cambia uno y no el otro, es probable porque se esta arreglando un error o mejorando la descripción para que sea mas adecuada al nombre.
```

¿Qué tal si se decide modelar una parte contenida como una entidad? Para esto, es necesario preguntarlos si la parte cambia sobre el tiempo, o si puede ser completamente reemplazada cuando los cambios se requieran. Los casos donde instancias pueden ser reemplazadas apuntan al uso de *object value* y no una entidad. Algunas veces entidades son necesarias. Es recomendable favorecer tipo de valores como parte de *aggregate* no significa que los *aggregate* sea inmutable por que el objeto raíz *root object* cambia cuando las propiedades de los tipos de valores son reemplazados.

#### Rule: Reference other Aggregates by Identity 

Un *aggregate* puede referenciar a una raíz de otro *aggregate*. Aun así, es necesario recordar que esto no coloca la referencia dentro de los límites de consistencia del *aggregate*  La referencia no causa la formación de un *aggregate*. Por ejemplo en Java se modelaria de la siguiente manera:


![Aggregate](https://github.com/KillLoGiC/resumen/blob/master/images/aggre.png)


``` Java 
public class BackLogItem extends COncurrencySsafeEntity {
    ...
    private Product product;
}

```

#### Making Aggregates Work Together Through Identity References 

Es preferible referencias a *aggregates* externos utilizando su *identificador global único*, y no mantener referencia al objeto directamente (puntero).

![Imagen 10.6](https://github.com/KillLoGiC/resumen/blob/master/images/referAggre.png)

Se dividira la fuente en:

``` Java
public class backlogitem extends Concurrencyssafeentity {
    ...
    private ProductId productid;
    ...
}
```

Los *aggregate* con referencias de objetos son automaticamente mas pequenos por que las referencias nunca son cargadas automaticamente. 

#### Model Navigation

Se recomienda utilizar un repositorio o servicio para buscar objetos dependientes antes de invocar el comportamiento del *aggregate*. 

#### Scalability and Distributtion

Ya que, no se utilizan referencias directas a otros *aggregates* pero si las referencias por identidad, el estado de persistencia puede alcanzar  una gran escala. *Almost-infinite scalability* puede ser alcanzado si se permite división continua del almacenamiento de datos del *aggregate*. 

#### Rule: Use eventual Consistency Outside the Boundary

Cualquier regla que utilice *aggregates* no estará todo actualizado todo el tiempo.  A través, de cada proceso, u otros mecanismos de actualización, otras dependencias pueden resolverse en un tiempo especifico. 

Por lo tanto, si al ejecutar un comando en una instancia de *aggregate* requiere que una o mas *aggregate* ejecuten una o mas reglas, es recomendable utilizar *eventual consistency*. Hay que aceptar que no todas las instancias de *aggregate* en un ambiente empresarial serán consistentes, esto nos ayuda aceptar que la consistencia eventual tiene sentido en pequeña escala cuando pocas instancias son involucradas.

##### How to know when to choose  Transactional or eventual consistency

**Cuando se examine el caso de uso, es necesario preguntarse sí,  es trabajo del usuario ejecutar el caso de uso para que los  datos sean consistentes. Si es así, se utiliza consistencia transaccional, pero solo si se siguen las otras reglas de *aggregate*.  Si es el trabajo de otro usuario, u otro sistema, se utiliza consistencia eventual**. 

#### Reasons to Break The Rules 

##### Reason one: user interface Convenience

Algunas veces las interfaces de usuario, permiten a los usuarios definir características comunes de muchas cosas a la vez para poder crear un conjunto de estas. La interfaz de usuario permite que se introduscan todas las propiedades comunes en una seccion, y entonces, una por una las propiedades diferentes, lo cual elimina la repeticion de tareas. 

##### Reason Two: Lack of Technical Mechanisms

Las consistencias eventuales requieren el uso de procesamiento *out-of-band*, tales como: mensajería, temporizadores, o tareas de fondo *background threads*. ¿Que pasa si no contamos con estos componentes? En este caso, nos veremos forzados a modificar dos o más *aggregate* en una transacción.

##### Reason Three: Global Transactions

Hay que considerar el uso de tecnologías *legacy*  y políticas empresariales. 


##### Reason Four: Query Performance

Existen ocasiones donde es mejor tener punteros a objetos de otros *aggregates*. Esto puede ser usado para reducir los problemas de rendimiento de las consultas sobre repositorios.



 
#### Implementation
##### Create a Root Entity with Unique Identity 

Cada raiz debe de disenarse con un identificador unico global. 

##### Favor Value Objects Parts 

Escoge para modelar una parte del *aggregate* como objeto valor *object value* en vez de una entidad siempre y cuando sea posible. Una parte contenida puede ser completamente reemplazable, si el reemplazo no causa costo elevado en el modelo o infraestructura. 

Usualmente, cuando se utilizan *key-value* o *document store*, las instancias *aggregate* son típicamente serializadas como un valor de representación del almacenamiento.

#### Using Law of Demeter and Tell, Don't Ask

- **Law of Demeter**: Esta guia se enfoca en el principio de menos conocimiento. Piensa en un objeto cliente y otro objecto que el objeto cliente utiliza para ejecutar algún comportamiento del sistema; nos podemos referir a este segundo objeto como *server*. Cuando el objeto cliente usa el objeto servidor, deberá saber lo menos posible de la estructura del servidor. Los atributos del servidor y propiedades deberán ser completamente desconocidas para el cliente. El cliente puede pedirle al servidor que ejecute un comando que esta declarado en la interfaz. Aunque, el cliente no deba de alcanzar el servidor, pedir al servidor por una parte interna, y después ejecutar un comando en esta parte. Si el cliente necesita un servicio que se encuentra dentro de las partes internas del servidor, el cliente no debe de obtener servicio a estas partes para ejecutar un comando. El servidor deberá proveer una interfaz y, cuando sea invocada, delegar permisos para ejecutar el comando.

     En resumen: cualquier método en cualquier objeto puede invocar métodos solo si sucede lo siguiente: 1. Es si mismo, 2 un parámetro es pasado a el, 3 un objeto que instancia, 4 una parte del objeto auto contenida puede ser accedido directamente.

- **Tell, Don't Ask**: Esta guia reafirma que los objetos deben de hacer lo que se les dice. Esto aplica de la siguiente forma: Un objeto cliente no deberá preguntar al objeto servidor por sus partes internas, para luego tomar una decisión en base al estado de estas, y luego hacer que el objeto servidor realice una tarea.

### Chapter 11. Factories

#### Factories in the Domain Model: 

Las principales motivaciones para utilizar fabricas:

Cambiar la responsabilidad de crear instancias de objetos complejos y *aggregate* a un objeto separado, el cual puede no tener responsabilidad en el modelo del dominio pero aun forma parte del diseño del dominio.  Provee una interfaz que encapsula toda la complejidad y no requiere que el cliente haga referencia a clases concretas las cuales están siendo instanciadas. Crear *aggregate* como una pieza, refuerza sus *invariants*.

Una fabrica puede o no tener responsabilidades adicionales en el modelo del dominio otras aparte de crear objetos. Un objeto tiene el único propósito de instanciar un tipo especifico de *aggregate* no tendrá otras responsabilidades y no deberá ser considerado como ciudadano de primera clase en el modelo. Es solo una fabrica. Un raíz *aggregate* que provee un método fabrica para producir instancias de otro tipo de *aggregate* tendrá como su principal responsabilidad en proveer su principal comportamiento, el método fabrica es solo uno de estos.

Uno de los casos que se puede obtener grandes beneficios del las fabricas es cuando se crean objetos de diferentes tipos en una clase hereditaria, el cual es un caso clásico.  El cliente necesita dar solo los parámetros básicos los cuales la fabrica utiliza para determinar el tipo concreto que creará.  

**Cuando se tiene el comportamiento de un metodo que exprese el lenguaje ubicuo en manera que no es posible si se utiliza solo un constructor**. 


### Chapter 12 Repositories 

Un repositorio usualmente hace referencia a un lugar de almacenamiento, el cual consiste en un lugar seguro o donde se almacenan cosas. Cuando se almacena algo en un repositorio y luego se regresa a sacarlo, se tiene la expectativa que el estado sera el mismo que cuando se almaceno al inicio.

Cuando se almacena una instancia de *aggregate* en su correspondiente repositorio, y luego se utiliza el repositorio para extraer la misma instancia, el producto esperado es el objeto. Sí se altera una instancia preexistente de un *aggregate*, que es extraída de un repositorio, los cambios serán persistentes. 

Por cada vez tipo de objeto que necesita acceso global, crea un objeto que pueda proveer la ilusión de una colección  una instancia preexistente de un *aggregate* , que es extraída de un repositorio, los cambios serán persistentes. 

Por cada vez tipo de objeto que necesita acceso global, crea un objeto que pueda proveer la ilusión de una colección en memoria de todos los objetos de ese tipo. Configura acceso global utilizando interfaces bien definidas. Provee métodos para agregar y remover objetos. Provee métodos para seleccionar objetos en base a algún criterio y que su resulta sea un objeto o un conjunto de objetos completamente instanciados, los cuales cumplen con el criterio. Provee repositorios solo para *aggregates*.


Los *aggregate* son los únicos que tienen repositorios. Sí no se esta utilizando *aggregates*  en un  limite de contexto,  los repositorios no serán muy útiles. 

Existen dos tipos de diseño de repositorios, *collection-oriented* y *persistence-oriented*.

#### Collection-oriented Repositories

Este diseño se puede considerar como el acercamiento tradicional por que apega a las ideas básicas del patrón DDD.

En muchos lenguajes OOP los objetos son añadidos a una colección, y son mantenidos ahí hasta que son removidos. No se necesita nada especial para hacer que una colección reconozca los cambios a los objetos, solo se requiere pedir a la colección una referencia a un objeto especifico y luego hacer una petición al objeto, lo cual modifica su estado. El mismo objeto se mantiene en la colección, y ahora el objeto es diferente del otro que fue anteriormente modificado.

**Un repositorio deberá parecerse a una colección de conjuntos. No importa la especificación de los mecanismos de persistencia, *no se debe de permitir que las instancias de un objeto sea almacenado dos veces*. Además, cuando obtengan objetos de un repositorio y se modifiquen, *no es necesario guardarlos nuevamente en el repositorio***.

Un repositorio orientado a colecciones imita a una colección en que ninguna de las partes de los mecanismos persistentes son mostrados al cliente por una interfaz publica. 

Los mecanismos de persistencia deberán tener algunos mecanismos de almacenamiento persistente. Estos deberán de poder tener la habilidad de mantener el seguimiento de los cambios de cada objeto. Esto puede ser obtenidos de varias maneras:

- **Implicit Copy-on-Read**.  El mecanismo de persistencia copia implícitamente el estado de cada objeto en lectura cuando este es reconstruido de *data store* y lo compara con su copia del cliente para ser enviado. . Cuando al mecanismo persistente se le pide leer un objeto del *data store*, lo hace  y luego copia el objeto. Cuando una transacción es creada a través de un mecanismo persistente, los mecanismos de persistencia busca modificaciones en la copia del objeto y los compara. Todos los cambios al objeto son enviados al *data store*.
- **Implicit Copy-on-Write**. Los mecanismos de persistencia administran todas las cargas de objetos a través de un proxy. Cada objeto es cargado del *data store*, un pequeño proxy es creado, el cual se le da al cliente. El cliente sin saber invoca el comportamiento en el proxy del objeto, el cual refleja el comportamiento al objeto real. Cuando el proxy recibe la primera invocación, crea una copia del objeto. El proxy mantiene los cambios de estados del objeto y los marca. Cuando la transacción es creada a través de los mecanismos persistentes, busca por objetos marcados y todos son enviados al *data store*.

La ventaja de cualquiera de estos acercamientos es el que los cambios de en los objetos son seguidos implícitamente, no requieren conocimiento del cliente o intervención de mecanismos de persistencia. 

#### Pesistence-oriented Repositories

Cuando los mecanismos de persistencia no detecten implícitamente o explícitamente los cambios de un objeto. Esto pasa cuando se utiliza *in-memory Data Fabric* o NoSQL. Cada vez que se cree una instancia de un *aggregate* o se realice un cambio a uno ya existente, es necesario almacenarlo en el *data store* utilizando *save()* o algún método parecido del método repositorio.

Cuando se utiliza *collection-oriented*, los *aggregate* son añadidos solo cuando son creados. Por lo contrario, *persistence-oriented* las instancias de *aggregate* deben ser almacenadas cuando son creadas y cuando son modificadas.

Aunque estos tipos de estilos imitan a una colección *Map*, desafortunadamente es necesario utilizar *put()* para añadir objetos nuevos y los cambios a objetos, así reemplazando los valores previos asociados con una llave determinada. Esto también sucede cuando un objeto es cambiado es lógicamente el mismo objeto que ya esta almacenado, por que estos no proveen seguimiento de estados. Mejor dicho, cada ** put()** y **putAll()** representan una transacción lógica diferente.

Al utilizar este tipo de almacenamiento permite simplificar las escrituras y lecturas de los *aggregates*. Por ejemplo, considere la simplicidad de agregar esto a  product

``` Java 
cache.put (product.productId(), product);
    // later ...

product = cache.get(productId);
```

Como se puede ver la instancia product  es automáticamente serializadas. 

Cuando se utiliza las bases de datos NoSQL, probablemente se quiera utilizar rápidos y compactos métodos de conversión para *aggregate* de su forma serializadas o su forma objeto. Para optimizar la visualización de los *aggregates* se puede crear un mapeo de descripción.

#### MongoDB Implementation

1. Una forma de transformar las instancias de *aggregates* a formato MongoDB, y luego transformarlo a su formato original. MongoDB utiliza un formato llamo BSON.
2. Una identidad generada por MongoDB, la cual es asignada al *aggregate*.
3. Una referencia al nodo/cluster de MongoDB.
4. Una colección única donde se almacene el tipo *aggregate*. Todas las instancias de tipo *aggregate* deberán ser convertidas como un conjunto llave-valor (*key-value*)


#### Managing Transactions

Un acercamiento utilizado para facilitar transacciones del aspectos del modelo del dominio es manejarlos en la capa de la aplicación. Generalmente, se crea un *Facade* para caso de uso donde se agrupan direcciones por aplicación o sistema. El *facade* esta diseñado con métodos del negocio, generalmente un método por cada caso de uso. Cada método coordinada una tarea requerida por cada caso de uso. Cuando un método de un *facade* es invocado por la capa de interfaz del usuario, el método inicia una transacción y luego actúa como cliente en el modelo del dominio. Una vez qué la transacción haya terminado, el método envía los resultados de esta. Sí un error ocurre, el cual impide que se finalice el caso de uso, la transacción vuelve a su estado original.

Para en listar cambios en el modelo del dominio en una transacción, hay que asegurarse que la implementación de repositorios tenga acceso a la misma sesión o unidad de trabajo de la transacción que la capa de aplicación haya iniciado. De esta forma las modificaciones hechas en la capa del dominio serán enviadas de forma apropiada a una base de datos o retrocederán a su estado original. 

#### Testing Repositories

Hay dos formas para probar repositorios. Se necesita probar los repositorios ellos mismos para saber si funcionan correctamente. También sé debe de probar con código el cual utiliza repositorios. Para éste es necesario utilizar una implementación de producción. De otra forma no se podría saber si el código de producción funciona correctamente. Para el segundo tipo,  se puede usar implementaciones de producción, o se puede utilizar implementaciones de memoria.

#### Chapter 13 Integrating Bounded Contexts 

##### Integration Basics

Cuando hay dos o más limites de contextos que necesitan ser integrados, existen algunas formas razonables para hacer esto en código.

1. Exponer el limité de contexto por medio de una API, y otro contexto utiliza esta API para realizar llamadas remotas o RPCs. 
2. Utilizar mecanismos de mensajería. Cada sistema necesita interactuar con este, a través de colas de mensajes o *Publish-Subscribe*.
3. Utilizando *RESTful HTTP*. *REST* es un medio para intercambio y modificación de recursos que son identificados únicamente al utilizar *URI*. Varias operaciones pueden ser realizadas en cada recurso.

##### Distributed Systems Are Fundamentally Different

###### Principles of Distributed Computing:
- La conexión no es confiable.
- Siempre hay algo de latencia, y aveces mucha.
- La banda ancha no es infinita.
- No asumir que la conexión es segura.
- Las topologías de redes cambian.
- El conocimiento y políticas se encuentran Distribuidas entre múltiples administradores.
- El transportar información a través de la red tiene un costo.
- La red es heterogénea.

##### Exchanging Information across System Boundaries

En muchas ocasiones cuando necesitamos que un sistema externos nos provea información a nuestro sistema, necesitamos mandar información al servicio. Los servicios algunas veces necesitan responder. Por ende, necesitamos una forma confiable para enviar información de sistema a sistema. Esta información necesita ser enviada de forma estructurada entre los diferentes sistemas la cual pueda ser consumida rápidamente. 

Los datos como parámetros son solo estructuras que pueden ser leídos por la maquina, y ser generados en varios formatos.

Existen múltiples formas de generar estructuras que se pueden utilizar para intercambio de información entre sistemas. Una implementación técnica se basa en los lenguajes de programación, los que facilitan la transformación (*serialized*) de objetos a una forma binaria y lo regresan al estado original. Esto también requiere el despliegue de interfaces y clases de objetos que son utilizados en un sistema.

Otro acercamiento es construir estructuras para el intercambio de información Utilizando un formato estándar intermedio. Algunas opciones que se pueden usar son *XML*, *JSON*, o algún formato especializado.

#### Integration Using RESTful Resources

Cuando un contexto provee un conjunto de recursos *RESTful* a través de *URIs*, es un tipo de *Open Host Service*: 
        
        Define un protocolo que de acceso a tu subsistema como un conjunto de servicios. 
        Deja el protocolo abierto para qué todo lo que necesite integración lo pueda utilizar.
        Mejora y expande el protocolo para que pueda procesar nuevos requisitos.


##### Long-Running Processes, and avoiding Responsability

Pagina 333


