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
        departamento: str = None
        ):

        cls.__id_cliente = id_cliente
        cls.__anotaciones = anotaciones
        cls.__departamento = departamento

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
        