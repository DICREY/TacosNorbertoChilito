# Imports
from database import DataBase
from datetime import date

# Librarys

class Pedido():
    # Method Constructor
    @classmethod
    def __init__(
        cls,
        fec: float = None,
        fec_ent: float = None,
        data = None
        ):
        cls.__fec = fec
        cls.__fec_ent = fec_ent
        cls.__data = data

    # Methods GET of each attribute
    @classmethod
    def get__fec(cls):
        return cls.__fec
    
    @classmethod
    def get__fec_ent(cls):
        return cls.__fec_ent
    
    @classmethod
    def registrar_pedido(cls):
        conexion = DataBase.conectar()
        pedido = cls.buscar_pedido_name()
        if not pedido:
            try:
                cursor_pedido = conexion.cursor()
                cursor_pedido.callproc('', [
                    cls.get__fec,
                    cls.get__fec_ent
                ])
            except Exception as e:
                return f'Error al buscar pedido: {e}'
            finally:
                if conexion:
                    cursor_pedido.close()
                    DataBase.desconectar()
        else:
            return 'Ya existe'
        
    @classmethod
    def buscar_pedido_fec(cls, name=None):
        conexion = DataBase.conectar()
        if conexion:
            try:
                cursor_pedido = conexion.cursor()
                cursor_pedido.callproc('SearchpedidoName', [name])
                for busqueda in cursor_pedido.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        cls.__data = resultado
                        return cls.__data
                    else:
                        return 'Pedido no encontrado'
            except Exception as e:
                return e
            finally:
                if conexion:
                    cursor_pedido.close()
                    DataBase.desconectar()

    @classmethod
    def buscar_pedidos_pendientes(cls):
        conexion = DataBase.conectar()
        if conexion:
            try:
                cursor_pedido = conexion.cursor()
                cursor_pedido.callproc('SearchOrderPendings')
                for busqueda in cursor_pedido.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        cls.__data = resultado
                        return cls.__data
                    else:
                        return 'Pedidos no encontrados'
            except Exception as e:
                return e
            finally:
                if conexion:
                    cursor_pedido.close()
                    DataBase.desconectar()

    @classmethod
    def buscar_pedidos_entregados(cls):
        conexion = DataBase.conectar()
        if conexion:
            try:
                cursor_pedido = conexion.cursor()
                cursor_pedido.callproc('SearchOrderDelivered')
                for busqueda in cursor_pedido.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        cls.__data = resultado
                        return cls.__data
                    else:
                        return 'Pedidos no encontrados'
            except Exception as e:
                return e
            finally:
                if conexion:
                    cursor_pedido.close()
                    DataBase.desconectar()
        
    @classmethod
    def eliminar_pedido(cls, name = None):
        conexion = DataBase.conectar()
        pedido = cls.buscar_pedido_fec(name)
        if pedido:
            try:
                cursor_pedido = conexion.cursor()
                cursor_pedido.callproc('DesactiveOrder', [name])
                conexion.commit()
                cursor_pedido.close()
                return 'pedido eliminado'
            except Exception as error:
                return f'Error al eliminar el pedido: {error}. Intente de nuevo'
            finally:
                DataBase.desconectar()



pe = Pedido()
# delete = pe.eliminar_pedido("2023-10-25")
# print(delete)
# allPen = pe.buscar_pedidos_pendientes()
# print(allPen)
allDel = pe.buscar_pedidos_entregados()
print(allDel)