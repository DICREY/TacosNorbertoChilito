# Imports
from models.database import DataBase

class Products:
    # Method Constructor
    @classmethod
    def __init__(
        cls,
        part: str = None,
        reference: str = None,
        incrustation: str = None,
        thread: str = None,
        tip: str = None,
        laminated: str = None,
        incrustation_tip: str = None,
        cap: str = None,
        weight: float = 0.0,
        process: str = None,
        accessory: str = None,
        color_accessory: str = None,
        description: str = None
        ):

        cls.__part = part
        cls.__reference = reference
        cls.__incrustation = incrustation
        cls.__thread = thread
        cls.__tip = tip
        cls.__laminated = laminated
        cls.__incrustation_tip = incrustation_tip
        cls.__cap = cap
        cls.__weight = weight
        cls.__process = process
        cls.__accessory = accessory
        cls.__color_accessory = color_accessory
        cls.__description = description

    # Methods GET of each attribute
    @classmethod
    def get__part(cls):
        return cls.__part
    
    @classmethod
    def get__reference(cls):
        return cls.__reference
    
    @classmethod
    def get__incrustation(cls):
        return cls.__incrustation
    
    @classmethod
    def get__thread(cls):
        return cls.__thread
    
    @classmethod
    def get__tip(cls):
        return cls.__tip
    
    @classmethod
    def get__laminated(cls):
        return cls.__laminated
    
    @classmethod
    def get__incrustation_tip(cls):
        return cls.__incrustation_tip
    
    @classmethod
    def get__cap(cls):
        return cls.__cap
    
    @classmethod
    def get__weight(cls):
        return cls.__weight
    
    @classmethod
    def get__process(cls):
        return cls.__process
    
    @classmethod
    def get__accessory(cls):
        return cls.__accessory
    
    @classmethod
    def get__color_accessory(cls):
        return cls.__color_accessory
    
    @classmethod
    def get__description(cls):
        return cls.__description
