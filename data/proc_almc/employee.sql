DELIMITER //
CREATE PROCEDURE SearchOneEmployee(
    -- Procedure Vars
    IN p_var_search VARCHAR(100)
)
BEGIN
    SELECT
        p.nom_per,
        p.ape_per,
        p.cel_per,
        p.doc_per,
        p.ema_per,
        p.dir_per,
        pa.nom_pai,
        c.nom_ciu,
        e.arl_emp,
        e.eps_emp,
        e.sal_emp
    FROM PERSONAS p, EMPLEADOS e, CIUDADES c, PAISES pa
    WHERE
        -- Enlazar varias tablas y buscar por nombre o documento
        p.id_per = e.id_emp AND 
        p.ciud_per = c.id_ciu AND 
        p.pais_per = pa.id_pai AND 
        p.estado = 1 AND
        p.nom_per LIKE p_var_search OR
        p.id_per = e.id_emp AND 
        p.ciud_per = c.id_ciu AND 
        p.pais_per = pa.id_pai AND 
        p.estado = 1 AND
        p.doc_per = p_var_search;
END //

CREATE PROCEDURE SearchEmployees()
BEGIN 
    SELECT
        p.nom_per,
        p.ape_per,
        p.cel_per,
        p.doc_per,
        p.ema_per,
        p.dir_per,
        pa.nom_pai,
        c.nom_ciu,
        e.arl_emp,
        e.eps_emp,
        e.sal_emp
    FROM PERSONAS p, EMPLEADOS e, CIUDADES c, PAISES pa
    WHERE 
        -- Enlazar varias tablas
        p.id_per = e.id_emp AND
        p.ciud_per = c.id_ciu AND
        p.estado = 1 AND
        p.pais_per = pa.id_pai
    ORDER BY(p.nom_per)
    LIMIT 40;
END //
CREATE PROCEDURE DesactiveEmployee(
    -- Procedure Vars
    IN p_var_search VARCHAR(100)
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
    UPDATE PERSONAS p,EMPLEADOS e
    SET p.estado = 0
    WHERE
        p.id_per = e.id_emp AND
        p.ema_per LIKE p_var_search OR
        p.id_per = e.id_emp AND
        p.doc_per LIKE p_var_search;

    COMMIT;

    SET autocommit = 1;
END //

CREATE PROCEDURE RegistEmployee(
    -- Procedure Vars
    IN name VARCHAR(100),
    IN lastname VARCHAR(100),
    IN cel VARCHAR(20),
    IN doc VARCHAR(20),
    IN email VARCHAR(100),
    IN address VARCHAR(100),
    IN country VARCHAR(100),
    IN city VARCHAR(100),
    IN sal DECIMAL(10,2),
    IN arl DECIMAL(10,2),
    IN eps VARCHAR(100)
)
BEGIN
    -- Vars
    DECLARE id_per INT;
    DECLARE id_country INT;
    DECLARE id_city INT;

    -- Manejador de excepciones
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    SET autocommit = 0;

    START TRANSACTION;

    -- Insert if not EXISTS
    INSERT INTO PAISES(nom_pai)
    SELECT country
    FROM DUAL -- Dual es una tabla vacia para tener datos en la ram
    WHERE NOT EXISTS (
        SELECT 1 FROM PAISES WHERE nom_pai = country
    );

    -- seleccionar el id del pais que estamos bucando y darselo como valor a la variable
    SELECT id_pai INTO id_country FROM PAISES WHERE nom_pai = country;

    -- insertar ciudad si no existe
    INSERT INTO CIUDADES(nom_ciu)
    SELECT city
    FROM DUAL
    WHERE NOT EXISTS(
        SELECT 1 FROM CIUDADES WHERE nom_ciu = city
    );

    SELECT id_ciu INTO id_city FROM CIUDADES WHERE nom_ciu = city;

    INSERT INTO PERSONAS(nom_per, ape_per, cel_per, doc_per, ema_per, dir_per, pais_per, ciud_per, estado)
    VALUES(name, lastname, cel, doc, email, address, id_country, id_city, 1);

    -- Seleccionar el id de la inserccion mas reciente y darselo como valor a la variable
    SET id_per = LAST_INSERT_ID();

    INSERT INTO EMPLEADOS VALUES(id_per,sal,arl,eps);

    COMMIT;

    SET autocommit = 1;
END //