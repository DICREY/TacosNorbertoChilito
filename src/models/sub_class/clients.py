# Imports
from models.database import DataBase
from models.people import People

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
    
    def get__data(cls):
        return cls.__data
        
    @classmethod
    def buscar_client_name(cls, name=None):
        conexion = DataBase.conectar()
        if conexion:
            try:
                mostrar_usuario = False
                cursor_client = conexion.cursor()
                cursor_client.callproc('SearchClientName', [name])
                for busqueda in cursor_client.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        mostrar_usuario = True
                        cls.__data = resultado
                        return mostrar_usuario
                    else:
                        return mostrar_usuario
            except Exception as e:
                print(f'Error al buscar client: {e}')
            finally:
                if conexion:
                    cursor_client.close()
                    DataBase.desconectar()
    @classmethod
    def eliminar_client(cls, name = None):
        conexion = DataBase.conectar()
        mostrar_usuario = cls.buscar_client_name(name)
        if mostrar_usuario:
            try:
                cursor_client = conexion.cursor()
                cursor_client.callproc('EliminarClient', [name])
                conexion.commit()
                cursor_client.close()
                print('client eliminado')
            except Exception as error:
                print(f'Error al eliminar el client: {error}. Intente de nuevo')
            finally:
                DataBase.desconectar()   

cl = Client()
cl.buscar_client_name("")
