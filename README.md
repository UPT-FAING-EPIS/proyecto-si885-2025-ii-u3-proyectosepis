# 📊 Plataforma de Análisis de Despliegue de Proyectos

## 🎓 Universidad Privada de Tacna
**Facultad de Ingeniería - Escuela Profesional de Ingeniería de Sistemas**

**Curso:** Inteligencia de Negocios  
**Docente:** Mag. Patrick Cuadros Quiroga

## 👥 Integrantes del Equipo
- **Ancco Suaña, Bruno Enrique** (2023077472)
- **Loyola Vilca, Renzo Fernando** (2021072615)

---

## 📎 Enlaces del Proyecto

- 🔗 **Dashboard Power BI:** [Dashboard-Proyectos](https://app.powerbi.com/links/UT-MLQnWHr?ctid=b6b466ee-468d-4011-b9fc-fbdcf82ac90a&pbi_source=linkShare)
- 🔗 **Repositorio GitHub:** [Proyectos-EPIS](https://github.com/UPT-FAING-EPIS/proyecto-si885-2025-ii-u3-proyectosepis)
- 🔗 **Drive de Videos:** [Videos-EPIS](https://drive.google.com/drive/folders/1pSFP-eRDIsdfwNtJrib-TK4bpZkAZl3V?usp=sharing)

---

## ❗ Problemática

Actualmente, la **Escuela Profesional de Ingeniería de Sistemas** de la Universidad Privada de Tacna no dispone de un método sistemático para conocer qué herramientas, lenguajes y plataformas de despliegue están siendo utilizados en la práctica por sus estudiantes.

Las decisiones sobre:
- ¿Qué tecnologías enseñar en el plan de estudios?
- ¿Qué convenios con proveedores de nube promover (AWS Educate, Azure for Students)?
- ¿Dónde enfocar los recursos de capacitación?

Se basan en **suposiciones generales del mercado** y no en **datos concretos del propio ecosistema universitario**.

---

## 🎯 Objetivo General

Desarrollar un **Dashboard de Business Intelligence** que permita analizar y visualizar las tecnologías y servicios de despliegue utilizados en los proyectos de software alojados en los repositorios de la comunidad de la Escuela Profesional de Ingeniería de Sistemas de la Universidad Privada de Tacna.

---

## ✅ Objetivos Específicos

1. **Visualizar un panorama general** de las tecnologías de despliegue más utilizadas
2. **Explorar proyectos de manera individual** para conocer sus detalles técnicos
3. **Filtrar los proyectos por curso** para analizar tendencias específicas
4. **Identificar las tecnologías de despliegue específicas** utilizadas en cada proyecto

---

## 🛠️ Tecnologías Utilizadas

### Backend & Pipeline de Datos
- **Python 🐍** → Extracción, análisis y carga de datos desde la API de GitHub
  - `requests` → Conexiones a la API
  - `python-dotenv` → Gestión segura de credenciales
  - `psycopg2` / `pyodbc` → Carga de datos a la base de datos SQL

### APIs & Integración
- **GitHub API** 🔗 → Acceso a repositorios, metadatos y contenido de archivos

### Infraestructura & Almacén de Datos
- **Cloud Platform** ☁️ (ej. Azure, AWS, GCP)
- **Base de Datos SQL** 🗄️ (ej. PostgreSQL, Azure SQL) → Almacén de datos central
- **Terraform** 🏗️ → Infraestructura como código para crear los recursos en la nube

### CI/CD & Automatización
- **GitHub Actions** ⚙️ → Orquestación del despliegue de infraestructura y ejecución periódica del pipeline

### Visualización & Dashboard
- **Microsoft Power BI** 📊 → Dashboard interactivo principal

---

## 📡 Metodología de Análisis

### 1. **Conexión Segura a Repositorios**
- Implementación de autenticación segura con Tokens de Acceso Personal de GitHub.
- Acceso de solo lectura a metadatos y contenido de archivos públicos de la organización.

### 2. **Análisis Automatizado de Proyectos**
El pipeline de Python analiza múltiples indicadores en cada repositorio para obtener una visión 360° de las tecnologías utilizadas.
```python
# Indicadores y archivos de configuración analizados:
# 1. Nombres de archivo de configuración
- Dockerfile, docker-compose.yml
- vercel.json, netlify.toml
- Procfile, render.yaml
- .travis.yml, Jenkinsfile, .circleci/
- Chart.yaml, Pulumi.yaml
- *.tf, *.csproj
- .github/workflows/*.yml

# 2. Contenido de archivos de dependencias
- package.json          # Node.js (NPM/Yarn)
- requirements.txt      # Python (pip)
- pom.xml               # Java (Maven)
- build.gradle, .kts    # Java (Gradle)
- composer.json         # PHP
- go.mod                # Go

# 3. Contenido de archivos README y Workflows
- Búsqueda de palabras clave (ej. "aws s3", "firebase deploy")
```

### 3. **Identificación de Tecnologías de Despliegue**
- **Servicios en la Nube:** AWS, Azure, Google Cloud, DigitalOcean
- **Plataformas PaaS:** Heroku, Vercel, Netlify, Render
- **Contenedores y Orquestación:** Docker, Kubernetes, Helm
- **Infraestructura como Código:** Terraform, Pulumi, Ansible
- **CI/CD:** GitHub Actions, CircleCI, Travis CI, Jenkins

### 4. **Procesamiento y Almacenamiento**
- Limpieza y normalización de los datos extraídos por el script de Python.
- Carga automatizada y estructurada en una **Base de Datos SQL**.

### 5. **Visualización Interactiva**
- El dashboard principal en Power BI se conecta directamente a la Base de Datos SQL.
- Se configuran actualizaciones programadas o DirectQuery para asegurar que los datos estén siempre frescos.

---

## 📈 Ejemplo de Visualizaciones

### Dashboard Principal en Power BI:
1. **Gráfico de barras** → Tecnologías de despliegue más utilizadas
2. **Gráfico circular** → Distribución de servicios en la nube
3. **Tabla interactiva** → Ranking de proyectos por tecnología
4. **Filtros dinámicos** → Por tecnología

---

## 🚀 Resultados Esperados

### Para la Institución:
- **Toma de decisiones informada** sobre actualización curricular
- **Optimización de recursos** en licencias y convenios tecnológicos
- **Identificación de tendencias** emergentes en el ecosistema universitario

### Para Estudiantes:
- **Visibilidad de tendencias** tecnológicas entre compañeros
- **Orientación para aprendizaje** basada en datos reales
- **Inspiración para proyectos** mediante exploración de casos exitosos

### Para Docentes:
- **Adaptación de contenidos** según herramientas realmente utilizadas
- **Propuesta de nuevos talleres** basada en demanda real
- **Evaluación del impacto** de la enseñanza en proyectos prácticos

---

## 📌 Roadmap Futuro

- **Recomendaciones personalizadas** → Sugerencias de tecnologías por perfil
- **Análisis multi-facultad** → Expandir a otras carreras de ingeniería