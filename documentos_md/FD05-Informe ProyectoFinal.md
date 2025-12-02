![Logo de la Universidad Privada de Tacna](https://github.com/user-attachments/assets/d0c41097-f5da-4dd4-934c-223bdf1e88e8)

# [cite_start]UNIVERSIDAD PRIVADA DE TACNA [cite: 623]
## [cite_start]FACULTAD DE INGENIERÍA [cite: 624]
### [cite_start]Escuela Profesional de Ingeniería de Sistemas [cite: 625]

**Proyecto**
[cite_start]“Plataforma de Análisis de Despliegue de Proyectos” [cite: 626, 627]

**Curso:**
[cite_start]Inteligencia de Negocios [cite: 628, 629]

**Docente:**
Mag. [cite_start]Patrick Cuadros Quiroga [cite: 630, 631]

**Integrantes:**
* [cite_start]Ancco Suaña, Bruno Enrique (2023077472) [cite: 633]
* [cite_start]Loyola Vilca, Renzo Fernando (2021072615) [cite: 635]

**Tacna – Perú**
[cite_start]**2025** [cite: 636, 637]

---

## [cite_start]Sistema Plataforma de Análisis de Despliegue de Proyectos [cite: 638]
### [cite_start]Documento de Especificación de Requerimientos de Software [cite: 639]

[cite_start]**Versión 1.0** [cite: 640]

---

### CONTROL DE VERSIONES
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1.0 | "BEAS, CDAR, RFLV " | PCQ | - | 09/09/2025 | Versión 1.0 |
[cite_start][cite: 641]

---

### [cite_start]INTRODUCCIÓN [cite: 679]
[cite_start]El presente documento describe la especificación de requerimientos del sistema Plataforma de Análisis de Despliegue, cuyo propósito es brindar a la Universidad Privada de Tacna una herramienta de inteligencia de negocios capaz de analizar, visualizar y gestionar información sobre las tecnologías de despliegue utilizadas por los estudiantes en sus proyectos. [cite: 680] [cite_start]La información aquí consignada se basa en la información adquirida durante el desarrollo, además de levantamientos adicionales y supuestos necesarios para definir de manera integral los requerimientos funcionales y no funcionales del sistema. [cite: 681] [cite_start]El sistema está dirigido a usuarios que deseen visitar lugares turísticos de Tacna de manera eficiente y estandarizada, como estudiantes, desarrolladores independientes y organizaciones académicas o empresariales. [cite: 682] [cite_start]La plataforma permitirá a los usuarios ingresar datos clave a través de un login y visualizará el aplicativo garantizando calidad, coherencia y cumplimiento de estándares predefinidos. [cite: 683]

### [cite_start]I. Generalidades de la Empresa [cite: 644]
#### [cite_start]1. Nombre de la Empresa [cite: 645]
[cite_start]Universidad Privada de Tacna – Escuela Profesional de Ingeniería de Sistemas [cite: 686]
#### [cite_start]2. Vision [cite: 646]
[cite_start]Ser una institución líder en educación superior, reconocida por su excelencia académica, innovación tecnológica y compromiso con la formación de profesionales altamente competitivos a nivel nacional e internacional. [cite: 688]
#### [cite_start]3. Mision [cite: 647]
[cite_start]Formar profesionales con sólidos valores éticos, competencias técnicas y visión crítica, capaces de aportar soluciones innovadoras a los retos de la sociedad mediante el uso eficiente de la ciencia y la tecnología. [cite: 690]
#### [cite_start]4. Organigrama [cite: 648]
[cite_start]![Organigrama de la Universidad Privada de Tacna](https://github.com/user-attachments/assets/b785d0d6-1579-4081-9bfe-e50e90c5f210) [cite: 691]

### II. [cite_start]Visionamiento de la Empresa [cite: 692]
#### [cite_start]1. Descripcion del Problema [cite: 650]
[cite_start]Actualmente la Escuela de Ingeniería de Sistemas de la Universidad Privada de Tacna no dispone de un método sistemático para conocer qué herramientas, lenguajes y plataformas de despliegue están siendo utilizados en la práctica por sus estudiantes. [cite: 694] [cite_start]Las decisiones sobre qué tecnologías enseñar, qué convenios con proveedores de nube (como AWS Educate o Azure for Students) promover o dónde enfocar los recursos de capacitación se basan en suposiciones generales del mercado y no en datos concretos del propio ecosistema universitario. [cite: 695] [cite_start]Esta falta de datos conduce a una posible brecha entre el plan de estudios y las habilidades aplicadas por los alumnos, dificultando la modernización de los cursos y la identificación de tendencias tecnológicas emergentes dentro de la propia institución. [cite: 696]

#### [cite_start]2. Objetivos de Negocios [cite: 651]
* [cite_start]Optimizar la asignación de recursos académicos (licencias, convenios) enfocándose en las herramientas de mayor demanda. [cite: 698]
* [cite_start]Fortalecer la toma de decisiones de la dirección académica, proveyendo una herramienta de inteligencia de negocios para la planificación estratégica. [cite: 699]
* [cite_start]Fomentar una cultura de innovación y mejora continua, visibilizando las tendencias tecnológicas emergentes dentro de la propia comunidad universitaria. [cite: 700]

#### [cite_start]3. Objetivos de Diseño [cite: 652]
* [cite_start]Desarrollar un módulo de extracción de datos seguro y eficiente que se conecte a las APIs de repositorios como GitHub. [cite: 702]
* [cite_start]Crear un dashboard de BI intuitivo e interactivo que permita a usuarios no técnicos explorar y comprender la información fácilmente. [cite: 703]
* [cite_start]Asegurar la precisión e integridad de los datos procesados y visualizados en la plataforma. [cite: 704]
* [cite_start]Construir una arquitectura escalable que permita el futuro crecimiento en volumen de datos y la posible expansión a otras facultades. [cite: 705]

#### [cite_start]4. Alcance del proyecto [cite: 653]
[cite_start]El proyecto “Generador de Documentación Impulsado por IA (GDI-IA)” contempla el desarrollo de una plataforma web que permita: [cite: 707]
* [cite_start]Capturar información guiada de usuarios. [cite: 708]
* [cite_start]Procesar dicha información utilizando modelos de IA. [cite: 709]
* [cite_start]Generar documentos en formatos PDF y DOCX. [cite: 710]
* [cite_start]Gestionar el historial de documentos creados. [cite: 711]
* [cite_start]Brindar acceso vía suscripción a funcionalidades premium. [cite: 712]

#### [cite_start]5. Viabilidad del Sistema [cite: 654]
[cite_start]De acuerdo al análisis técnico, operativo, legal y financiero realizado, el proyecto es viable: [cite: 714]
* [cite_start]Existe infraestructura tecnológica adecuada para su desarrollo y despliegue. [cite: 715]
* [cite_start]Se cuenta con personal calificado para la implementación y mantenimiento del sistema. [cite: 716]
* [cite_start]La tendencia del mercado favorece la adopción de soluciones basadas en IA. [cite: 717]
* [cite_start]El análisis de factibilidad financiera muestra un VAN positivo y una relación B/C favorable. [cite: 718]

#### [cite_start]6. Informacion obtenida del Levantamiento de Informacion [cite: 655]
[cite_start]Durante el levantamiento de información se identificó: [cite: 720]
* [cite_start]Alta demanda de automatización en generación de documentos en sectores académicos y tecnológicos. [cite: 721]
* [cite_start]Interés de usuarios potenciales en contar con soluciones accesibles y fáciles de usar. [cite: 722]
* [cite_start]Necesidad de reducción de tiempos de entrega de documentos formales. [cite: 723]
* [cite_start]Limitada oferta actual de plataformas que integren varios servicios de IA de forma modular. [cite: 724]

### III. [cite_start]Análisis de Procesos [cite: 725]
#### [cite_start]a) Diagrama del Proceso Actual – Diagrama de actividades [cite: 726]
#### [cite_start]b) Diagrama del Proceso Propuesto – Diagrama de actividades Inicial [cite: 727]

![Diagrama de procesos](https://github.com/user-attachments/assets/751d388e-6b71-460d-85fa-17070189b83b)
[cite_start][cite: 727]

### IV. [cite_start]Especificacion de Requerimientos de Software [cite: 728]
#### [cite_start]a) Cuadro de Requerimientos funcionales Inicial [cite: 729]
* El sistema web debe permitir la creacion de cuentas a los usuario nuevos
* El sistema web debe tener un modulo para introducir la informacion clave dependiendo del formato escogido
* El sistema web debe permitir la seleccion del formato estandarizado para iniciar un nuevo documento
* El sistema web debe contener modelos de IA
* El sistema web debe permitir la generacion documentos completos en formatos word - version 2
* El sistema web debe permitir la generacion documentos completos en formatos PDF siguiendo los formatos establecidos.
* El sistema web debe descargar el documento en el momento de su generacion
* El sistema web debe generar las citas y bibliografia automaticamente segun el contenido extraidas de fuentes reales dependiendo del formato escogido
* El sistema web debe almacenar un historial de los documentos realizados previamente
* El sistema web debe permitir la edicion de los documentos previamente creados - version 2
* El sistema web debe permitir generar documentos en distintos idiomas si así lo permite el modelo IA configurado.
* El sistema web debe permitir la creacion de cuentas para adminsitradores
[cite_start][cite: 730]

#### [cite_start]b) Cuadro de Requerimientos No funcionales [cite: 731]
| REQS | Requerimiento | Descripción | Prioridad | Urgencia | Estado de desarrollo | Estabilidad |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| RNF1 | Debe integrar Login | Debe validar las credenciales | Alta | Necesario | Terminado | Alta |
| RNF2 | Accesibilidad multiplataforma | La plataforma debe ser accesible desde navegadores web modernos, tanto en computadoras como en dispositivos móviles. | Alta | Necesario | En Proceso | Media |
| RNF3 | Seguridad de la información | La información introducida por los usuarios y los documentos generados deben estar protegidos con autenticación, cifrado y control de acceso. | Alta | Necesario | En Proceso | Media |
| RNF4 | Escalabilidad | La plataforma debe estar preparada para escalar en cuanto a número de usuarios y tipos de formatos a futuro. | Alta | Necesario | En Proceso | Baja |
| RNF5 | Compatibilidad con estándares documentales | El contenido generado debe cumplir con los estándares y formatos establecidos en los manuales institucionales. | Alta | Necesario | En Proceso | Media |
| RNF6 | Tolerancia a fallos | En caso de fallo de una IA o servicio externo, el sistema debe mostrar un mensaje claro y permitir reintentar la generación. | Alta | Necesario | En Proceso | Media |
| RNF7 | Registro de errores (log) | El sistema debe registrar errores internos para fines de soporte y mejora continua. | Alta | Necesario | En Proceso | Media |
| RNF8 | Interfaz adaptativa (responsive) | El diseño debe adaptarse correctamente a distintos tamaños de pantalla (teléfono, tablet, laptop, escritorio). | Alta | Necesario | En Proceso | Media |
[cite_start][cite: 732]

#### [cite_start]c) Cuadro de Requerimientos funcionales Final [cite: 733]
| REQS | REQUERIMIENTO | DESCRIPCION | PRIORIDAD | URGENCIAS | ESTADO DE DESARROLLO | ESTABILIDAD |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| RF001 | RegistroUsuario | El sistema web debe permitir la creacion de cuentas a los usuario nuevos | Alta | Necesario | Terminado | Alta |
| RF002 | RegistroAdmin | El sistema web debe permitir la creacion de cuentas para administrador | Alta | Necesario | Terminado | Alta |
| RF003 | ModuloInput | El sistema web debe tener un modulo para introducir la informacion clave dependiendo del formato escogido | Alta | Necesario | En Proceso | Media |
| RF004 | SeleccionFormato | El sistema web debe permitir la seleccion del formato estandarizado para iniciar un nuevo documento | Alta | Necesario | En Proceso | Media |
| RF005 | MultiIdioma | El sistema web debe permitir generar documentos en distintos idiomas si así lo permite el modelo IA configurado. | Alta | Necesario | En Proceso | Media |
| RF006 | ModelosIA | El sistema web debe contener modelos de IA | Alta | Necesario | En Proceso | Baja |
| RF007 | GenerarPDF | El sistema web debe permitir la generacion documentos completos en formatos PDF siguiendo los formatos establecidos. | Alta | Necesario | En Proceso | Media |
| RF008 | DescargaInmediata | El sistema web debe permitir la descarga del documento en el momento de su generacion | Alta | Necesario | En Proceso | Media |
| RF009 | GenerarCitas | El sistema web debe generar las citas y bibliografia automaticamente segun el contenido extraidas de fuentes reales dependiendo del formato escogido | Alta | Necesario | En Proceso | Media |
| RF010 | HistorialDocs | El sistema web debe almacenar un historial de los documentos realizados previamente | Alta | Necesario | En Proceso | Media |
| RF011 | DescargaHistorial | El sistema web debe permitir la descarga de los documentos previos | Alta | Necesario | En Proceso | Media |
[cite_start][cite: 734]

#### [cite_start]d) Reglas de Negocio [cite: 663]
* [cite_start]**RN-01: Control de Acceso** [cite: 736]
    * [cite_start]Descripción: Solo los usuarios autenticados pueden acceder a las funcionalidades del sistema. [cite: 737]
    * [cite_start]Condición: Se debe validar la sesión activa con token. [cite: 738]
    * [cite_start]Aplicación: Todas las secciones del sistema. [cite: 739]
* [cite_start]**RN-02: Plantillas y Formatos Estandarizados** [cite: 740]
    * [cite_start]Descripción: La generación de documentos debe seguir las plantillas institucionales o seleccionadas por el usuario. [cite: 741]
    * [cite_start]Condición: No se permite la modificación libre de estructura fuera de las plantillas. [cite: 742]
    * [cite_start]Aplicación: Módulo de generación. [cite: 743]
* [cite_start]**RN-03: Idioma y Localización** [cite: 744]
    * [cite_start]Descripción: Los documentos generados deben respetar el idioma seleccionado por el usuario. [cite: 745]
    * [cite_start]Condición: Solo idiomas soportados por el modelo IA activo. [cite: 746]
    * [cite_start]Aplicación: IA, salida de documentos. [cite: 747]
* [cite_start]**RN-04: Versionamiento de Documentos** [cite: 748]
    * [cite_start]Descripción: Cada documento generado debe almacenarse como una nueva versión. [cite: 749]
    * [cite_start]Condición: Cada nueva generación desde la misma entrada produce un documento con versión incremental. [cite: 750]
    * [cite_start]Aplicación: Historial de documentos. [cite: 751]
* [cite_start]**RN-05: Revisión de Calidad de Documentos** [cite: 752]
    * [cite_start]Descripción: Todo documento generado debe ser evaluado por el usuario mediante un mecanismo de feedback. [cite: 753]
    * [cite_start]Condición: La retroalimentación debe ser vinculada al documento generado. [cite: 754]
    * [cite_start]Aplicación: Post-generación, módulo de feedback. [cite: 755]
* [cite_start]**RN-06: Roles y Permisos** [cite: 756]
    * [cite_start]Descripción: Los administradores tienen acceso a estadísticas de uso, feedback de usuarios y ajustes de modelos IA. [cite: 757]
    * [cite_start]Condición: Se requiere perfil con privilegios de administrador. [cite: 758]
    * [cite_start]Aplicación: Panel de administración. [cite: 759]

### [cite_start]V. Fase de Desarrollo [cite: 760]
#### [cite_start]1. Perfiles de Usuario [cite: 665]
* [cite_start]**Usuario General:** Persona que utiliza la herramienta para generar documentación a partir de formularios guiados o flujos IA. [cite: 762]
* [cite_start]**Administrador:** Gestor del sistema que puede supervisar el uso de la IA, evaluar feedback, ajustar configuraciones del sistema y actualizar plantillas o modelos IA. [cite: 763]

| HU | Nombre | Descripción |
| :--- | :--- | :--- |
| HU01 | Inicio de Sesión | "Como usuario, quiero poder acceder a la página principal de la herramienta para comenzar a generar documentación." |
| HU02 | Descripción del Proyecto | "Como usuario, quiero poder describir mi proyecto en un formulario con campos para el tipo de proyecto, lenguajes utilizados y arquitectura, para que la IA entienda el contexto de la documentación." |
| HU03 | Selección de Plantilla | "Como usuario, quiero poder seleccionar una plantilla de documentación de una lista de categorías (arquitectura, despliegue, diseño, API) para guiar la generación de la documentación." |
| HU04 | Flujo de Preguntas Iniciales | "Como usuario, si no selecciono una plantilla, quiero que la IA me haga preguntas iniciales sobre mi proyecto para que pueda determinar el tipo de documentación a generar." |
| HU05 | Preguntas de la IA | "Como usuario, quiero que la IA me haga preguntas específicas dentro del formulario sobre mi proyecto para proporcionar detalles adicionales y refinar la documentación." |
| HU06 | Generación de Documento | "Como usuario, quiero que la IA genere un documento base en formato Markdown o texto plano basado en la información proporcionada, para tener un punto de partida para la documentación." |
| HU07 | Generación de Diagramas | "Como usuario, quiero que la IA genere diagramas UML relevantes para mi proyecto utilizando APIs externas (PlantUML, Mermaid) para visualizar la arquitectura y el diseño." |
| HU08 | Priorización de Diagramas | "Como usuario, quiero que la IA priorice la generación de ciertos tipos de diagramas UML (por ejemplo, diagramas de clases si menciono 'clases') para obtener la documentación más relevante." |
| HU09 | Vista Previa de Documento | "Como usuario, quiero poder ver una vista previa del documento generado en formato Markdown o texto plano antes de descargarlo, para revisar el contenido." |
| HU10 | Descarga en Formato PDF | "Como usuario, quiero poder descargar el documento generado en formato PDF para compartirlo y archivarlo fácilmente." |
| HU11 | Guardado de Documentación | "Como usuario, quiero que mi documentación generada se guarde en un servidor FTP durante un tiempo determinado, para poder acceder a ella posteriormente." |
| HU12 | Entrenamiento de la IA | "Como administrador de la herramienta, quiero poder revisar y analizar la documentación generada por la IA, junto con el feedback del usuario, para identificar áreas de mejora y entrenar a la IA para que genere documentación de mayor calidad en el futuro." |
| HU13 | Especificar Idioma | "Como usuario, quiero poder especificar el idioma en el que se genera la documentación (por ejemplo, italiano) para obtenerla en el idioma deseado." |
| HU14 | Feedback del Usuario | "Como usuario, quiero poder proporcionar feedback a la IA sobre la calidad de la documentación generada para ayudar a mejorar la herramienta." |
| HU15 | Ayuda y Soporte | "Como usuario, quiero tener acceso a una sección de ayuda o soporte para resolver dudas y obtener asistencia sobre el uso de la herramienta." |
[cite_start][cite: 764]

#### [cite_start]2. Modelo Conceptual [cite: 666]
##### [cite_start]a) Diagrama de Paquetes [cite: 667]
[cite_start]![Diagrama de Paquetes](https://github.com/user-attachments/assets/c96d88b4-8456-429a-9d62-c1729b8c9e05) [cite: 766]

##### [cite_start]b) Diagrama de Casos de Uso [cite: 668]
[cite_start]![Diagrama de Casos de Uso](https://github.com/user-attachments/assets/f0e30d4b-22fa-450f-a65c-3571a938c353) [cite: 767]

#### [cite_start]3. Modelo Logico [cite: 670]
##### [cite_start]a) Analisis de Objetos [cite: 671]
[cite_start]![Análisis de Objetos](https://github.com/user-attachments/assets/a21191ec-8984-47be-a690-0b61f4388836) [cite: 769]

##### [cite_start]b) Diagrama de Actividades con objetos [cite: 672]
[cite_start]![Diagrama de Actividades con Objetos](https://github.com/user-attachments/assets/9d671f65-27a3-488b-a4b5-0b0469b6187b) [cite: 770]

##### [cite_start]c) Diagrama de Secuencia [cite: 673]
[cite_start]![Diagrama de Secuencia](https://github.com/user-attachments/assets/0ab80d5d-c6a9-4629-bdf3-ecb25b5a7068) [cite: 771]

##### [cite_start]d) Diagrama de Clases [cite: 674]
[cite_start]![Diagrama de Clases 1](https://github.com/user-attachments/assets/6770f5e1-0c58-472d-ac15-1811eb2316e6) [cite: 772]
[cite_start]![Diagrama de Clases 2](https://github.com/user-attachments/assets/81ed5c93-548c-4447-b86a-79ca844d1877) [cite: 772]

### [cite_start]CONCLUSIÓN [cite: 773]
[cite_start]El proyecto Generador de Documentación Impulsado por IA (GDI-IA) propone una solución innovadora para automatizar la creación de documentos técnicos y académicos, respondiendo a una necesidad real de eficiencia, estandarización y calidad en la generación de documentación. [cite: 774] [cite_start]A través de la integración de tecnologías modernas como PHP, MySQL y servicios de inteligencia artificial vía APIs externas, se busca proporcionar a los usuarios una herramienta accesible, rápida y precisa. [cite: 775] [cite_start]La especificación de requerimientos aquí presentada define de manera clara y estructurada las funcionalidades esenciales del sistema, las necesidades de los usuarios, las limitaciones técnicas y los estándares de calidad que debe cumplir la plataforma. [cite: 776] [cite_start]Este documento servirá como guía fundamental para el diseño, desarrollo, validación y mantenimiento del proyecto. [cite: 777] [cite_start]La correcta implementación de estos requerimientos garantizará que GDI-IA no solo satisfaga las expectativas de los usuarios finales, sino que también aporte valor a nivel organizacional, aumentando la productividad, reduciendo errores de redacción y fortaleciendo los procesos de documentación en proyectos de software. [cite: 778] [cite_start]Con una visión a futuro, el proyecto tiene el potencial de escalar, integrar nuevas funcionalidades y adaptarse a las cambiantes necesidades del entorno tecnológico y académico. [cite: 779]

### [cite_start]RECOMENDACIONES [cite: 780]
[cite_start]Se recomienda asegurar una infraestructura tecnológica robusta para garantizar la disponibilidad y el rendimiento de la plataforma GDI-IA. [cite: 781] [cite_start]Esto incluye la optimización de la máquina virtual Ubuntu donde está alojada la aplicación y la base de datos, así como implementar sistemas de respaldo, monitoreo constante y protocolos de recuperación ante fallos. [cite: 782] [cite_start]La estabilidad de la infraestructura es fundamental para cumplir con los estándares de disponibilidad y calidad exigidos por los usuarios. [cite: 783]

[cite_start]Dado que el sistema depende de servicios externos de inteligencia artificial, se sugiere establecer procedimientos periódicos de actualización y verificación de las API integradas (como OpenAI y Hugging Face). [cite: 784] [cite_start]Mantener la compatibilidad con las últimas versiones, así como revisar las políticas de uso y costos de los proveedores, permitirá asegurar la continuidad del servicio y optimizar los recursos económicos destinados a estas integraciones. [cite: 785]

[cite_start]Para proteger la información ingresada y los documentos generados, se recomienda reforzar las medidas de seguridad en la plataforma. [cite: 786] [cite_start]Esto incluye el cifrado de datos en tránsito y en reposo, la gestión segura de las credenciales y claves API, la implementación de políticas de acceso basado en roles (RBAC) y la realización de auditorías de seguridad periódicas. [cite: 787] [cite_start]La confianza del usuario en la plataforma dependerá en gran medida de la protección efectiva de su información. [cite: 788]

[cite_start]Se aconseja planificar la escalabilidad del sistema desde sus primeras versiones. [cite: 789] [cite_start]A medida que crezca la demanda, será necesario optimizar el desempeño y considerar la integración de nuevas funcionalidades, como editores visuales de documentos, nuevos tipos de plantillas, o capacidades de personalización avanzada. [cite: 790] [cite_start]Esta planificación permitirá que el proyecto evolucione de manera ordenada y mantenga su relevancia en un entorno competitivo y en constante cambio. [cite: 791]