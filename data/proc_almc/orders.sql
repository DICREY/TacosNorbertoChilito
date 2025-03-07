CREATE PROCEDURE DesactiveOrder(
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
    
    -- Update Pedidos for desactive it
    UPDATE pedidos p
    SET p.estado = "ANULADO"
    WHERE p.fec_ped = p_var_search;

    COMMIT;

    SET autocommit = 1;
END //

CREATE PROCEDURE SearchOrderPendings()
BEGIN
    -- Update Pedidos for desactive it
    SELECT
        p.fec_ped,
        pe.nom_per,
        pe.ape_per,
        pe.cel_per,
        p.estado,
        pa.nom_pai,
        p.obs_ped
    FROM pedidos p,clientes c,personas pe,paises pa
    WHERE
        c.id_cli = p.id_cli AND
        c.id_cli = pe.id_per AND
        pe.pais_per = pa.id_pai AND
        p.estado = "PENDIENTE"
    ORDER BY(p.fec_ped)
    LIMIT 20;
END //

CREATE PROCEDURE SearchOrderDelivered()
BEGIN
    -- Update Pedidos for desactive it
    SELECT
        p.fec_ped,
        pe.nom_per,
        pe.ape_per,
        pe.cel_per,
        p.estado,
        pa.nom_pai,
        p.obs_ped
    FROM pedidos p,clientes c,personas pe,paises pa
    WHERE
        c.id_cli = p.id_cli AND
        c.id_cli = pe.id_per AND
        pe.pais_per = pa.id_pai AND
        p.estado = "ENTREGADO"
    ORDER BY(p.fec_ped)
    LIMIT 20;
END //
CREATE PROCEDURE SearchOrder(
    IN var_order VARCHAR(100)
)
BEGIN
    -- Update Pedidos for desactive it
    SELECT
        p.fec_ped,
        pe.nom_per,
        pe.ape_per,
        pe.cel_per,
        p.estado,
        pa.nom_pai,
        p.obs_ped
    FROM pedidos p,clientes c,personas pe,paises pa
    WHERE
        c.id_cli = p.id_cli AND
        c.id_cli = pe.id_per AND
        pe.pais_per = pa.id_pai AND
        p.fec_ped = var_order AND
        p.estado = "PENDIENTE" OR
        c.id_cli = p.id_cli AND
        c.id_cli = pe.id_per AND
        pe.pais_per = pa.id_pai AND
        p.fec_ped = var_order AND
        p.estado = "ENTREGADO"
    LIMIT 20;
END //
CREATE PROCEDURE SearchOrders()
BEGIN
    -- Update Pedidos for desactive it
    SELECT
        p.fec_ped,
        pe.nom_per,
        pe.ape_per,
        pe.cel_per,
        p.estado,
        pa.nom_pai,
        p.obs_ped
    FROM pedidos p,clientes c,personas pe,paises pa
    WHERE
        c.id_cli = p.id_cli AND
        c.id_cli = pe.id_per AND
        pe.pais_per = pa.id_pai AND
        p.estado = "PENDIENTE" OR
        c.id_cli = p.id_cli AND
        c.id_cli = pe.id_per AND
        pe.pais_per = pa.id_pai AND
        p.estado = "ENTREGADO"
    ORDER BY(p.fec_ped)
    LIMIT 20;
END //