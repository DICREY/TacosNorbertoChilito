# Imports
from database import DataBase
from people import People

# Librarys

class Client(People):
    # Method Constructor
    @classmethod
    def __init__(
        cls,
        id_cliente: int = None,
        anotaciones: str = None,
        departamento: str = None,
        data = None
        ):

        cls.__id_cliente = id_cliente
        cls.__anotaciones = anotaciones
        cls.__departamento = departamento
        cls.__data = data

    # Methods GET of each attribute
    @classmethod
    def get__id_cliente(cls):
        return cls.__id_cliente
    
    @classmethod
    def get__anotaciones(cls):
        return cls.__anotaciones
    
    @classmethod
    def get__departamento(cls):
        return cls.__departamento
    
    @classmethod
    def get__data(cls):
        return cls.__data
    
    # def catch_data(cls):
        # cls.__name = ;
    
    @classmethod
    def registrar_client(cls):
        conexion = DataBase.conectar()
        cliente = cls.buscar_client_name()
        if not cliente:
            try:
                cursor_client = conexion.cursor()
                cursor_client.callproc('RegistClient', [
                    cls.get__name,
                    cls.get__lastname,
                    cls.get__cel,
                    cls.get__doc,
                    cls.get__email,
                    cls.get__address,
                    cls.get__country,
                    cls.get__city,
                    cls.get__anotaciones,
                    cls.get__departamento

                ])
            except Exception as e:
                return f'Error al buscar client: {e}'
            finally:
                if conexion:
                    cursor_client.close()
                    DataBase.desconectar()
        else:
            return 'Ya existe'
        
    @classmethod
    def buscar_client_name(cls, name=None):
        conexion = DataBase.conectar()
        cliente = cls.buscar_client_name(name)
        if not cliente:
            try:
                cursor_client = conexion.cursor()
                cursor_client.callproc('SearchClientName', [name])
                for busqueda in cursor_client.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        cls.__data = resultado
                        print(cls.__data)
                        return 'Cliente encontrado'
                    else:
                        return 'Cliente not encontrado'
            except Exception as e:
                return e
            finally:
                if conexion:
                    cursor_client.close()
                    DataBase.desconectar()
        
    @classmethod
    def eliminar_client(cls, name = None):
        conexion = DataBase.conectar()
        cliente = cls.buscar_client_name(name)
        if cliente:
            try:
                cursor_client = conexion.cursor()
                cursor_client.callproc('DesactivarClient', [name])
                conexion.commit()
                cursor_client.close()
                return 'client eliminado'
            except Exception as error:
                return f'Error al eliminar el client: {error}. Intente de nuevo'
            finally:
                DataBase.desconectar()

    @classmethod
    def buscar_clientes(cls):
        conexion = DataBase.conectar()
        if conexion:
            try:
                cursor_client = conexion.cursor()
                cursor_client.callproc('SearchClients')
                for i in cursor_client.stored_results():
                    res = i.fetchall()
                if res:
                    cls.__data = res
                    return cls.__data
                else:
                    return "No hay clientes registrados"
                
                return
            except Exception as error:
                return f'Error al buscar los distributores: {error}. Intente de nuevo'
            finally:
                if conexion:
                    cursor_client.close()
                    DataBase.desconectar()


cl = Client()
# search = cl.buscar_client_name("cristi")
# print(search)
# delete = cl.eliminar_client("123456789")
# print(delete)
# regis = cl.registrar_client(
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
all = cl.buscar_clientes()
print(all)