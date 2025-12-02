# Genera un sufijo aleatorio para asegurar nombres únicos
resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false
}

# Grupo de Recursos
resource "azurerm_resource_group" "rg" {
  name     = "rg-${var.base_name}-${random_string.suffix.result}"
  location = var.resource_group_location
}

resource "azurerm_key_vault" "kv" {
  name                = "kv-${var.base_name}-${random_string.suffix.result}"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "standard"
  
  # Esta política le da permisos a la identidad que ejecuta Terraform
  # para que pueda gestionar los secretos dentro de este Key Vault.
  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id # ID de tu Entidad de Servicio

    # Permisos necesarios para los secretos
    secret_permissions = [
      "Get",
      "List",
      "Set",
      "Delete",
    ]
  }
}

# Genera una contraseña segura y la guarda en Key Vault
resource "random_password" "sql_password" {
  length  = 16
  special = true
}

resource "azurerm_key_vault_secret" "sql_password_secret" {
  name         = "sql-admin-password"
  value        = random_password.sql_password.result
  key_vault_id = azurerm_key_vault.kv.id
}

# Servidor SQL
resource "azurerm_mssql_server" "server" {
  name                         = "sql-${var.base_name}-${random_string.suffix.result}"
  resource_group_name          = azurerm_resource_group.rg.name
  location                     = azurerm_resource_group.rg.location
  version                      = "12.0"
  administrator_login          = var.sql_admin_username
  administrator_login_password = random_password.sql_password.result
}

# Base de Datos SQL
resource "azurerm_mssql_database" "db" {
  name      = "db-${var.base_name}"
  server_id = azurerm_mssql_server.server.id
}

# Regla de Firewall para permitir acceso desde cualquier lugar
resource "azurerm_mssql_firewall_rule" "allow_all" {
  name             = "AllowAllWindowsAzureIps"
  server_id        = azurerm_mssql_server.server.id
  start_ip_address = "0.0.0.0"
  end_ip_address   = "0.0.0.0" # Regla especial para permitir servicios de Azure
}

# Recursos para la Function App (donde se ejecutará el script de Python)
resource "azurerm_storage_account" "sa" {
  name                     = "st${var.base_name}${random_string.suffix.result}"
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_service_plan" "plan" {
  name                = "plan-${var.base_name}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "Y1" # Plan de consumo sin costo (Dynamic)
}

resource "azurerm_linux_function_app" "func" {
  name                = "func-${var.base_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  storage_account_name       = azurerm_storage_account.sa.name
  storage_account_access_key = azurerm_storage_account.sa.primary_access_key
  service_plan_id            = azurerm_service_plan.plan.id

  site_config {
    application_stack {
      python_version = "3.9"
    }
  }
}

# Obtiene la configuración actual del cliente de Azure
data "azurerm_client_config" "current" {}