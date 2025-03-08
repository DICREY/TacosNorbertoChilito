-- Active: 1725413700917@@127.0.0.1@3306@tacos_norberto_chilito
DELIMITER //
CREATE PROCEDURE SearchOneClient(
    -- Procedure Vars
    IN p_name VARCHAR(100)
)
BEGIN
    -- Consult one client
    SELECT 
        p.nom_per,
        p.ape_per,
        p.cel_per,
        p.doc_per,
        p.ema_per,
        p.dir_per,
        pa.nom_pai,
        ci.nom_ciu,
        c.depart_cli,
        c.ano_cli
    FROM PERSONAS p, CLIENTES c,PAISES pa, CIUDADES ci
    WHERE
        -- Enlazar varias tablas y buscar por nombre, documento o anotacion
        p.pais_per = pa.id_pai AND
        p.ciud_per = ci.id_ciu AND
        p.id_per = c.id_cli AND
        p.estado = 1 AND
        p.nom_per LIKE p_name OR
        p.pais_per = pa.id_pai AND
        p.ciud_per = ci.id_ciu AND
        p.id_per = c.id_cli AND
        p.estado = 1 AND
        p.doc_per = p_name OR 
        p.pais_per = pa.id_pai AND
        p.ciud_per = ci.id_ciu AND
        p.id_per = c.id_cli AND
        p.estado = 1 AND
        c.ano_cli LIKE CONCAT("%",p_name,"%");
END //

CREATE PROCEDURE SearchClients()
BEGIN
    -- Consult Clients
    SELECT 
        p.nom_per,
        p.ape_per,
        p.cel_per,
        p.doc_per,
        p.ema_per,
        p.dir_per,
        pa.nom_pai,
        ci.nom_ciu,
        c.ano_cli,
        c.depart_cli
    FROM PERSONAS p,CLIENTES c,PAISES pa, CIUDADES ci
    WHERE 
        -- Enlace para buscar solo los clientes
        p.id_per = c.id_cli AND
        p.ciud_per = ci.id_ciu AND
        p.estado = 1 AND
        p.pais_per = pa.id_pai
    ORDER BY(p.nom_per)
    LIMIT 40;
END //

CREATE PROCEDURE RegistClient(
    -- Procedure Vars
    IN name VARCHAR(100),
    IN lastname VARCHAR(100),
    IN cel VARCHAR(20),
    IN doc VARCHAR(20),
    IN email VARCHAR(100),
    IN address VARCHAR(100),
    IN country VARCHAR(100),
    IN city VARCHAR(100),
    IN ano VARCHAR(100),
    IN departamento VARCHAR(100)
)
BEGIN
    -- Vars
    DECLARE p_id_per INT;
    DECLARE p_id_country INT;
    DECLARE p_id_city INT;

    -- Manejador de excepciones
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    -- Insert PAIS if not exist
    INSERT INTO PAISES(nom_pai)
    SELECT country
    FROM DUAL -- Dual es una tabla vacia para tener datos en la ram
    WHERE NOT EXISTS (
        SELECT 1 FROM PAISES WHERE nom_pai = country
    );

    -- GET ID PAIS
    SELECT id_pai INTO p_id_country FROM PAISES WHERE nom_pai = country;

    -- Insert ciudad if not exist
    INSERT INTO CIUDADES(nom_ciu)
    SELECT city
    FROM DUAL
    WHERE NOT EXISTS(
        SELECT 1 FROM CIUDADES WHERE nom_ciu = city
    );

    -- GET ID CIUDADES
    SELECT id_ciu INTO p_id_city FROM CIUDADES WHERE nom_ciu = city;

    -- Insert PERSONAS
    INSERT INTO PERSONAS 
    (nom_per, ape_per, cel_per, doc_per, ema_per, dir_per, pais_per, ciud_per, estado)
    VALUES (name, lastname, cel, doc, email, address, p_id_country, p_id_city, 1);

    -- Get ID
    SET p_id_per = LAST_INSERT_ID();

    -- Insert CLIENTES
    INSERT INTO CLIENTES (id_cli, ano_cli, depart_cli)
    VALUES (p_id_per, ano, departamento);

    COMMIT;

    SET autocommit = 1;
END //

CREATE PROCEDURE DesactivarClient(
    -- Procedure Vars
    IN name VARCHAR(100)
)
BEGIN
    -- Manejador de excepciones
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    -- Update PERSONAS for desactive it
    UPDATE PERSONAS p,CLIENTES c
    SET p.estado = 0
    WHERE
        p.id_per = c.id_cli AND
        p.ema_per LIKE name OR
        p.id_per = c.id_cli AND
        p.doc_per LIKE name;

    COMMIT;

    SET autocommit = 1;
END //

CALL `SearchClients`();