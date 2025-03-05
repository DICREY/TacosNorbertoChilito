# Imports
from database import DataBase
from people import People 

# Librarys

class Pedido():
    # Method Constructor
    @classmethod
    def __init__(
        cls,
        sal: float = None,
        arl: float = None,
        eps: str = None,
        data = None
        ):

        cls.__sal = sal
        cls.__arl = arl
        cls.__eps = eps
        cls.__data = data

    # Methods GET of each attribute
    @classmethod
    def get__sal(cls):
        return cls
    
    @classmethod
    def registrar_pedido(cls):
        conexion = DataBase.conectar()
        pedido = cls.buscar_pedido_name()
        if not pedido:
            try:
                cursor_pedido = conexion.cursor()
                cursor_pedido.callproc('', [
                    cls.get__name,
                    cls.get__lastname,
                    cls.get__cel,
                    cls.get__doc,
                    cls.get__email,
                    cls.get__address,
                    cls.get__country,
                    cls.get__city,
                    cls.get__sal,
                    cls.get__arl,
                    cls.get__eps
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
    def buscar_pedido_name(cls, name=None):
        conexion = DataBase.conectar()
        pedido = cls.buscar_pedido_name(name)
        if not pedido:
            try:
                cursor_pedido = conexion.cursor()
                cursor_pedido.callproc('SearchpedidoName', [name])
                for busqueda in cursor_pedido.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        cls.__data = resultado
                        print(cls.__data)
                        return 'pedido encontrado'
                    else:
                        return 'pedido not encontrado'
            except Exception as e:
                return e
            finally:
                if conexion:
                    cursor_pedido.close()
                    DataBase.desconectar()
        
    @classmethod
    def eliminar_pedido(cls, name = None):
        conexion = DataBase.conectar()
        pedido = cls.buscar_pedido_name(name)
        if pedido:
            try:
                cursor_pedido = conexion.cursor()
                cursor_pedido.callproc('Desactivarpedido', [name])
                conexion.commit()
                cursor_pedido.close()
                return 'pedido eliminado'
            except Exception as error:
                return f'Error al eliminar el pedido: {error}. Intente de nuevo'
            finally:
                DataBase.desconectar()

    @classmethod
    def buscar_pedidos(cls):
        conexion = DataBase.conectar()
        if conexion:
            try:
                cursor_pedido = conexion.cursor()
                cursor_pedido.callproc('Searchpedidos')
                for i in cursor_pedido.stored_results():
                    res = i.fetchall()
                if res:
                    cls.__data = res
                    return cls.__data
                else:
                    return "No hay pedido registrados"
                
                return
            except Exception as error:
                return f'Error al buscar los pedido: {error}. Intente de nuevo'
            finally:
                if conexion:
                    cursor_pedido.close()
                    DataBase.desconectar()


cl = Pedido()
# search = cl.buscar_pedido_name("cristi")
# print(search)
# delete = cl.eliminar_pedido("123456789")
# print(delete)
# regis = cl.registrar_pedido(
#     'CRISTIAN',
#     'Pérez',
#     '3001234567',
#     '123456789',
#     'cristian@example.com',
#     'Calle 123',
#     'Colombia',
#     'Bogotá',
#     'C.A. S.A.S'
# )
# print(regis)
all = cl.buscar_pedidos()
print(all)