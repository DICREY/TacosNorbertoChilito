# Imports
from database import DataBase
from people import People
import re

# Librarys

class Client(People):
    # Method Constructor
    @classmethod
    def __init__(
        cls,
        anotaciones = "vacio",
        departamento: str = "vacio",
        data = None
        ):

        cls.__anotaciones = anotaciones
        cls.__departamento = departamento
        cls.__data = data

    # Methods GET of each attribute
    @classmethod
    def get__anotaciones(cls):
        return cls.__anotaciones
    
    @classmethod
    def get__departamento(cls):
        return cls.__departamento
    
    @classmethod
    def get__data(cls):
        return cls.__data
    
    # Methods SET of each attribute
    @classmethod
    def set_departamento(cls,dep):
        if re.match(r'^[A-Za-z\s]{3,100}$', dep):
            cls.__departamento = dep
            return True
        else:
            return "Departamento o Estado invalido"
        
    @classmethod
    def validar_datos(cls,name,lastname,cel,doc,email,country,city,dep):
        try:
            if (cls.set_name(name) and
            cls.set_lastname(lastname) and
            cls.set_cel(cel) and
            cls.set_doc(doc) and
            cls.set_email(email) and
            cls.set_country(country) and
            cls.set_city(city) and 
            cls.set_departamento(dep)):
                return True
        except Exception as e:
            return e

    
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
        if conexion:
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


# cl = Client()
# val = cl.validar_datos('s',
#     'P',
#     '3001234567',
#     '123456789',
#     'cristian@example.com',
#     'Colombia',
#     'Bogotá',
#     'C.A. S.A.S')
# print(val)