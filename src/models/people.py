# Imports
import re

class People:
    # Method Constructor
    @classmethod
    def __init__(cls,
        name: str = "vacio",
        lastname: str = "vacio",
        cel: str = "vacio",
        doc: str = "vacio",
        email: str  = "vacio",
        address: str = "vacio",
        country: str = "vacio",
        city: str = "vacio" ):
        
        cls.__name = name
        cls.__lastname = lastname
        cls.__cel = cel
        cls.__doc = doc
        cls.__email = email
        cls.__address = address
        cls.__country = country
        cls.__city = city

    # Methods GET of each attribute
    @classmethod
    def get__name(cls):
        return cls.__name
    
    @classmethod
    def get__lastname(cls):
        return cls.__lastname
    
    @classmethod
    def get__cel(cls):
        return cls.__cel

    @classmethod
    def get__doc(cls):
        return cls.__doc
    
    @classmethod
    def get__email(cls):
        return cls.__email
    
    @classmethod
    def get__address(cls):
        return cls.__address   
    
    @classmethod
    def get__country(cls):
        return cls.__country
    
    @classmethod
    def get__city(cls):
        return cls.__city
    
    # Methods SET of each attribute
    @classmethod
    def set_name(cls,name):
        if re.match(r'^[A-Za-z\s]{3,50}$', name):
            return True
        else:
            raise ValueError("Nombre invalido")
    
    @classmethod
    def set_lastname(cls,lastname):
        if re.match(r'^[A-Za-z\s]{3,50}$', lastname):
            return True
        else:
            raise ValueError("Apellido invalido")

    @classmethod
    def set_cel(cls,cel):
        if 12 > len(cel) > 6:
            return True
        else:
            raise ValueError("Celular Invalido")

    @classmethod
    def set_doc(cls,doc):
        if 12 > len(doc) > 6:
            return True
        else:
            raise ValueError("Documento Invalido")

    @classmethod
    def set_email(cls,email):
        if "@" in email and 10 < len(email):
            return True
        else:
            raise ValueError("Email invalido")

    @classmethod
    def set_country(cls,country):
        if re.match(r'^[A-Za-z\s]{3,100}$', country):
            return True
        else:
            raise ValueError("Pais invalido")
        
    @classmethod
    def set_city(cls,city):
        if re.match(r'^[A-Za-z\s]{3,100}$', city):
            return True
        else:
            raise ValueError("Ciudad invalida")