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
INSERT INTO PRODUCTO_PEDIDOS (parte_pro_ped, refe_pro_ped, incrust_pro_ped, rosca_pro_ped, punt_pro_ped, lamin_pro_ped, incrust_punt_pro_ped, casq_pro_ped, peso_pro_ped, proceso_pro_ped, acces_pro_ped, colo_acc_pro_ped, des_pro_ped) VALUES
('Parte A', 'REF001', 'Incrustación 1', 'Rosca 1', 'Punta 1', 'Laminado 1', 'Incrustación Punta 1', 'Casco 1', 1.5, 'Proceso 1', 'Accesorio 1', 'Color 1', 'Descripción 1'),
('Parte B', 'REF002', 'Incrustación 2', 'Rosca 2', 'Punta 2', 'Laminado 2', 'Incrustación Punta 2', 'Casco 2', 2.0, 'Proceso 2', 'Accesorio 2', 'Color 2', 'Descripción 2'),
('Parte C', 'REF003', 'Incrustación 3', 'Rosca 3', 'Punta 3', 'Laminado 3', 'Incrustación Punta 3', 'Casco 3', 2.5, 'Proceso 3', 'Accesorio 3', 'Color 3', 'Descripción 3'),
('Parte D', 'REF004', 'Incrustación 4', 'Rosca 4', 'Punta 4', 'Laminado 4', 'Incrustación Punta 4', 'Casco 4', 3.0, 'Proceso 4', 'Accesorio 4', 'Color 4', 'Descripción 4'),
('Parte E', 'REF005', 'Incrustación 5', 'Rosca 5', 'Punta 5', 'Laminado 5', 'Incrustación Punta 5', 'Casco 5', 3.5, 'Proceso 5', 'Accesorio 5', 'Color 5', 'Descripción 5');
INSERT INTO PEDIDOS (fec_ped, estado, obs_ped, id_cli) VALUES
('2023-10-01', 'PENDIENTE', 'Pedido urgente', 1),
('2023-10-02', 'ENTREGADO', 'Pedido estándar', 2),
('2023-10-03', 'ANULADO', 'Pedido cancelado', 5),
('2023-10-04', 'PENDIENTE', 'Pedido prioritario', 6),
('2023-10-05', 'ENTREGADO', 'Pedido normal', 7);
INSERT INTO DETALLE_PEDIDOS (id_ped, id_pro_ped, cantidad) VALUES
(1, 1, 10),
(2, 2, 5),
(3, 3, 8),
(4, 4, 12),
(5, 5, 15);
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
INSERT INTO MATERIALES (nom_mat, can_mat, pre_mat) VALUES
('Plástico', '100 kg', 50000.00),
('Metal', '50 kg', 100000.00),
('Algodón', '200 m', 30000.00),
('Madera', '30 m³', 150000.00),
('Caucho', '80 kg', 40000.00);
INSERT INTO COMPRAS (fec_com, id_dis, id_mat) VALUES
('2023-10-01', 4, 1),
('2023-10-02', 8, 2),
('2023-10-03', 9, 3),
('2023-10-04', 10, 4),
('2023-10-05', 11, 5);
INSERT INTO MAQUINARIA (nom_maq, estado) VALUES
('Máquina de Corte', 'FUNCIONAL'),
('Máquina de Soldar', 'INSERVIBLE'),
('Máquina de Empaque', 'FUNCIONAL'),
('Máquina de Impresión', 'FUNCIONAL'),
('Máquina de Ensamblaje', 'INSERVIBLE');
INSERT INTO REMISIONES (tal_rem, not_rem, feca_rem, fece_rem, cliente, pedidos, tipag_rem, iva_rem, subt_rem, des_rem, dat_rem, tot_rem) VALUES
('TAL001', 'NOT001', '2023-10-01', '2023-10-05', 1, 1, 'EF', 19, 1500000.00, 0.00, 0, 1785000.00),
('TAL002', 'NOT002', '2023-10-02', '2023-10-06', 2, 2, 'TC', 19, 50000.00, 5000.00, 0, 53500.00),
('TAL003', 'NOT003', '2023-10-03', '2023-10-07', 5, 3, 'EF', 19, 2000000.00, 100000.00, 0, 2261000.00),
('TAL004', 'NOT004', '2023-10-04', '2023-10-08', 6, 4, 'TC', 19, 30000.00, 0.00, 0, 35700.00),
('TAL005', 'NOT005', '2023-10-05', '2023-10-09', 7, 5, 'EF', 19, 250000.00, 25000.00, 0, 267750.00);
INSERT INTO ASISTENCIA_EMPLEADOS (id_emp, fec_ase, fes_ase, ent_ase, onc_ini_ase, onc_fin_ase, alm_ini_ase, alm_fin_ase, sal_ase, per_ini_ase, per_fin_ase) VALUES
(3, '2023-10-01', 'DES', '08:00:00', '10:00:00', '10:15:00', '12:00:00', '13:00:00', '17:00:00', NULL, NULL),
(14, '2023-10-02', 'FES', '09:00:00', '11:00:00', '11:15:00', '13:00:00', '14:00:00', '18:00:00', NULL, NULL),
(15, '2023-10-03', 'DES', '08:30:00', '10:30:00', '10:45:00', '12:30:00', '13:30:00', '17:30:00', NULL, NULL),
(13, '2023-10-04', 'FES', '09:30:00', '11:30:00', '11:45:00', '13:30:00', '14:30:00', '18:30:00', NULL, NULL),
(12, '2023-10-05', 'DES', '08:15:00', '10:15:00', '10:30:00', '12:15:00', '13:15:00', '17:15:00', NULL, NULL);