output "sql_server_name" {
  description = "El nombre del servidor SQL creado."
  value       = azurerm_mssql_server.server.name
}

output "sql_database_name" {
  description = "El nombre de la base de datos SQL creada."
  value       = azurerm_mssql_database.db.name
}

output "admin_username" {
  description = "El nombre de usuario administrador para el servidor SQL."
  value       = azurerm_mssql_server.server.administrator_login
}

output "sql_admin_password" {
  description = "La contraseña del administrador de SQL (sensible)."
  value       = random_password.sql_password.result
  sensitive   = true
}