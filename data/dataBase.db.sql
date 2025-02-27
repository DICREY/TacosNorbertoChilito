wDROP DATABASE IF EXISTS TACOS_NORVERTO_CHILITO;
CREATE DATABASE TACOS_NORVERTO_CHILITO;
USE TACOS_NORVERTO_CHILITO;

CREATE TABLE USUARIOS (
	id_usu INT AUTO_INCREMENT PRIMARY KEY,
	nom_usu CHAR(100) NOT NULL,
	ape_usu CHAR(100) NOT NULL,
	cel_usu CHAR(20) NOT NULL,
	doc_usu CHAR(20) NOT NULL,
	ema_usu CHAR(100),
	dir_usu CHAR(100)
)
CREATE TABLE PRODUCTOS (
	nom_pro CHAR(100) NOT NULL

)ENGINE=INNODB;

CREATE TABLE CLIENTES (
	id_cli INT AUTO_INCREMENT PRIMARY KEY,
	nom_cli CHAR(100) NOT NULL,
	ape_cli CHAR(100) NOT NULL
)ENGINE=INNODB;

CREATE TABLE PEDIDOS (
	id_ven INT AUTO_INCREMENT PRIMARY KEY,
	fec_ven DATE NOT NULL,
	cat_ven CHAR(100) NOT NULL,
	id_pro_ped INT NOT NULL, INDEX(id_pro_ped), FOREIGN KEY(id_pro_ped) REFERENCES PRODUCTO_PEDIDOS(id_pro_ped) ON DELETE CASCADE ON UPDATE CASCADE,
	id_cli INT NOT NULL, INDEX(id_cli), FOREIGN KEY(id_cli) REFERENCES CLIENTES(id_cli) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE MATERIALES (
	id_mat INT AUTO_INCREMENT PRIMARY KEY,
	nom_mat CHAR(100) NOT NULL,
	can_mat CHAR(20) NOT NULL,
	pre_mat DECIMAL(20,2) NOT NULL
);

CREATE TABLE DISTRIBUIDORES (
	id_usu INT NOT NULL,FOREIGN KEY(id_usu) REFERENCES USUARIOS(id_usu) ON UPDATE CASCADE ON DELETE CASCADE,
);

CREATE TABLE COMPRAS (
	id_com INT AUTO_INCREMENT PRIMARY KEY,
	fec_com DATE NOT NULL,
    id_dis INT NOT NULL, INDEX(id_dis), FOREIGN KEY(id_dis) REFERENCES DISTRIBUIDORES(id_dis) ON DELETE CASCADE ON UPDATE CASCADE,
    id_mat INT NOT NULL, INDEX(id_mat), FOREIGN KEY(id_mat) REFERENCES MATERIALES(id_mat) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE EMPLEADOS(
	id_usu INT PRIMARY KEY NOT NULL
	sal_emp DECIMAL(20,2) NOT NULL,
	FOREIGN KEY(id_usu) REFERENCES USUARIOS(id_usu)
)

CREATE TABLE MAQUINARIA(
	id_maq INT AUTO_INCREMENT PRIMARY KEY,
	nom_maq CHAR(100) NOT NULL,
	estado ENUM("INSERVIBLE","FUNCIONAL") NOT NULL
)

CREATE TABLE PRODUCTO_PEDIDOS(
	id_pro_ped INT AUTO_INCREMENT PRIMARY KEY,
	parte_pro_ped CHAR(50) NOT NULL,
	refe_pro_ped CHAR(50) NOT NULL,
	incrust_pro_ped CHAR(50) NOT NULL,
	rosca_pro_ped CHAR(50) NOT NULL,
	punt_pro_ped CHAR(50) NOT NULL,
	lamin_pro_ped CHAR(50) NOT NULL,
	incrust_punt_pro_ped CHAR(50) NOT NULL,
	casq_pro_ped CHAR(50) NOT NULL,
	peso_pro_ped CHAR(50) NOT NULL,
	proceso_pro_ped CHAR(50) NOT NULL,
	acces_pro_ped CHAR(50) NOT NULL,
	colo_acc_pro_ped CHAR(50) NOT NULL
)

CREATE TABLE REMISIONES(
    id INT PRIMARY KEY AUTO_INCREMENT,
	tal_rem VARCHAR(10) NOT NULL,
	not_rem VARCHAR(20) UNIQUE,
	feca_rem date NOT NULL,
	fece_rem date,
	cliente INT NOT NULL, INDEX(cliente), FOREIGN KEY(cliente) REFERENCES CLIENTES(id_cli) ON DELETE CASCADE ON UPDATE CASCADE,
	pedidos INT NOT NULL, INDEX(pedidos), FOREIGN KEY(pedidos) REFERENCES PEDIDOS(id_ven) ON DELETE CASCADE ON UPDATE CASCADE,
	tipag_rem char(2),
	iva_rem INT NOT NULL,
	subt_rem DECIMAL(20,2) NOT NULL,
	des_rem DECIMAL(20,2) NOT NULL,
	dat_rem bool def(0),
	tot_rem DECIMAL(20,2) NOT NULL,
);

