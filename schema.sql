-- Nuevo schema.sql para usar fecha de creación
CREATE TABLE analisis_repositorios (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre_repo NVARCHAR(255) UNIQUE NOT NULL, -- Mantenemos UNIQUE para tener solo el último estado
    url_repo NVARCHAR(MAX),
    lenguaje_principal NVARCHAR(100),
    tecnologias NVARCHAR(MAX),
    fecha_creacion_repo DATE NOT NULL -- CAMBIO: Columna para la fecha de creación (solo fecha)
);