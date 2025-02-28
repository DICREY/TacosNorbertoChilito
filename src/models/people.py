# Imports
from models.database import DataBase

# librarys
import bcrypt
import re

class People:
    # Method Constructor
    @classmethod
    def __init__(
        cls,
        name: str= None,
        lastname: str= None,
        cel: str= None,
        doc: str= None,
        email: str = None,
        address: str= None,
        country: str= None,
        city: str= None,
        state: bool= True
            ):
        
        cls.__name = name
        cls.__lastname = lastname
        cls.__cel = cel
        cls.__doc = doc
        cls.__email = email
        cls.__address = address
        cls.__country = country
        cls.__city = city
        cls.__state = state

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
    
    @classmethod
    def get__state(cls):
        return cls.__state
    
    # Methods SET of each attribute
        