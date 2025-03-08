# Imports
from database import DataBase
from people import People

# Librarys
import re

# Seudo class
class Exist(Exception):
    pass

class Client(People):
    # Method Constructor
    @classmethod
    def __init__(
        cls,
        name: str = None,
        lastname: str = None,
        cel: str = None,
        doc: str = None,
        email: str  = None,
        address: str = None,
        country: str = None,
        city: str = None,
        anotaciones: str = None,
        departamento: str = None,
        data = None
        ):
        super().__init__(name,lastname,cel,doc,email,address,country,city)

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
        if re.match(r"^[A-Za-z\s]{3,100}$", dep):
            cls.__departamento = dep
            return True
        else:
            raise ValueError("Departamento o Estado invalido")
        
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
            else:
                return False
        except ValueError as ve:
            return f"{ve}"
        except Exception as e:
            return f"{e}"
    
    @classmethod
    def registrar_client(cls):
        try:
            conexion = DataBase.conectar()
            validar = cls.validar_datos(
                cls.get__name(),
                cls.get__lastname(),
                cls.get__cel(),
                cls.get__doc(),
                cls.get__email(),
                cls.get__country(),
                cls.get__city(),
                cls.get__departamento()
            )
            if validar:
                doc = cls.get__doc
                cliente = cls.buscar_client_name(doc)
                if cliente:
                    raise Exist("El cliente ya está registrado")
                else:
                    cursor_client = conexion.cursor()
                    cursor_client.callproc("RegistClient", [
                        cls.get__name(),
                        cls.get__lastname(),
                        cls.get__cel(),
                        cls.get__doc(),
                        cls.get__email(),
                        cls.get__address(),
                        cls.get__country(),
                        cls.get__city(),
                        cls.get__anotaciones(),
                        cls.get__departamento()
                    ])
                cursor_client.close()
                return F"Cliente {cls.get__name()} Registrado Correctamente"
        except Exist as exist:
            return f"{exist}"
        
        except Exception as e:
            return f"{e}"
        finally:
            if conexion:
                DataBase.desconectar()
        
    @classmethod
    def buscar_client_name(cls, name=None):
        conexion = DataBase.conectar()
        if conexion:
            try:
                cursor_client = conexion.cursor()
                cursor_client.callproc("SearchOneClient", [name])

                for busqueda in cursor_client.stored_results():
                    resultado = busqueda.fetchone()
                    cls.__data = resultado

                return cls.__data if cls.__data else None
            
            except Exception as e:
                return f"{e}"
    
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
                cursor_client.callproc("DesactivarClient", [name])
                conexion.commit()
                cursor_client.close()
                return "client eliminado"
            except Exception as error:
                return f"Error al eliminar el client: {error}. Intente de nuevo"
            finally:
                DataBase.desconectar()

    @classmethod
    def buscar_clientes(cls):
        conexion = DataBase.conectar()
        if conexion:
            try:
                cursor_client = conexion.cursor()
                cursor_client.callproc("SearchClients")
                for i in cursor_client.stored_results():
                    res = i.fetchall()
                if res:
                    cls.__data = res
                    return cls.__data
                else:
                    raise Exception("No hay clientes registrados")
            except Exception as error:
                return f"Error al buscar los clientes: {error}. Intente de nuevo"
            finally:
                if conexion:
                    cursor_client.close()
                    DataBase.desconectar()