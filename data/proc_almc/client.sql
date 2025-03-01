-- Active: 1725413700917@@127.0.0.1@3306@tacos_norberto_chilito
CREATE PROCEDURE SearchClientName(
    IN p_name VARCHAR(100)
)
BEGIN
    SELECT 
        p.nom_per,
        p.ape_per,
        p.cel_per,
        p.doc_per,
        p.ema_per,
        p.dir_per,
        p.pais_per,
        p.ciud_per,
        c.depart_cli,
        c.ano_cli
    FROM PERSONAS p, CLIENTES c
    WHERE
        p.id_per = c.id_cli AND
        p.estado = 1 AND
        nombre LIKE CONCAT("%",p_name,"%");
END //
    
