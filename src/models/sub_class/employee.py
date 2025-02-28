# Imports
from models.database import DataBase
from models.people import People

# Librarys

class Employee(People):
    # Method Constructor
    @classmethod
    def __init__(
        cls,
        id_empleado: int = None,
        salario: str = None,
        arl: str = None,
        eps: str = None
        ):

        cls.__id_empleado = id_empleado
        cls.__salario = salario
        cls.__arl = arl
        cls.__eps = eps

    # Methods GET of each attribute
    @classmethod
    def get__id_empleado(cls):
        return cls.__id_empleado
    
    @classmethod
    def get__salario(cls):
        return cls.__salario
    
    @classmethod
    def get__arl(cls):
        return cls.__arl
    
    @classmethod
    def get__eps(cls):
        return cls.__eps
        