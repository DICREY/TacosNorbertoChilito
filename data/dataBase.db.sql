-- Active: 1725413700917@@127.0.0.1@3306@tacos_norberto_chilito
DROP DATABASE IF EXISTS TACOS_NORBERTO_CHILITO;
CREATE DATABASE TACOS_NORBERTO_CHILITO;
USE TACOS_NORBERTO_CHILITO;

CREATE TABLE USUARIOS(
	id_usu INT AUTO_INCREMENT PRIMARY KEY,
	nom_usu VARCHAR(100) NOT NULL,
	psw_usu VARCHAR(100) NOT NULL,
	rol_usu ENUM("ADMIN","USER") NOT NULL
);

CREATE TABLE PERSONAS (
	id_per INT AUTO_INCREMENT PRIMARY KEY,
	nom_per VARCHAR(100) NOT NULL,
	ape_per VARCHAR(100) NOT NULL,
	cel_per VARCHAR(20) NOT NULL,
	doc_per VARCHAR(20) NOT NULL,
	ema_per VARCHAR(100) NOT NULL,
	dir_per VARCHAR(100),
	pais_per VARCHAR(100) NOT NULL,
	ciud_per VARCHAR(100) NOT NULL,
	estado BOOLEAN NOT NULL
);

CREATE TABLE EMPLEADOS(
	id_emp INT PRIMARY KEY, INDEX(id_emp),FOREIGN KEY(id_emp) REFERENCES PERSONAS(id_per) ON UPDATE CASCADE ON DELETE CASCADE,
	sal_emp DECIMAL(20,2) NOT NULL,
	arl_emp DECIMAL(20,2) NOT NULL,
	eps_emp VARCHAR(100) NOT NULL
);

CREATE TABLE CLIENTES (
	id_cli INT PRIMARY KEY,INDEX(id_cli),FOREIGN KEY(id_cli) REFERENCES PERSONAS(id_per) ON DELETE CASCADE ON UPDATE CASCADE,
	ano_cli VARCHAR(100) NOT NULL,
	depart_cli VARCHAR(100) NOT NULL DEFAULT("BOGOTA")
);

CREATE TABLE DISTRIBUIDORES (
	id_dis INT PRIMARY KEY,INDEX(id_dis),FOREIGN KEY(id_dis) REFERENCES PERSONAS(id_per) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE PRODUCTO_PEDIDOS(
	id_pro_ped INT AUTO_INCREMENT PRIMARY KEY,
	parte_pro_ped VARCHAR(50) NOT NULL,
	refe_pro_ped VARCHAR(50) NOT NULL,
	incrust_pro_ped VARCHAR(50) NOT NULL,
	rosca_pro_ped VARCHAR(50) NOT NULL,
	punt_pro_ped VARCHAR(50) NOT NULL,
	lamin_pro_ped VARCHAR(50) NOT NULL,
	incrust_punt_pro_ped VARCHAR(50) NOT NULL,
	casq_pro_ped VARCHAR(50) NOT NULL,
	peso_pro_ped DECIMAL(5,10) NOT NULL,
	proceso_pro_ped VARCHAR(50) NOT NULL,
	acces_pro_ped VARCHAR(50) NOT NULL,
	colo_acc_pro_ped VARCHAR(50) NOT NULL,
	des_pro_ped VARCHAR(50) NOT NULL
);

CREATE TABLE PEDIDOS (
	id_ped INT AUTO_INCREMENT PRIMARY KEY,
	fec_ped DATE NOT NULL,
	estado ENUM("PENDIENTE","ENTREGADO","ANULADO"),
	obs_ped TEXT,
	id_pro_ped INT NOT NULL,
	INDEX(id_pro_ped),
	FOREIGN KEY(id_pro_ped) REFERENCES PRODUCTO_PEDIDOS(id_pro_ped) ON DELETE CASCADE ON UPDATE CASCADE,
	id_cli INT NOT NULL, INDEX(id_cli),
	FOREIGN KEY(id_cli) REFERENCES CLIENTES(id_cli) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE MATERIALES (
	id_mat INT AUTO_INCREMENT PRIMARY KEY,
	nom_mat VARCHAR(100) NOT NULL,
	can_mat VARCHAR(20) NOT NULL,
	pre_mat DECIMAL(20,2) NOT NULL
);

CREATE TABLE COMPRAS (
	id_com INT AUTO_INCREMENT PRIMARY KEY,
	fec_com DATE NOT NULL,
    id_dis INT NOT NULL, INDEX(id_dis), FOREIGN KEY(id_dis) REFERENCES DISTRIBUIDORES(id_dis) ON DELETE CASCADE ON UPDATE CASCADE,
    id_mat INT NOT NULL, INDEX(id_mat), FOREIGN KEY(id_mat) REFERENCES MATERIALES(id_mat) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE MAQUINARIA(
	id_maq INT AUTO_INCREMENT PRIMARY KEY,
	nom_maq VARCHAR(100) NOT NULL,
	estado ENUM("INSERVIBLE","FUNCIONAL") NOT NULL
);

CREATE TABLE REMISIONES(
    id INT PRIMARY KEY AUTO_INCREMENT,
	tal_rem VARCHAR(10) NOT NULL,
	not_rem VARCHAR(20) UNIQUE,
	feca_rem DATE NOT NULL,
	fece_rem DATE,
	cliente INT NOT NULL, INDEX(cliente), FOREIGN KEY(cliente) REFERENCES CLIENTES(id_cli) ON DELETE CASCADE ON UPDATE CASCADE,
	pedidos INT NOT NULL, INDEX(pedidos), FOREIGN KEY(pedidos) REFERENCES PEDIDOS(id_ped) ON DELETE CASCADE ON UPDATE CASCADE,
	tipag_rem CHAR(2),
	iva_rem INT NOT NULL,
	subt_rem DECIMAL(20,2) NOT NULL,
	des_rem DECIMAL(20,2) NOT NULL,
	dat_rem BOOLEAN DEFAULT(0),
	tot_rem DECIMAL(20,2) NOT NULL
);

CREATE TABLE ASISTENCIA_EMPLEADOS(
	id_emp INT PRIMARY KEY, INDEX(id_emp),FOREIGN KEY(id_emp) REFERENCES EMPLEADOS(id_emp) ON DELETE CASCADE ON UPDATE CASCADE,
	fec_ase DATE NOT NULL,
	fes_ase ENUM ("DES,FES"),
	ent_ase TIME NOT NULL,
	onc_ini_ase TIME NOT NULL,
	onc_fin_ase TIME NOT NULL,
	alm_ini_ase TIME NOT NULL,
	alm_fin_ase TIME NOT NULL,
	sal_ase TIME NOT NULL,
	per_ini_ase TIME,
	per_fin_ase TIME
);