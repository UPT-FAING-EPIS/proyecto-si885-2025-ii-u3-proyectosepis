variable "resource_group_location" {
  type    = string
  default = "eastus2"
  description = "Ubicación para todos los recursos."
}

variable "base_name" {
  type        = string
  description = "Un nombre base único para todos los recursos."
  default     = "pyintnegocios"
}

variable "sql_admin_username" {
  type        = string
  description = "El nombre de usuario administrador para el servidor SQL."
  default     = "azureadmin"
}