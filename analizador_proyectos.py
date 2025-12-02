import os
# from xmlrpc import server #<- Esta importación no era necesaria
import requests
import pyodbc
from dotenv import load_dotenv
import time
import base64
# import datetime #<- Ya no es necesario para este enfoque

# --- CONFIGURACIÓN INICIAL ---
load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

if not TOKEN or not DB_HOST:
    raise ValueError("Asegúrate de configurar GITHUB_TOKEN y las variables de la BD en el archivo .env")

ORG = "UPT-FAING-EPIS"
HEADERS = {"Authorization": f"token {TOKEN}"}

# --- (Funciones de análisis sin cambios) ---
def get_repo_files(owner, repo_name, path=""):
    contents_url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{path}"
    try:
        response = requests.get(contents_url, headers=HEADERS)
        if response.status_code == 404: return []
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener archivos de {repo_name}/{path}: {e}")
        return []

def get_file_content(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        content_base64 = response.json()['content']
        decoded_content = base64.b64decode(content_base64).decode('utf-8')
        return decoded_content
    except (requests.exceptions.RequestException, KeyError, UnicodeDecodeError) as e:
        print(f"Error al leer o decodificar contenido: {e}")
        return ""

def analyze_tech_from_content(content):
    found_techs = set()
    content_lower = content.lower()
    if any(keyword in content_lower for keyword in ["aws s3", "aws ecr", "aws lambda", "amazonaws.com", "aws-actions/"]): found_techs.add("AWS")
    if "firebase deploy" in content_lower: found_techs.add("Firebase")
    if any(keyword in content_lower for keyword in ["gcloud app deploy", "cloud.google.com", "google-github-actions/"]): found_techs.add("Google Cloud")
    if any(keyword in content_lower for keyword in ["azure webapp up", "azure/login"]): found_techs.add("Azure")
    if "vercel" in content_lower: found_techs.add("Vercel")
    if "netlify" in content_lower: found_techs.add("Netlify")
    if "heroku/deploy" in content_lower: found_techs.add("Heroku")
    if "digitalocean/app-deploy" in content_lower: found_techs.add("DigitalOcean")
    if "hashicorp/setup-terraform" in content_lower or "terraform apply" in content_lower: found_techs.add("Terraform")
    if "kubectl apply" in content_lower: found_techs.add("Kubernetes")
    return found_techs

def analyze_deployment_tech(root_files_json):
    file_list = [item["name"] for item in root_files_json]
    techs = set()
    if "vercel.json" in file_list: techs.add("Vercel")
    if "netlify.toml" in file_list: techs.add("Netlify")
    if "serverless.yml" in file_list or ".aws" in file_list: techs.add("AWS")
    if "app.yaml" in file_list or "cloudbuild.yaml" in file_list: techs.add("Google Cloud")
    if "azure-pipelines.yml" in file_list or "azuredeploy.json" in file_list: techs.add("Azure")
    if "Procfile" in file_list: techs.add("Heroku")
    if "render.yaml" in file_list: techs.add("Render")
    if ".do" in file_list: techs.add("DigitalOcean")
    if "Dockerfile" in file_list or "docker-compose.yml" in file_list: techs.add("Docker")
    if "k8s" in file_list or "kubernetes" in file_list: techs.add("Kubernetes")
    if "Chart.yaml" in file_list: techs.add("Helm")
    if any(f.endswith(".tf") for f in file_list): techs.add("Terraform")
    if "Pulumi.yaml" in file_list: techs.add("Pulumi")
    if "ansible" in file_list or "playbooks" in file_list: techs.add("Ansible")
    if ".github" in file_list: techs.add("GitHub Actions")
    if ".circleci" in file_list: techs.add("CircleCI")
    if ".travis.yml" in file_list: techs.add("Travis CI")
    if "Jenkinsfile" in file_list: techs.add("Jenkins")
    return techs

def analyze_dependencies(root_files_json):
    techs = set()
    dependency_files = {
        "package.json": "JavaScript",
        "requirements.txt": "Python",
        "pom.xml": "Java (Maven)",
        "go.mod": "Go",
        "build.gradle": "Java (Gradle)",
        "build.gradle.kts": "Java (Gradle)",
        "composer.json": "PHP",
    }

    is_csproj_present = any(f.get("name", "").endswith(".csproj") for f in root_files_json)

    for file_info in root_files_json:
        file_name = file_info.get("name")
        if file_name in dependency_files:
            print(f"--- Analizando dependencias en '{file_name}'...")
            content = get_file_content(file_info.get("url", ""))
            if not content: continue

            content_lower = content.lower()

            if file_name == "package.json":
                if any(pkg in content_lower for pkg in ['"@aws-sdk/', '"aws-sdk"']): techs.add("AWS")
                if any(pkg in content_lower for pkg in ['"@google-cloud/', '"gcp-metadata"']): techs.add("Google Cloud")
                if any(pkg in content_lower for pkg in ['"@azure/']): techs.add("Azure")

            elif file_name == "requirements.txt":
                if "boto3" in content_lower: techs.add("AWS")
                if "google-cloud" in content_lower: techs.add("Google Cloud")
                if "azure-" in content_lower: techs.add("Azure")

            elif file_name == "pom.xml":
                if "com.amazonaws" in content_lower: techs.add("AWS")
                if "com.google.cloud" in content_lower: techs.add("Google Cloud")
                if "com.microsoft.azure" in content_lower: techs.add("Azure")

            elif file_name == "go.mod":
                if "github.com/aws/aws-sdk-go" in content_lower: techs.add("AWS")
                if "cloud.google.com/go" in content_lower: techs.add("Google Cloud")
                if "github.com/azure/azure-sdk-for-go" in content_lower: techs.add("Azure")

            elif file_name.startswith("build.gradle"):
                if "com.amazonaws" in content_lower or "aws.sdk" in content_lower: techs.add("AWS")
                if "com.google.cloud" in content_lower: techs.add("Google Cloud")
                if "com.microsoft.azure" in content_lower: techs.add("Azure")

            elif file_name == "composer.json":
                if '"aws/aws-sdk-php"' in content_lower: techs.add("AWS")
                if '"google/cloud"' in content_lower: techs.add("Google Cloud")
                if '"microsoft/azure' in content_lower: techs.add("Azure")

    if is_csproj_present:
        csproj_file_info = next((f for f in root_files_json if f.get("name", "").endswith(".csproj")), None)
        if csproj_file_info:
            print(f"--- Analizando dependencias en '{csproj_file_info.get('name')}'...")
            content = get_file_content(csproj_file_info.get("url", ""))
            if content:
                content_lower = content.lower()
                if 'packagereference include="awssdk' in content_lower: techs.add("AWS")
                if 'packagereference include="google.cloud' in content_lower: techs.add("Google Cloud")
                if 'packagereference include="azure.' in content_lower: techs.add("Azure")

    return techs

# --- SCRIPT PRINCIPAL ---
def main():
    print(f"Buscando repositorios en la organización: {ORG}...")

    repos_api_url = f"https://api.github.com/orgs/{ORG}/repos"
    all_repos_data = []
    page = 1

    while True:
        response = requests.get(repos_api_url, headers=HEADERS, params={"per_page": 100, "page": page})
        if response.status_code != 200: break
        data = response.json()
        if not data: break

        print(f"Página {page} obtenida, procesando {len(data)} repositorios...")

        for repo in data:
            repo_name = repo["name"]

            if "proyecto" not in repo_name.lower():
                continue

            if not repo.get("language"):
                continue

            print(f"\nAnalizando '{repo_name}'...")

            root_files_json = get_repo_files(ORG, repo_name)
            detected_techs = analyze_deployment_tech(root_files_json)
            detected_techs.update(analyze_dependencies(root_files_json))

            readme_file = next((f for f in root_files_json if f['name'].lower() == 'readme.md'), None)
            if readme_file:
                print(f"--- Leyendo README.md en '{repo_name}'...")
                readme_content = get_file_content(readme_file['url'])
                if readme_content:
                    detected_techs.update(analyze_tech_from_content(readme_content))

            if "GitHub Actions" in detected_techs:
                workflow_files = get_repo_files(ORG, repo_name, path=".github/workflows")
                for wf_file in workflow_files:
                    if wf_file['name'].endswith(('.yml', '.yaml')):
                        print(f"--- Leyendo workflow '{wf_file['name']}' en '{repo_name}'...")
                        workflow_content = get_file_content(wf_file['url'])
                        if workflow_content:
                            detected_techs.update(analyze_tech_from_content(workflow_content))

            # --- CAMBIO: Añadimos la fecha de creación al diccionario ---
            all_repos_data.append({
                "Nombre": repo["name"], # Usar repo["name"] directamente
                "URL": repo["html_url"],
                "Lenguaje Principal": repo.get("language", "N/A"),
                "Tecnologías": sorted(list(detected_techs)),
                "Fecha Creacion": repo["created_at"] # <-- CAMBIO AÑADIDO
            })
            time.sleep(1)

        page += 1

    if not all_repos_data:
        print("No se encontró ningún repositorio que cumpla con los filtros.")
        return

    # ### INICIO DE LA SECCIÓN MODIFICADA PARA CARGA CON FECHA DE CREACIÓN ###
    conn = None
    try:
        # Preparar la cadena de conexión para Azure SQL
        server = os.getenv("DB_HOST")
        database = os.getenv("DB_NAME")
        username = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")

        print("\nConectando a la base de datos Azure SQL...")
        conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER=tcp:{server}.database.windows.net,1433;DATABASE={database};UID={username};PWD={password}'
        conn = pyodbc.connect(conn_str)

        cursor = conn.cursor()

        # Opcional: Limpiar la tabla antes de insertar si solo quieres el estado más reciente
        # print("Limpiando tabla de análisis anterior...")
        # cursor.execute("TRUNCATE TABLE analisis_repositorios;") # Descomenta si quieres borrar antes

        print(f"Insertando o actualizando {len(all_repos_data)} registros en la base de datos...")
        for repo_data in all_repos_data:
            tecnologias_str = ", ".join(repo_data["Tecnologías"])

            # --- CAMBIO: Procesar y usar la fecha de creación ---
            fecha_creacion_str = repo_data["Fecha Creacion"]
            # Convertimos la fecha de ISO 8601 (ej: "2024-01-15T10:30:00Z") a solo fecha (YYYY-MM-DD)
            fecha_creacion_date = fecha_creacion_str.split('T')[0]
            # --- FIN CAMBIO ---

            # El comando MERGE sigue siendo útil para actualizar si el repo ya existe
            insert_query = """
            MERGE INTO analisis_repositorios AS target
            USING (VALUES (?, ?, ?, ?, ?)) AS source (nombre_repo, url_repo, lenguaje_principal, tecnologias, fecha_creacion_repo)
            ON target.nombre_repo = source.nombre_repo
            WHEN MATCHED THEN
                UPDATE SET
                    url_repo = source.url_repo,
                    lenguaje_principal = source.lenguaje_principal,
                    tecnologias = source.tecnologias
                    -- No actualizamos fecha_creacion_repo porque es fija
            WHEN NOT MATCHED THEN
                INSERT (nombre_repo, url_repo, lenguaje_principal, tecnologias, fecha_creacion_repo)
                VALUES (source.nombre_repo, source.url_repo, source.lenguaje_principal, source.tecnologias, source.fecha_creacion_repo);
            """
            cursor.execute(insert_query, (
                repo_data["Nombre"],
                repo_data["URL"],
                repo_data["Lenguaje Principal"],
                tecnologias_str,
                fecha_creacion_date # Usamos la fecha de creación procesada
            ))

        conn.commit()
        print("¡Carga de datos a la base de datos completada con éxito!")

    except pyodbc.Error as e:
        print(f"Error en la base de datos: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Conexión a la base de datos cerrada.")
    ### FIN DE LA SECCIÓN MODIFICADA ###


if __name__ == "__main__":
    main()