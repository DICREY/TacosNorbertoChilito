INSERT INTO USUARIOS (nom_usu, psw_usu, rol_usu) VALUES
('admin1', 'password1', 'ADMIN'),
('user1', 'password2', 'USER'),
('user2', 'password3', 'USER'),
('user3', 'password4', 'USER'),
('user4', 'password5', 'USER');
INSERT INTO PAISES (nom_pai) VALUES
('Colombia'),
('México'),
('Argentina'),
('España'),
('Estados Unidos');
INSERT INTO CIUDADES (nom_ciu) VALUES
('Bogotá'),
('Ciudad de México'),
('Buenos Aires'),
('Madrid'),
('Nueva York');
INSERT INTO PERSONAS (nom_per, ape_per, cel_per, doc_per, ema_per, dir_per, pais_per, ciud_per, estado) VALUES
('Juan', 'Pérez', '3001234567', '123456789', 'juan@example.com', 'Calle 123', 1, 1, 1),
('Ana', 'Gómez', '3102345678', '987654321', 'ana@example.com', 'Avenida 456', 2, 2, 1),
('Carlos', 'López', '3203456789', '456789123', 'carlos@example.com', 'Carrera 789', 3, 3, 1),
('Luisa', 'Martínez', '3304567890', '321654987', 'luisa@example.com', 'Calle 321', 4, 4, 1),
('Pedro', 'Rodríguez', '3405678901', '654987321', 'pedro@example.com', 'Avenida 654', 5, 5, 1),
('María', 'García', '3001111111', '111111111', 'maria@example.com', 'Calle 111', 1, 1, 1),
('Luis', 'Fernández', '3102222222', '222222222', 'luis@example.com', 'Avenida 222', 2, 2, 1),
('Carmen', 'López', '3203333333', '333333333', 'carmen@example.com', 'Carrera 333', 3, 3, 1),
('Jorge', 'Martínez', '3304444444', '444444444', 'jorge@example.com', 'Calle 444', 4, 4, 1),
('Sofía', 'Rodríguez', '3405555555', '555555555', 'sofia@example.com', 'Avenida 555', 5, 5, 1),
('Diego', 'Hernández', '3506666666', '666666666', 'diego@example.com', 'Carrera 666', 1, 1, 1),
('Laura', 'Díaz', '3607777777', '777777777', 'laura@example.com', 'Calle 777', 2, 2, 1),
('Miguel', 'Sánchez', '3708888888', '888888888', 'miguel@example.com', 'Avenida 888', 3, 3, 1),
('Elena', 'Romero', '3809999999', '999999999', 'elena@example.com', 'Carrera 999', 4, 4, 1),
('Pablo', 'Gómez', '3900000000', '000000000', 'pablo@example.com', 'Calle 000', 5, 5, 1);
INSERT INTO EMPLEADOS (id_emp, sal_emp, arl_emp, eps_emp) VALUES
(3, 2500000.00, 150000.00, 'EPS Sura'),
(15, 3000000.00, 180000.00, 'Sanitas'),
(14, 2800000.00, 160000.00, 'Nueva EPS'),
(13, 3200000.00, 200000.00, 'Salud Total'),
(12, 2700000.00, 170000.00, 'Coomeva');
INSERT INTO CLIENTES (id_cli, ano_cli, depart_cli) VALUES
(1, '2020', 'Bogotá'),
(2, '2021', 'Ciudad de México'),
(5, '2022', 'Nueva York'),
(6, '2023', 'Buenos Aires'),
(7, '2024', 'Madrid');
INSERT INTO DISTRIBUIDORES (id_dis, emp_per_dis) VALUES
(4, 'Distribuidora ABC'),
(8, 'Distribuidora XYZ'),
(9, 'Distribuidora 123'),
(10, 'Distribuidora 456'),
(11, 'Distribuidora 789');

INSERT INTO PEDIDOS (fec_ped, fec_ent_ped, estado, obs_ped, id_cli) VALUES
('2023-10-01', '2023-10-10', 'PENDIENTE', 'Observación 1', 1),
('2023-10-02', '2023-10-11', 'ENTREGADO', 'Observación 2', 2),
('2023-10-03', '2023-10-12', 'ANULADO', 'Observación 3', 2),
('2023-10-04', '2023-10-13', 'PENDIENTE', 'Observación 4', 7),
('2023-10-05', '2023-10-14', 'ENTREGADO', 'Observación 5', 5),
('2023-10-06', '2023-10-15', 'ANULADO', 'Observación 6', 6),
('2023-10-07', '2023-10-16', 'PENDIENTE', 'Observación 7', 1),
('2023-10-08', '2023-10-17', 'ENTREGADO', 'Observación 8', 7),
('2023-10-09', '2023-10-18', 'ANULADO', 'Observación 9', 6),
('2023-10-10', '2023-10-19', 'PENDIENTE', 'Observación 10', 5),
('2023-10-11', '2023-10-20', 'ENTREGADO', 'Observación 11', 7),
('2023-10-12', '2023-10-21', 'ANULADO', 'Observación 12', 6),
('2023-10-13', '2023-10-22', 'PENDIENTE', 'Observación 13', 5),
('2023-10-14', '2023-10-23', 'ENTREGADO', 'Observación 14', 6),
('2023-10-15', '2023-10-24', 'ANULADO', 'Observación 15', 7),
('2023-10-16', '2023-10-25', 'PENDIENTE', 'Observación 16', 1),
('2023-10-17', '2023-10-26', 'ENTREGADO', 'Observación 17', 6),
('2023-10-18', '2023-10-27', 'ANULADO', 'Observación 18', 5),
('2023-10-19', '2023-10-28', 'PENDIENTE', 'Observación 19', 6),
('2023-10-20', '2023-10-29', 'ENTREGADO', 'Observación 20', 7);

INSERT INTO PRODUCTO_PEDIDOS (parte_pro_ped, refe_pro_ped, incrust_pro_ped, rosca_pro_ped, punt_pro_ped, lamin_pro_ped, incrust_punt_pro_ped, casq_pro_ped, peso_pro_ped, proceso_pro_ped, acces_pro_ped, colo_acc_pro_ped, des_pro_ped) VALUES
('Parte1', 'Ref1', 'Incrust1', 'Rosca1', 'Punt1', 'Lamin1', 'IncrustPunt1', 'Casq1', 1.5, 'Proceso1', 'Acces1', 'Color1', 'Desc1'),
('Parte2', 'Ref2', 'Incrust2', 'Rosca2', 'Punt2', 'Lamin2', 'IncrustPunt2', 'Casq2', 2.0, 'Proceso2', 'Acces2', 'Color2', 'Desc2'),
('Parte3', 'Ref3', 'Incrust3', 'Rosca3', 'Punt3', 'Lamin3', 'IncrustPunt3', 'Casq3', 2.5, 'Proceso3', 'Acces3', 'Color3', 'Desc3'),
('Parte4', 'Ref4', 'Incrust4', 'Rosca4', 'Punt4', 'Lamin4', 'IncrustPunt4', 'Casq4', 3.0, 'Proceso4', 'Acces4', 'Color4', 'Desc4'),
('Parte5', 'Ref5', 'Incrust5', 'Rosca5', 'Punt5', 'Lamin5', 'IncrustPunt5', 'Casq5', 3.5, 'Proceso5', 'Acces5', 'Color5', 'Desc5'),
('Parte6', 'Ref6', 'Incrust6', 'Rosca6', 'Punt6', 'Lamin6', 'IncrustPunt6', 'Casq6', 4.0, 'Proceso6', 'Acces6', 'Color6', 'Desc6'),
('Parte7', 'Ref7', 'Incrust7', 'Rosca7', 'Punt7', 'Lamin7', 'IncrustPunt7', 'Casq7', 4.5, 'Proceso7', 'Acces7', 'Color7', 'Desc7'),
('Parte8', 'Ref8', 'Incrust8', 'Rosca8', 'Punt8', 'Lamin8', 'IncrustPunt8', 'Casq8', 5.0, 'Proceso8', 'Acces8', 'Color8', 'Desc8'),
('Parte9', 'Ref9', 'Incrust9', 'Rosca9', 'Punt9', 'Lamin9', 'IncrustPunt9', 'Casq9', 5.5, 'Proceso9', 'Acces9', 'Color9', 'Desc9'),
('Parte10', 'Ref10', 'Incrust10', 'Rosca10', 'Punt10', 'Lamin10', 'IncrustPunt10', 'Casq10', 6.0, 'Proceso10', 'Acces10', 'Color10', 'Desc10'),
('Parte11', 'Ref11', 'Incrust11', 'Rosca11', 'Punt11', 'Lamin11', 'IncrustPunt11', 'Casq11', 6.5, 'Proceso11', 'Acces11', 'Color11', 'Desc11'),
('Parte12', 'Ref12', 'Incrust12', 'Rosca12', 'Punt12', 'Lamin12', 'IncrustPunt12', 'Casq12', 7.0, 'Proceso12', 'Acces12', 'Color12', 'Desc12'),
('Parte13', 'Ref13', 'Incrust13', 'Rosca13', 'Punt13', 'Lamin13', 'IncrustPunt13', 'Casq13', 7.5, 'Proceso13', 'Acces13', 'Color13', 'Desc13'),
('Parte14', 'Ref14', 'Incrust14', 'Rosca14', 'Punt14', 'Lamin14', 'IncrustPunt14', 'Casq14', 8.0, 'Proceso14', 'Acces14', 'Color14', 'Desc14'),
('Parte15', 'Ref15', 'Incrust15', 'Rosca15', 'Punt15', 'Lamin15', 'IncrustPunt15', 'Casq15', 8.5, 'Proceso15', 'Acces15', 'Color15', 'Desc15'),
('Parte16', 'Ref16', 'Incrust16', 'Rosca16', 'Punt16', 'Lamin16', 'IncrustPunt16', 'Casq16', 9.0, 'Proceso16', 'Acces16', 'Color16', 'Desc16'),
('Parte17', 'Ref17', 'Incrust17', 'Rosca17', 'Punt17', 'Lamin17', 'IncrustPunt17', 'Casq17', 9.5, 'Proceso17', 'Acces17', 'Color17', 'Desc17'),
('Parte18', 'Ref18', 'Incrust18', 'Rosca18', 'Punt18', 'Lamin18', 'IncrustPunt18', 'Casq18', 10.0, 'Proceso18', 'Acces18', 'Color18', 'Desc18'),
('Parte19', 'Ref19', 'Incrust19', 'Rosca19', 'Punt19', 'Lamin19', 'IncrustPunt19', 'Casq19', 10.5, 'Proceso19', 'Acces19', 'Color19', 'Desc19'),
('Parte20', 'Ref20', 'Incrust20', 'Rosca20', 'Punt20', 'Lamin20', 'IncrustPunt20', 'Casq20', 11.0, 'Proceso20', 'Acces20', 'Color20', 'Desc20');

INSERT INTO DETALLE_PEDIDOS (id_ped, id_pro_ped, cantidad) VALUES
(1, 1, 5),
(2, 2, 10),
(3, 3, 15),
(4, 4, 20),
(5, 5, 25),
(6, 6, 30),
(7, 7, 35),
(8, 8, 40),
(9, 9, 45),
(10, 10, 50),
(11, 11, 55),
(12, 12, 60),
(13, 13, 65),
(14, 14, 70),
(15, 15, 75),
(16, 16, 80),
(17, 17, 85),
(18, 18, 90),
(19, 19, 95),
(20, 20, 100);

INSERT INTO CATEGORIAS (nom_cat) VALUES
('Electrónica'),
('Ropa'),
('Hogar'),
('Juguetes'),
('Deportes');
INSERT INTO ARTICULOS (cod_art, nom_art, cat_art, mat_art, pre_art, des_art) VALUES
('ART001', 'Laptop', 1, 'Plástico, Metal', 1500000.00, 'Laptop de última generación'),
('ART002', 'Camiseta', 2, 'Algodón', 50000.00, 'Camiseta de algodón orgánico'),
('ART003', 'Sofá', 3, 'Madera, Tela', 2000000.00, 'Sofá de 3 plazas'),
('ART004', 'Pelota', 4, 'Caucho', 30000.00, 'Pelota de fútbol'),
('ART005', 'Raqueta', 5, 'Grafito', 250000.00, 'Raqueta de tenis profesional');
INSERT INTO MATERIALES (nom_mat, pre_mat) 
VALUES 
('Tornillos', 0.50),
('Tuercas', 0.30),
('Arandelas', 0.20),
('Clavos', 0.10),
('Pegamento', 5.00);
INSERT INTO EXISTENCIAS_MATERIALES (id_mat, can_exi_mat) 
VALUES 
(1, 1000),  -- 1000 tornillos
(2, 1500),  -- 1500 tuercas
(3, 2000),  -- 2000 arandelas
(4, 5000),  -- 5000 clavos
(5, 50);    -- 50 unidades de pegamento
INSERT INTO COMPRAS (fec_com, uni_com, can_com,pre_tot_com, id_dis, id_mat) 
VALUES 
('2023-10-25', 'unidades', 500, 2000.99, 4, 1),  -- Compra de 500 tornillos
('2023-10-26', 'unidades', 300, 2000.99, 8, 2),  -- Compra de 300 tuercas
('2023-10-27', 'unidades', 200, 2000.99, 9, 3),  -- Compra de 200 arandelas
('2023-10-28', 'unidades', 1000, 2000.99, 10, 4), -- Compra de 1000 clavos
('2023-10-29', 'litros', 10,591.99, 11, 5);     -- Compra de 10 litros de pegamento
INSERT INTO MAQUINARIA (nom_maq, estado) VALUES
('Máquina de Corte', 'FUNCIONAL'),
('Máquina de Soldar', 'INSERVIBLE'),
('Máquina de Empaque', 'FUNCIONAL'),
('Máquina de Impresión', 'FUNCIONAL'),
('Máquina de Ensamblaje', 'INSERVIBLE');
INSERT INTO REMISIONES (tal_rem, not_rem, feca_rem, fece_rem, cliente, pedidos, tipag_rem, iva_rem, subt_rem, des_rem, dat_rem, tot_rem) VALUES
('TAL001', 'NOT001', '2023-10-01', '2023-10-05', 1, 1, 'EF', 19, 1500000.00, 0.00, 0, 1785000.00);
INSERT INTO ASISTENCIA_EMPLEADOS (id_emp, fec_ase, fes_ase, ent_ase, onc_ini_ase, onc_fin_ase, alm_ini_ase, alm_fin_ase, sal_ase, per_ini_ase, per_fin_ase) VALUES
(3, '2023-10-01', 'DES', '08:00:00', '10:00:00', '10:15:00', '12:00:00', '13:00:00', '17:00:00', NULL, NULL),
(14, '2023-10-02', 'FES', '09:00:00', '11:00:00', '11:15:00', '13:00:00', '14:00:00', '18:00:00', NULL, NULL),
(15, '2023-10-03', 'DES', '08:30:00', '10:30:00', '10:45:00', '12:30:00', '13:30:00', '17:30:00', NULL, NULL),
(13, '2023-10-04', 'FES', '09:30:00', '11:30:00', '11:45:00', '13:30:00', '14:30:00', '18:30:00', NULL, NULL),
(12, '2023-10-05', 'DES', '08:15:00', '10:15:00', '10:30:00', '12:15:00', '13:15:00', '17:15:00', NULL, NULL);