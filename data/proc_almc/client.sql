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
        pa.nom_pai,
        ci.nom_ciu,
        c.depart_cli,
        c.ano_cli
    FROM PERSONAS p, CLIENTES c,PAISES pa, CIUDADES ci
    WHERE
        p.pais_per = pa.id_pai AND
        p.ciud_per = ci.id_ciu AND
        p.id_per = c.id_cli AND
        p.estado = 1 AND
        p.nom_per LIKE CONCAT("%",p_name,"%");
END //
    
