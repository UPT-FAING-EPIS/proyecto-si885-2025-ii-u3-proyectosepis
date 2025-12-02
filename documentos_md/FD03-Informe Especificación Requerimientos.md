![Logo de la Universidad Privada de Tacna](https://github.com/user-attachments/assets/da29bb46-4c4f-4d39-9d93-376663f789d2)

# [cite_start]UNIVERSIDAD PRIVADA DE TACNA [cite: 324]
## [cite_start]FACULTAD DE INGENIERÍA [cite: 325]
### [cite_start]Escuela Profesional de Ingeniería de Sistemas [cite: 326]

**Proyecto**
[cite_start]“Plataforma de Análisis de Despliegue de Proyectos” [cite: 327, 328]

**Curso:**
[cite_start]Inteligencia de Negocios [cite: 329, 330]

**Docente:**
Mag. [cite_start]Patrick Cuadros Quiroga [cite: 331, 332]

**Integrantes:**
* [cite_start]Ancco Suaña, Bruno Enrique (2023077472) [cite: 334]
* [cite_start]Loyola Vilca, Renzo Fernando (2021072615) [cite: 336]

**Tacna – Perú**
[cite_start]**2025** [cite: 337, 338]

---

### CONTROL DE VERSIONES
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1.0 | "BEAS, CDAR, RFLV" | PCQ | - | 09/09/2025 | Versión 1.0 |
[cite_start][cite: 339]

---

## [cite_start]Sistema Plataforma de Análisis de Despliegue de Proyectos [cite: 340]
### [cite_start]Documento de Visión [cite: 341]

[cite_start]**Versión 1.0** [cite: 342]

---

### Índice General
* [1. [cite_start]Introducción](#1-introducción) [cite: 345]
    * [a. [cite_start]Propósito](#a-propósito) [cite: 346]
    * [b. [cite_start]Alcance](#b-alcance) [cite: 347]
    * [c. [cite_start]Definiciones, Siglas y Abreviaturas](#c-definiciones-siglas-y-abreviaturas) [cite: 348]
    * [d. [cite_start]Referencias](#d-referencias) [cite: 349]
    * [e. [cite_start]Visión General](#e-visión-general) [cite: 350]
* [2. [cite_start]Posicionamiento](#2-posicionamiento) [cite: 351]
    * [a. [cite_start]Oportunidad de negocio](#a-oportunidad-de-negocio) [cite: 352]
    * [b. [cite_start]Definición del problema](#b-definición-del-problema) [cite: 353]
* [3. [cite_start]Descripción de los interesados y usuarios](#3-descripción-de-los-interesados-y-usuarios) [cite: 354]
* [4. [cite_start]Vista General del Producto](#4-vista-general-del-producto) [cite: 361]
* [5. [cite_start]Características del producto](#5-características-del-producto) [cite: 367]
* [6. [cite_start]Restricciones](#6-restricciones) [cite: 368]
* [7. [cite_start]Rangos de calidad](#7-rangos-de-calidad) [cite: 369]
* [8. [cite_start]Precedencia y Prioridad](#8-precedencia-y-prioridad) [cite: 370]
* [9. [cite_start]Otros requerimientos del producto](#9-otros-requerimientos-del-producto) [cite: 371]
* [10. [cite_start]Conclusiones](#10-conclusiones) [cite: 376]
* [11. [cite_start]Recomendaciones](#11-recomendaciones) [cite: 377]
* [12. [cite_start]Webgrafía](#12-webgrafía) [cite: 378]

---

### [cite_start]1. Introducción [cite: 379]

#### a. [cite_start]Propósito [cite: 380]
[cite_start]El propósito de este proyecto es diseñar e implementar una plataforma web de análisis y Business Intelligence (BI) capaz de identificar, procesar y visualizar las tecnologías de despliegue utilizadas en los proyectos de software de los repositorios de la comunidad académica de la Universidad Privada de Tacna. [cite: 381] [cite_start]La solución permitirá a los directivos y docentes obtener una visión clara y basada en datos del ecosistema tecnológico de la institución, facilitando la toma de decisiones estratégicas. [cite: 382]

#### b. [cite_start]Alcance [cite: 383]
[cite_start]El sistema abarca: [cite: 384]
* [cite_start]Un módulo de conexión segura a las APIs de servicios de repositorios (ej. GitHub, GitLab) mediante autenticación OAuth. [cite: 385]
* [cite_start]Un sistema de análisis (parser) para examinar archivos de configuración y metadatos de los proyectos. [cite: 386]
* [cite_start]El almacenamiento de los datos analíticos en una base de datos relacional. [cite: 387]
* [cite_start]La presentación de los datos en un dashboard interactivo con filtros y gráficos. [cite: 388]
* [cite_start]Almacenamiento del historial de análisis para observar tendencias en el tiempo. [cite: 389]
[cite_start]No incluye el análisis de la calidad, seguridad o lógica interna del código fuente de los proyectos. [cite: 390]

#### c. [cite_start]Definiciones, Siglas y Abreviaturas [cite: 391]
* [cite_start]**BI:** Business Intelligence (Inteligencia de Negocios). [cite: 392]
* [cite_start]**API:** Application Programming Interface (Interfaz de Programación de Aplicaciones). [cite: 393]
* [cite_start]**Dashboard:** Panel de control visual e interactivo. [cite: 394]
* [cite_start]**Parser:** Analizador sintáctico diseñado para extraer información de archivos de texto. [cite: 395]
* [cite_start]**OAuth:** Open Authorization, un estándar para la delegación segura de acceso. [cite: 396]

#### d. [cite_start]Referencias [cite: 397]
* [cite_start]Documentación oficial de las APIs de GitHub y GitLab. [cite: 398]
* [cite_start]Guías de buenas prácticas para el desarrollo de dashboards de BI. [cite: 399]
* [cite_start]Documentación de librerías de análisis de datos (ej. Pandas para Python). [cite: 400]
* [cite_start]Documentación de librerías de visualización de datos (ej. Chart.js, D3.js). [cite: 401]

#### e. [cite_start]Visión General [cite: 402]
[cite_start]El proyecto busca convertirse en una herramienta estratégica interna para la Facultad de Ingeniería y la dirección de la universidad. [cite: 403] [cite_start]Facilitará la toma de decisiones académicas y administrativas mediante la provisión de datos claros y actualizados sobre el panorama tecnológico de la institución. [cite: 404] [cite_start]La visión a largo plazo es expandir el análisis a otras facultades, integrar más fuentes de datos y consolidarse como el sistema central de inteligencia académica y tecnológica de la universidad. [cite: 405]

### [cite_start]2. Posicionamiento [cite: 406]
[cite_start]La Plataforma de Análisis de Despliegue se posiciona como una solución de Inteligencia de Negocios académica, enfocada en resolver una necesidad interna de la Universidad Privada de Tacna. [cite: 407] [cite_start]Su valor no radica en competir en un mercado, sino en proporcionar una ventaja estratégica al permitir una gestión académica informada y moderna. [cite: 408]

#### a. [cite_start]Oportunidad de negocio [cite: 409]
[cite_start]Actualmente, la universidad carece de un mecanismo para conocer las tecnologías que sus estudiantes aplican en la práctica. [cite: 410] [cite_start]Esta falta de visibilidad representa una oportunidad estratégica para dejar de tomar decisiones curriculares y de inversión basadas en suposiciones y empezar a usar datos reales del propio ecosistema universitario. [cite: 411]

#### b. [cite_start]Definición del problema [cite: 412]
[cite_start]La dirección académica y el cuerpo docente de la Facultad de Ingeniería no tienen datos centralizados sobre qué lenguajes de programación, servicios en la nube y plataformas de despliegue son más utilizados por los estudiantes en sus proyectos. [cite: 413] [cite_start]Esto dificulta la actualización de los planes de estudio, la asignación de recursos y la identificación de tendencias tecnológicas emergentes dentro de la propia institución. [cite: 414]

### [cite_start]3. Descripción de los interesados y usuarios [cite: 415]
* [cite_start]**Resumen de los interesados:** Los interesados en el proyecto incluyen a los directivos de la Facultad de Ingeniería (Decano, Directores de Carrera), la administración de TI de la universidad y los docentes del área de tecnología, quienes buscan mejorar la calidad y pertinencia de la formación. [cite: 416, 417]
* [cite_start]**Resumen de los usuarios:** Los usuarios principales del sistema serán directivos académicos, coordinadores, docentes y alumnos, quienes consultarán el dashboard para la toma de decisiones. [cite: 419] [cite_start]Los estudiantes serán beneficiarios indirectos al recibir una educación más actualizada y también podrán ser usuarios secundarios para explorar tendencias. [cite: 420]
* [cite_start]**Entorno de usuario:** El entorno de usuario será una plataforma web interna, accesible desde navegadores modernos en dispositivos de escritorio, que requerirá autenticación con credenciales universitarias. [cite: 422]
* [cite_start]**Perfiles de los interesados:** [cite: 423]
    * [cite_start]Directivos Académicos (Decano, Directores): Interesados en datos agregados para la planificación estratégica, actualización curricular y justificación de inversiones. [cite: 424]
    * [cite_start]Administradores de TI: Buscan entender las tecnologías más demandadas para planificar el soporte y la infraestructura. [cite: 425]
    * [cite_start]Docentes: Interesados en conocer las herramientas que usan sus alumnos para adaptar los contenidos de sus cursos y proponer nuevos talleres. [cite: 426]
    * [cite_start]Alumnos de la universidad [cite: 427]
* [cite_start]**Perfiles de los Usuarios:** [cite: 428]
    * [cite_start]Director de Carrera: Necesita visualizar las tecnologías más populares en su carrera para evaluar la pertinencia del plan de estudios. [cite: 429]
    * [cite_start]Docente de Programación: Quiere saber qué frameworks o servicios en la nube utilizan los estudiantes para orientar mejor sus proyectos finales. [cite: 430]
    * [cite_start]Estudiante: Desea explorar qué tecnologías son tendencia entre sus compañeros para orientar su propio aprendizaje. [cite: 431]
* [cite_start]**Necesidades de los interesados y usuarios:** [cite: 432]
    * [cite_start]Visualización clara y rápida de las tendencias tecnológicas. [cite: 433]
    * [cite_start]Capacidad de filtrar datos por carrera, curso o periodo académico. [cite: 434]
    * [cite_start]Acceso a datos históricos para comparar la evolución tecnológica. [cite: 435]
    * [cite_start]Interfaz intuitiva que no requiera conocimientos técnicos en BI. [cite: 436]
    * [cite_start]Generación de reportes visuales para presentaciones institucionales. [cite: 437]
    * [cite_start]Confianza en la seguridad y privacidad de los datos analizados. [cite: 438]

### [cite_start]4. Vista General del Producto [cite: 439]
* [cite_start]**Perspectiva del producto:** El sistema será una plataforma web interna, desarrollada preferentemente en Python por sus capacidades de análisis de datos, con una arquitectura modular. [cite: 441] [cite_start]Utilizará una base de datos MySQL para la gestión de los datos analíticos. [cite: 442]
* [cite_start]**Resumen de capacidades:** [cite: 443]
    * [cite_start]Conexión segura a APIs de repositorios (GitHub) mediante OAuth. [cite: 444]
    * [cite_start]Análisis automatizado de archivos de configuración para identificar tecnologías. [cite: 445]
    * [cite_start]Dashboard interactivo con múltiples gráficos y filtros dinámicos. [cite: 446]
    * [cite_start]Generación de reportes visuales en formato PDF o imagen. [cite: 447]
* [cite_start]**Suposiciones y dependencias:** [cite: 448]
    * [cite_start]Disponibilidad constante de las APIs de los servicios de repositorios. [cite: 449]
    * [cite_start]Acceso a internet para que el sistema pueda conectarse a las APIs. [cite: 450]
    * [cite_start]Consentimiento de los estudiantes y docentes para permitir el análisis de sus repositorios. [cite: 451]
* [cite_start]**Costos y precios:** El proyecto no contempla un modelo de precios, ya que es una herramienta de uso interno para la Universidad Privada de Tacna. [cite: 453] [cite_start]Los costos están asociados al desarrollo (enmarcado como proyecto de curso) y al mantenimiento mínimo del servidor donde se alojará, los cuales serán asumidos por la facultad. [cite: 454]
* [cite_start]**Licenciamiento e instalación:** El sistema se distribuirá bajo un modelo SaaS (Software as a Service), alojado en la nube. [cite: 456] [cite_start]No requiere instalación local por parte del usuario. [cite: 457] [cite_start]Los términos de licencia dependerán del perfil del cliente: usuario individual, empresa o institución educativa. [cite: 458]

### [cite_start]5. Características del producto [cite: 459]
* [cite_start]**Módulo de Conexión a APIs de Git:** Integración segura para la lectura de datos de repositorios. [cite: 460]
* [cite_start]**Motor de Análisis (Parser):** Lógica para identificar tecnologías a partir de archivos clave. [cite: 461]
* [cite_start]**Dashboard de BI:** Interfaz principal para la visualización de datos con gráficos interactivos. [cite: 462]
* [cite_start]**Sistema de Autenticación:** Inicio de sesión único con credenciales de la universidad para usuarios autorizados. [cite: 463]

### [cite_start]6. Restricciones [cite: 464]
* [cite_start]Dependencia de la disponibilidad y políticas de las APIs externas (GitHub, GitLab). [cite: 465]
* [cite_start]El análisis se limita a la información declarada en los archivos de configuración, no pudiendo inferir tecnologías no especificadas. [cite: 466]
* [cite_start]El acceso a los datos depende del consentimiento de la comunidad universitaria. [cite: 467]

### [cite_start]7. Rangos de calidad [cite: 468]
* [cite_start]**Disponibilidad del sistema:** 99% de uptime mensual mínimo garantizado. [cite: 469]
* [cite_start]**Precisión en la generación:** Alta coherencia estructural y gramatical en los documentos generados. [cite: 470]
* [cite_start]**Interfaz de usuario:** Interfaz intuitiva, responsiva, accesible desde dispositivos móviles y de escritorio. [cite: 471]

### [cite_start]8. Precedencia y Prioridad [cite: 472]
* [cite_start]Prioridad alta en el desarrollo de módulos de captura de datos y generación de documentos. [cite: 473]
* [cite_start]La integración con APIs será desarrollada en paralelo con énfasis en la escalabilidad. [cite: 474]
* [cite_start]Funcionalidades como el historial y las descargas se implementarán en fases posteriores. [cite: 475]

### [cite_start]9. Otros requerimientos del producto [cite: 476]
* [cite_start]**Estándares legales:** Cumplimiento de normativas de protección de datos personales como la GDPR o la Ley de Protección de Datos local. [cite: 477, 478]
* [cite_start]**Estándares de comunicación:** Uso de canales seguros (HTTPS), y encriptación de datos sensibles. [cite: 479, 480]
* [cite_start]**Estándares de cumplimiento de la plataforma:** Soporte para navegadores modernos, accesibilidad (WCAG) y adaptabilidad a diferentes resoluciones. [cite: 481, 482]
* [cite_start]**Estándares de calidad y seguridad:** Pruebas de integración, pruebas de carga y validaciones de seguridad periódicas. [cite: 483, 484]

### [cite_start]10. Conclusiones [cite: 485]
[cite_start]El proyecto "Plataforma de Análisis de Despliegue" representa una solución estratégica e innovadora para abordar la necesidad de la Universidad Privada de Tacna de comprender su propio ecosistema tecnológico. [cite: 486] [cite_start]A través de una plataforma de BI, se busca transformar la toma de decisiones, pasando de un modelo basado en suposiciones a uno basado en datos reales. [cite: 487] [cite_start]El sistema no solo optimizará la planificación académica, sino que también potenciará la calidad de la educación, asegurando su relevancia en un sector en constante cambio. [cite: 488]

### [cite_start]11. Recomendaciones [cite: 489]
* [cite_start]**Monitoreo constante de las APIs externas:** Es fundamental vigilar cambios en las políticas o funcionalidades de las APIs de GitHub/GitLab. [cite: 490]
* [cite_start]**Políticas claras de uso y protección de datos:** Implementar y comunicar una política de privacidad clara para generar confianza en la comunidad universitaria. [cite: 491]
* [cite_start]**Capacitación a los usuarios finales:** Realizar breves talleres para directivos y docentes sobre cómo interpretar los datos del dashboard. [cite: 492]
* [cite_start]**Plan de Mantenimiento y Sostenibilidad:** Establecer un plan de mantenimiento técnico para asegurar la continuidad y actualización de la plataforma a largo plazo. [cite: 493]
* [cite_start]**Arquitectura escalable:** Diseñar la arquitectura considerando el posible crecimiento en el volumen de datos y usuarios. [cite: 494]
* [cite_start]**(Mantener Pruebas exhaustivas y Retroalimentación)** la retroalimentación del mercado y las necesidades de los usuarios. [cite: 495]