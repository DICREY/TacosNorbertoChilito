# Imports
from models.database import DataBase
from models.people import People 

# Librarys

class Distributor(People):
    # Method Constructor
    @classmethod
    def __init__(
        cls,
        corp: str = None,
        data = None
        ):
        cls.__corp = corp
        cls.__data = data

    # Methods GET of each attribute
    @classmethod
    def get__corp(cls):
        return cls.__corp
    
    def get__data(cls):
        return cls.__data
    
    # def catch_data(cls):
        # cls.__name = ;
    
    @classmethod
    def registrar_distributor(cls):
        conexion = DataBase.conectar()
        distributor = cls.buscar_distributor_name()
        if not distributor:
            try:
                cursor_distributor = conexion.cursor()
                cursor_distributor.callproc('RegistDistributor', [
                    cls.get__name,
                    cls.get__lastname,
                    cls.get__cel,
                    cls.get__doc,
                    cls.get__email,
                    cls.get__address,
                    cls.get__country,
                    cls.get__city,
                    cls.get__corp
                ])
            except Exception as e:
                return f'Error al buscar distributor: {e}'
            finally:
                if conexion:
                    cursor_distributor.close()
                    DataBase.desconectar()
        else:
            return 'Ya existe'
    @classmethod
    def buscar_distributor_name(cls, name=None):
        conexion = DataBase.conectar()
        distributor = cls.buscar_distributor_name(name)
        if not distributor:
            try:
                cursor_distributor = conexion.cursor()
                cursor_distributor.callproc('SearchDistributorName', [name])
                for busqueda in cursor_distributor.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        cls.__data = resultado
                        print(cls.__data)
                        return 'distributor encontrado'
                    else:
                        return 'distributor not encontrado'
            except Exception as e:
                return e
            finally:
                if conexion:
                    cursor_distributor.close()
                    DataBase.desconectar()
        
    @classmethod
    def eliminar_distributor(cls, name = None):
        conexion = DataBase.conectar()
        distributor = cls.buscar_distributor_name(name)
        if distributor:
            try:
                cursor_distributor = conexion.cursor()
                cursor_distributor.callproc('DesactivarDistributor', [name])
                conexion.commit()
                cursor_distributor.close()
                return 'distributor eliminado'
            except Exception as error:
                return f'Error al eliminar el distributor: {error}. Intente de nuevo'
            finally:
                DataBase.desconectar()


cl = Distributor()
search = cl.buscar_distributor_name("cristi")
print(search)
# delete = cl.eliminar_distributor("123456789")
# print(delete)
# regis = cl.registrar_distributor(
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