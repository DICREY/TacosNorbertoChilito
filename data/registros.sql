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
INSERT INTO PRODUCTO_PEDIDOS (
    parte_pro_ped, refe_pro_ped, incrust_pro_ped, rosca_pro_ped, punt_pro_ped, 
    lamin_pro_ped, incrust_punt_pro_ped, casq_pro_ped, peso_pro_ped, 
    proceso_pro_ped, acces_pro_ped, colo_acc_pro_ped, des_pro_ped
)
VALUES 
('Parte A', 'Ref001', 'Incrust1', 'Rosca1', 'Punt1', 'Lamin1', 'IncrustPunt1', 'Casq1', 1.5, 'Proceso1', 'Acces1', 'Rojo', 'Descripción1'),
('Parte B', 'Ref002', 'Incrust2', 'Rosca2', 'Punt2', 'Lamin2', 'IncrustPunt2', 'Casq2', 2.0, 'Proceso2', 'Acces2', 'Azul', 'Descripción2'),
('Parte C', 'Ref003', 'Incrust3', 'Rosca3', 'Punt3', 'Lamin3', 'IncrustPunt3', 'Casq3', 1.8, 'Proceso3', 'Acces3', 'Verde', 'Descripción3'),
('Parte D', 'Ref004', 'Incrust4', 'Rosca4', 'Punt4', 'Lamin4', 'IncrustPunt4', 'Casq4', 2.5, 'Proceso4', 'Acces4', 'Amarillo', 'Descripción4'),
('Parte E', 'Ref005', 'Incrust5', 'Rosca5', 'Punt5', 'Lamin5', 'IncrustPunt5', 'Casq5', 1.2, 'Proceso5', 'Acces5', 'Negro', 'Descripción5');
INSERT INTO PEDIDOS (fec_ped, id_cli) 
VALUES ('2023-10-25', 1);
INSERT INTO DETALLE_PEDIDOS (id_ped, id_pro_ped, cantidad) 
VALUES 
(1, 1, 5)  -- 5 unidades del producto con id_pro_ped = 1

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