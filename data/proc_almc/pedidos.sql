CREATE PROCEDURE DesactivePedido(
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
    

    COMMIT;

    SET autocommit = 1;
END //
