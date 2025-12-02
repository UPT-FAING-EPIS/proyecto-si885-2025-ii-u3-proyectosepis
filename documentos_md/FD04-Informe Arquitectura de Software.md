![Logo de la Universidad Privada de Tacna](https://github.com/user-attachments/assets/71c61858-a5ec-449e-b8cd-61a7a00f2ac7)

# [cite_start]UNIVERSIDAD PRIVADA DE TACNA [cite: 496]
## [cite_start]FACULTAD DE INGENIERÍA [cite: 497]
### [cite_start]Escuela Profesional de Ingeniería de Sistemas [cite: 498]

**Proyecto**
[cite_start]“Plataforma de Análisis de Despliegue de Proyectos” [cite: 499, 500]

**Curso:**
[cite_start]Inteligencia de Negocios [cite: 501, 502]

**Docente:**
Mag. [cite_start]Patrick Cuadros Quiroga [cite: 503, 504]

**Integrantes:**
* [cite_start]Ancco Suaña, Bruno Enrique (2023077472) [cite: 506]
* [cite_start]Loyola Vilca, Renzo Fernando (2021072615) [cite: 508]

**Tacna – Perú**
[cite_start]**2025** [cite: 509, 510]

---

### CONTROL DE VERSIONES
| Versión | Hecha por | Revisada por | Aprobada por | Fecha | Motivo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1.0 | "BEAS, CDAR, RFLV" | PCQ | - | 09/09/2025 | Versión 1.0 |
[cite_start][cite: 511]

---

## [cite_start]Sistema Plataforma de Análisis de Despliegue de Proyectos [cite: 512]
### [cite_start]Documento de Arquitectura de Software [cite: 513]

[cite_start]**Versión 1.0** [cite: 514]

---

### [cite_start]1. INTRODUCCIÓN [cite: 548]

#### 1.1. [cite_start]Propósito (Diagrama 4+1) [cite: 549]
[cite_start]Este documento presenta una visión estructurada de la arquitectura del sistema Generador de Documentación Impulsado por IA (GDI-IA), abordando los requerimientos funcionales y no funcionales desde una perspectiva de diseño basada en el modelo 4+1. [cite: 550] [cite_start]El objetivo es asegurar un equilibrio entre eficiencia, escalabilidad y portabilidad, proporcionando una plataforma web que automatice la generación de documentación estructurada mediante múltiples servicios de inteligencia artificial. [cite: 551]

#### 1.2. [cite_start]Alcance [cite: 552]
[cite_start]El sistema cubre: [cite: 553]
* [cite_start]Generación automatizada de documentos técnicos bajo formatos FD01–FD06. [cite: 554]
* [cite_start]Captura de información a través de formularios interactivos. [cite: 555]
* [cite_start]Integración de APIs para IA (redacción, generación de diagramas). [cite: 556]
* [cite_start]Exportación a formatos PDF y DOCX. [cite: 557]
* [cite_start]Almacenamiento en servidor FTP. [cite: 558]
* [cite_start]Gestión de versiones y plantillas. [cite: 559]

#### 1.3. [cite_start]Definición, siglas y abreviaturas [cite: 560]
| Término | Definición |
| :--- | :--- |
| API | Interfaz de Programación de Aplicaciones (Application Programming Interface) |
| DOCX | Formato de documento de Microsoft Word |
| FD01-FD06| Formatos documentales estandarizados para proyectos de software |
| IA | Inteligencia Artificial |
| PDF | Formato de Documento Portátil (Portable Document Format) |
[cite_start][cite: 561]

#### 1.4. [cite_start]Organización del documento [cite: 562]
[cite_start]Este informe detalla las vistas arquitectónicas del sistema: lógica, procesos, despliegue, casos de uso e implementación, seguidas de los atributos de calidad clave. [cite: 563]

### [cite_start]2. OBJETIVOS Y RESTRICCIONES ARQUITECTÓNICAS [cite: 564]

#### 2.1.1. [cite_start]Requerimientos Funcionales [cite: 569]
| ID | Descripcion | Prioridad |
| :--- | :--- | :--- |
| RegistroUsuario | El sistema web debe permitir la creacion de cuentas a los usuario nuevos | Alta |
| RegistroAdmin | El sistema web debe permitir la creacion de cuentas para administrador | Alta |
| ModuloInput | El sistema web debe tener un modulo para introducir la informacion clave dependiendo del formato escogido | Alta |
| SeleccionFormato | El sistema web debe permitir la seleccion del formato estandarizado para iniciar un nuevo documento | Alta |
| MultiIdioma | El sistema web debe permitir generar documentos en distintos idiomas si así lo permite el modelo IA configurado. | Alta |
| ModelosIA | El sistema web debe contener modelos de IA | Alta |
| GenerarPDF | El sistema web debe permitir la generacion documentos completos en formatos PDF siguiendo los formatos establecidos. | Alta |
| DescargaInmediata | El sistema web debe permitir la descarga del documento en el momento de su generacion | Alta |
| GenerarCitas | El sistema web debe generar las citas y bibliografia automaticamente segun el contenido extraidas de fuentes reales dependiendo del formato escogido | Alta |
| HistorialDocs | El sistema web debe almacenar un historial de los documentos realizados previamente | Alta |
| DescargaHistorial | El sistema web debe permitir la descarga de los documentos previos | Alta |
[cite_start][cite: 570]

#### 2.1.2. [cite_start]Requerimientos No Funcionales – Atributos de Calidad [cite: 571]
| ID | Descripcion | Prioridad |
| :--- | :--- | :--- |
| Debe integrar Login | Debe validar las credenciales | Alta |
| Accesibilidad multiplataforma | "La plataforma debe ser accesible desde navegadores web modernos, tanto en computadoras como en dispositivos móviles." | Alta |
| Seguridad de la información | "La información introducida por los usuarios y los documentos generados deben estar protegidos con autenticación, cifrado y control de acceso." | Alta |
| Escalabilidad | La plataforma debe estar preparada para escalar en cuanto a número de usuarios y tipos de formatos a futuro. | Alta |
| Compatibilidad con estándares documentales | El contenido generado debe cumplir con los estándares y formatos establecidos en los manuales institucionales. | Alta |
| Tolerancia a fallos | "En caso de fallo de una IA o servicio externo, el sistema debe mostrar un mensaje claro y permitir reintentar la generación." | Alta |
| Registro de errores (log) | El sistema debe registrar errores internos para fines de soporte y mejora continua. | Alta |
| Interfaz adaptativa (responsive) | "El diseño debe adaptarse correctamente a distintos tamaños de pantalla (teléfono, tablet, laptop, escritorio)." | Alta |
[cite_start][cite: 572]

#### [cite_start]Restricciones [cite: 573]
* [cite_start]El sistema debe ser accesible vía plataforma web desde computadoras o dispositivos móviles con conexión a internet. [cite: 574]
* [cite_start]Dependencia de servicios externos de IA para la generación de contenido. [cite: 575]
* [cite_start]El sistema no incluirá funcionalidades de edición manual posterior al documento generado. [cite: 576]

### [cite_start]3. REPRESENTACIÓN DE LA ARQUITECTURA DEL SISTEMA [cite: 577]

#### 3.1. [cite_start]Vista de Caso de uso [cite: 578]
[cite_start]Incluye: [cite: 579]
* [cite_start]Usuario interactúa con el sistema para iniciar sesión, seleccionar plantilla, proporcionar datos y generar documentos. [cite: 580]
* [cite_start]El sistema responde validando, consultando los modelos IA y devolviendo el documento generado. [cite: 581]

##### 3.1.1. [cite_start]Diagramas de Casos de uso [cite: 582]
[cite_start]![Diagrama de Casos de Uso](https://github.com/user-attachments/assets/b642e171-897b-40ef-8e3b-967b5f549c4c) [cite: 582]

#### 3.2. [cite_start]Vista Lógica [cite: 583]
[cite_start]![Vista Lógica del Sistema GDI-IA](https://github.com/user-attachments/assets/d9213166-5e04-4c57-acfd-b99f36e89098) [cite: 583]

##### 3.2.1. [cite_start]Diagrama de Subsistemas (paquetes) [cite: 584]
[cite_start]![Diagrama de Subsistemas](https://github.com/user-attachments/assets/b9ce6028-2b5d-40d2-995a-694553b478d5) [cite: 584]

##### 3.2.2. [cite_start]Diagrama de Secuencia (vista de diseño) [cite: 585]
[cite_start]**Login:** [cite: 586]
[cite_start]![Diagrama de Secuencia de Login](https://github.com/user-attachments/assets/37d7a469-8089-49dd-9a56-a010d95d660e) [cite: 586]
[cite_start]![Diagrama de Secuencia de Registro](https://github.com/user-attachments/assets/4ed07ffb-ec6a-4933-a3d1-43e742e97a47) [cite: 586]

##### 3.2.3. [cite_start]Diagrama de Objetos [cite: 587]
[cite_start]**Ingreso al Sistema del Generador de documentación impulsado por IA** [cite: 588]
[cite_start]![Diagrama de Objetos de Ingreso al Sistema](https://github.com/user-attachments/assets/9525c34e-090d-4009-acbe-f57ef518c7ed) [cite: 588]
[cite_start]Describe gráficamente cómo el usuario interactúa con el sistema para acceder a la interfaz de inicio de sesión, donde ingresa sus credenciales. [cite: 589] [cite_start]El sistema valida esta información a través del controlador(AuthController) y la clase de acceso a datos de login (User), permitiendo el ingreso al sistema. [cite: 590]

[cite_start]**Registro de Usuario dentro del Sistema** [cite: 591]
[cite_start]![Diagrama de Objetos de Registro de Usuario](https://github.com/user-attachments/assets/056ed871-3316-432d-9689-53e7d5da99fd) [cite: 591]
[cite_start]Describe gráficamente cómo el usuario interactúa con el sistema para registrase. [cite: 592] [cite_start]El usuario accede a la interfaz de registro, la cual envía la información al controlador(AuthController), que a su vez gestiona la interacción con la clase de registro de usuarios(User). [cite: 593]

##### 3.2.4. [cite_start]Diagrama de Clases [cite: 594]
[cite_start]![Diagrama de Clases](https://github.com/user-attachments/assets/44e4501a-1d54-469a-a8c4-c483a30a13e5) [cite: 594]

##### 3.2.5. [cite_start]Diagrama de Base de datos (relacional o no relacional) [cite: 595]
[cite_start]![Diagrama de Base de Datos 1](https://github.com/user-attachments/assets/b3469e35-a7b2-4d2a-8924-a3f1ed143719) [cite: 595]
[cite_start]![Diagrama de Base de Datos 2](https://github.com/user-attachments/assets/5c357f86-2ec1-409e-be4c-fc02a2491b2c) [cite: 595]

#### 3.3. [cite_start]Vista de Implementación (vista de desarrollo) [cite: 596]
[cite_start]![Vista de Implementación](https://github.com/user-attachments/assets/40673d31-4a4b-4b15-99d9-06488730bb5f) [cite: 596]

##### 3.3.1. [cite_start]Diagrama de arquitectura software (paquetes) [cite: 597]
[cite_start]![Diagrama de Arquitectura de Software](https://github.com/user-attachments/assets/26f8605d-6c8f-4a00-9830-4e3650239632) [cite: 597]

##### 3.3.2. [cite_start]Diagrama de arquitectura del sistema (Diagrama de componentes) [cite: 598]
[cite_start]![Diagrama de Arquitectura del Sistema](https://github.com/user-attachments/assets/fa89b33a-d698-4c80-87c2-d17e584f280e) [cite: 598]

#### 3.4. [cite_start]Vista de procesos [cite: 599]
* [cite_start]Procesos asincrónicos: llamada a IA, generación de documentos, almacenamiento en FTP. [cite: 600]
* [cite_start]Control de errores mediante logs y reintentos automáticos. [cite: 601]

##### 3.4.1. [cite_start]Diagrama de Procesos del sistema (diagrama de actividad) [cite: 602]
[cite_start]![Diagrama de Procesos del Sistema](https://github.com/user-attachments/assets/71c6ddca-3549-4786-8a03-bb7429188d3e) [cite: 602]

#### 3.5. [cite_start]Vista de Despliegue (vista física) [cite: 603]
[cite_start]![Vista de Despliegue](https://github.com/user-attachments/assets/b784a3c6-f761-4df2-892f-c06d863f6990) [cite: 603]

##### 3.5.1. [cite_start]Diagrama de despliegue [cite: 604]
[cite_start]![Diagrama de Despliegue](https://github.com/user-attachments/assets/9417937a-4298-4389-9bd7-5f725a72df9b) [cite: 604]

### [cite_start]4. ATRIBUTOS DE CALIDAD DEL SOFTWARE [cite: 605]
* [cite_start]**Escenario de Funcionalidad:** El sistema cumple con las funciones definidas de generación documental con IA, exportación, almacenamiento y gestión. [cite: 606, 607]
* [cite_start]**Escenario de Usabilidad:** Interfaz intuitiva accesible desde navegador moderno en móviles y PCs. [cite: 608, 609] [cite_start]Bajo tiempo de aprendizaje. [cite: 610]
* [cite_start]**Escenario de confiabilidad:** Seguridad en acceso y encriptación de datos. [cite: 611, 612] [cite_start]Logs de errores y recuperación ante fallos. [cite: 613]
* [cite_start]**Escenario de rendimiento:** Generación de documentos en tiempo real. [cite: 614, 615] [cite_start]Tiempos de respuesta óptimos gracias a la ejecución asincrónica. [cite: 616]
* [cite_start]**Escenario de mantenibilidad:** Arquitectura modular. [cite: 617, 618] [cite_start]Documentación clara del código y componentes. [cite: 619]
* [cite_start]**Otros Escenarios:** [cite: 620]
    * [cite_start]**Performance:** Alta capacidad de respuesta bajo carga moderada. [cite: 621]
    * [cite_start]**Escalabilidad:** Lista para crecer horizontalmente en la nube. [cite: 622]