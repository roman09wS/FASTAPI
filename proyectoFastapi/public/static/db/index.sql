DROP DATABASE personas;
CREATE DATABASE personas;
USE personas;
CREATE TABLE usuarios(
    id_user INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    correo VARCHAR(90)
);