# Modelado 

Los fundamentos principales de DDD están basados en la discusión, entendimiento, descubrimiento, y valores de negocio, todo esto permite poder centralizar el conocimiento. Para poder diseñar un software en un dominio en particular, es necesario entablar una conversación con los expertos del dominio. Donde, un experto del dominio es aquella persona, la cual tiene un basto conocimiento en el dominio en la que labora. Lo cual, permite crear una definición refinada y precisa del negocio. Lo cual permite a los desarrolladores reflejar con mayor exactitud el área del negocio en software.



Para poder iniciar el diseño del software es necesario tener claro cual es el modelo del dominio, el cual es un modelo basado en software, y a su vez, esta basado en un dominio de negocio. También considerado como modelo objeto, donde existen objetos, los cuales tienen datos y comportamientos en base al negocio. Crear un modelo del domino es esencial para poder utilizar DDD. Utilizando DDD los modelos del dominio tienden a ser pequeños y enfocados [Referencia libro de Implementing DDD Vaugh Capitulo 1].

Un Dominio a grandes rasgos es que es lo que hace la organización y en que mundo lo hace. Cuando se desarrolla un software para una empresa, se esta trabajando en su dominio. El cual esta compuesto por subdominios.

La aplicacion que se desarrollara tiene como objetivo agilizar la migracion de maquinas fisicas a la nube. Este es el modelo del dominio. Adicionalmente, la aplicacion tendra las siguientes caracteristicas:

- Crear un inventario. Este tendra como proposito obtener caracteristicas especificas de una maquina tales como: CPU, RAM, disco duro. Donde el resultado se le es presentado al usuario para poder seleccionar que maquinas seran migradas a la nube. Para realizar este trabajo se escaneara la LAN por maquinas fisicas.
- Creacion de maquinas. Se utilizara la informacion del inventario para crear maquinas virtuales en la nube.
- Respaldo a discos virtuales. Se convertiran los discos duros de las maquinas seleccionadas en el inventario  a discos virtuales, estos son necesarios para  la migracion. 

la aplicacion tiene tres subdominios:
- Escaneo
- Creacion de maquinas virtuales
- Creacion de discos virtuales


