DELIMITER //
CREATE PROCEDURE inventoryMaterials()
BEGIN
    SELECT 
        M.nom_mat,
        E.can_exi_mat AS existencia_actual,
        SUM(C.can_com) AS cantidad_comprada,
        (E.can_exi_mat + SUM(C.can_com)) AS nueva_existencia
    FROM MATERIALES M, EXISTENCIAS_MATERIALES E, COMPRAS C
    WHERE 
        M.id_mat = E.id_mat AND
        M.id_mat = C.id_mat
    GROUP BY (M.id_mat)
    LIMIT 40;
END //
CREATE PROCEDURE inventoryMachinery()
BEGIN
    SELECT 
        nom_maq,
        can_exi_maq
    FROM maquinaria 
    WHERE estado = "FUNCIONAL"
    GROUP BY(id_maq)
    LIMIT 40;
END //