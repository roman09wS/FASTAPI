DROP DATABASE gestion_user;
CREATE DATABASE gestion_user;
USE gestion_user;
CREATE TABLE usuarios(
    id_user INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    cargo VARCHAR(100),
    ciudad VARCHAR(100),
    edad VARCHAR(100),
    salario VARCHAR(100)
);

CREATE TABLE admin(
    id_admin INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    passw VARCHAR(100)
);

INSERT INTO admin (nombre,passw) VALUES ('winder','1234');

INSERT INTO usuarios (nombre, cargo, ciudad, edad, salario)
VALUES
    ('John Doe', 'Gerente de Ventas', 'Nueva York', '35', '80000'),
    ('Jane Smith', 'Ingeniera de Software', 'Los Ángeles', '28', '75000'),
    ('Carlos Sánchez', 'Analista de Datos', 'Ciudad de México', '30', '60000'),
    ('Emily Brown', 'Diseñadora Gráfica', 'Toronto', '26', '65000'),
    ('Luis Garcia', 'Contador', 'Bogotá', '32', '70000'),
    ('Sophie Martin', 'Economista', 'París', '29', '72000'),
    ('Makoto Yamada', 'Ingeniero Mecánico', 'Tokio', '31', '85000'),
    ('Isabella Rossi', 'Abogada', 'Roma', '27', '67000'),
    ('Mikhail Ivanov', 'Científico de Datos', 'Moscú', '33', '78000'),
    ('Maria Santos', 'Médica', 'Sao Paulo', '34', '90000'),
    ('Benjamin Lee', 'Arquitecto', 'Seúl', '29', '82000'),
    ('Alicia Fernández', 'Publicista', 'Buenos Aires', '28', '70000'),
    ('Fatemah Khan', 'Ingeniera Civil', 'Dubái', '30', '95000'),
    ('William Johnson', 'Investigador', 'Londres', '31', '76000'),
    ('Anastasia Petrova', 'Diseñadora de Moda', 'Moscú', '27', '72000'),
    ('Raj Patel', 'Chef', 'Mumbai', '32', '68000'),
    ('Emilia Andersson', 'Psicóloga', 'Estocolmo', '29', '71000'),
    ('Diego Fernández', 'Profesor', 'Buenos Aires', '35', '67000'),
    ('Chen Wei', 'Ingeniero Eléctrico', 'Shanghái', '30', '80000'),
    ('Olivia Murphy', 'Escritora', 'Dublín', '28', '62000'),
    ('Hiroshi Tanaka', 'Diseñador Industrial', 'Tokio', '31', '85000'),
    ('Amelia Jackson', 'Bióloga', 'Sydney', '26', '72000'),
    ('Alexandre Moreau', 'Traductor', 'París', '33', '73000'),
    ('Elena Vargas', 'Médica', 'Ciudad de México', '34', '92000'),
    ('Andrei Popov', 'Ingeniero de Software', 'Moscú', '29', '80000'),
    ('Fiona Connor', 'Economista', 'Dublín', '28', '69000'),
    ('Javier Torres', 'Arquitecto', 'Madrid', '31', '78000'),
    ('Jasmine Kim', 'Artista', 'Seúl', '27', '67000'),
    ('Matteo Bianchi', 'Chef', 'Roma', '32', '75000'),
    ('Lara Silva', 'Abogada', 'Río de Janeiro', '30', '85000'),
    ('Anna Kovalenko', 'Científica de Datos', 'Moscú', '29', '92000'),
    ('Mohammed Al-Mansoori', 'Ingeniero Civil', 'Dubái', '31', '89000'),
    ('Julia Costa', 'Diseñadora Gráfica', 'Sao Paulo', '28', '71000'),
    ('Robert Smith', 'Consultor', 'Nueva York', '33', '80000'),
    ('Elena Petrova', 'Médica', 'Moscú', '34', '93000'),
    ('Sebastian Müller', 'Ingeniero Mecánico', 'Berlín', '29', '82000'),
    ('Mia Johnson', 'Psicóloga', 'Los Ángeles', '30', '73000'),
    ('Alessandro Ferrari', 'Diseñador Industrial', 'Milán', '27', '76000'),
    ('Nadia Chen', 'Ingeniera Eléctrica', 'Shanghái', '32', '79000'),
    ('Lucas Souza', 'Artista', 'Río de Janeiro', '28', '67000'),
    ('Yuki Tanaka', 'Traductor', 'Tokio', '31', '71000');
