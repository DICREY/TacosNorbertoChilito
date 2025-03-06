DELIMITER //
CREATE PROCEDURE inventoryMaterials()
BEGIN
    SELECT 
        M.nom_mat,
        E.can_exi_mat AS existencia_actual,
        SUM(C.can_com) AS cantidad_comprada,
        (E.can_exi_mat + SUM(C.can_com)) AS nueva_existencia
    FROM 
        MATERIALES M
    JOIN 
        EXISTENCIAS_MATERIALES E ON M.id_mat = E.id_mat
    JOIN 
        COMPRAS C ON M.id_mat = C.id_mat
    GROUP BY 
        M.id_mat;
END //