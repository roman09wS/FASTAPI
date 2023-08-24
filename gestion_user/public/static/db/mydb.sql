CREATE DATABASE db_ejemplo;
USE db_ejemplo;
CREATE TABLE usuarios(
    id_usuario CHAR(10) PRIMARY KEY,
    nombres VARCHAR(100),
    apellidos VARCHAR(100),
    email VARCHAR(100),
    pass VARCHAR(100),
    rol ENUM('admin','editor','lector')
);