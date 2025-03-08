# Imports
from database import DataBase
from people import People

# Librarys
import re

# Seudo class
class Exist(Exception):
    pass

class Employee(People):
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
        sal: float = None,
        arl: float = None,
        eps: str = None,
        data = None
        ):
        super().__init__(name,lastname,cel,doc,email,address,country,city)

        cls.__sal = sal
        cls.__arl = arl
        cls.__eps = eps
        cls.__data = data

    # Methods GET of each attribute
    @classmethod
    def get__sal(cls):
        return cls.__sal
    
    @classmethod
    def get__arl(cls):
        return cls.__arl
    
    @classmethod
    def get__eps(cls):
        return cls.__eps
    
    @classmethod
    def get__data(cls):
        return cls.__data
    
    # Methods SET of each attribute
    @classmethod
    def set_sal(cls,sal):
        if re.match(r'^[A-Za-z\s]{1,12}$', sal):
            return True
        else:
            raise ValueError("Salario invalida")
        
    @classmethod
    def set_arl(cls,arl):
        if re.match(r'^[A-Za-z\s]{1,12}$', arl):
            return True
        else:
            raise ValueError("Salario invalida")
        
    @classmethod
    def set_eps(cls,eps):
        if re.match(r'^[A-Za-z\s]{3,50}$', eps):
            return True
        else:
            raise ValueError("Eps invalida")
        
    @classmethod
    def validar_datos(cls,name,lastname,cel,doc,email,country,city,sal,arl,eps):
        try:
            if (cls.set_name(name) and
                cls.set_lastname(lastname) and
                cls.set_cel(cel) and
                cls.set_doc(doc) and
                cls.set_email(email) and
                cls.set_country(country) and
                cls.set_city(city) and 
                cls.set_sal(sal) and 
                cls.set_arl(arl) and 
                cls.set_eps(eps)):
                return True
            else:
                return False
        except ValueError as ve:
            return f"{ve}"
        except Exception as e:
            return f"{e}"
    
    @classmethod
    def registrar_employee(cls):
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
                cls.get__sal(),
                cls.get__arl(),
                cls.get__eps()
            )
            if validar:
                doc = cls.get__doc()
                employeee = cls.buscar_employee_name(doc)
                if employeee:
                    raise Exist("El empleado ya está registrado")
                else:
                    cursor_employee = conexion.cursor()
                    cursor_employee.callproc("RegistEmployee", [
                        cls.get__name(),
                        cls.get__lastname(),
                        cls.get__cel(),
                        cls.get__doc(),
                        cls.get__email(),
                        cls.get__address(),
                        cls.get__country(),
                        cls.get__city(),
                        cls.get__sal(),
                        cls.get__arl(),
                        cls.get__eps()
                    ])
                cursor_employee.close()
                return F"Empleado {cls.get__name()} Registrado Correctamente"
        except Exist as exist:
            return f"{exist}"
        
        except Exception as e:
            return f"{e}"
        finally:
            if conexion:
                DataBase.desconectar()
        
    @classmethod
    def buscar_employee_name(cls, name=None):
        conexion = DataBase.conectar()
        if conexion:
            try:
                cursor_employee = conexion.cursor()
                cursor_employee.callproc("SearchOneEmployee", [name])

                for busqueda in cursor_employee.stored_results():
                    resultado = busqueda.fetchone()
                    cls.__data = resultado

                return cls.__data if cls.__data else None
            
            except Exception as e:
                return f"{e}"
    
            finally:
                if conexion:
                    cursor_employee.close()
                    DataBase.desconectar()
        
    @classmethod
    def eliminar_employee(cls, name = None):
        conexion = DataBase.conectar()
        employeee = cls.buscar_employee_name(name)
        if employeee:
            try:
                cursor_employee = conexion.cursor()
                cursor_employee.callproc("DesactiveEmployee", [name])
                conexion.commit()
                cursor_employee.close()
                return "employee eliminado"
            except Exception as error:
                return f"Error al eliminar el employee: {error}. Intente de nuevo"
            finally:
                DataBase.desconectar()

    @classmethod
    def buscar_employees(cls):
        conexion = DataBase.conectar()
        if conexion:
            try:
                cursor_employee = conexion.cursor()
                cursor_employee.callproc("SearchEmployees")
                for i in cursor_employee.stored_results():
                    res = i.fetchall()
                if res:
                    cls.__data = res
                    return cls.__data
                else:
                    raise Exception("No hay empleados registrados")
            except Exception as error:
                return f"Error al buscar los empleados: {error}. Intente de nuevo"
            finally:
                if conexion:
                    cursor_employee.close()
                    DataBase.desconectar()

em = Employee("Juan",
"Pérez",
"123456789",
"123456712",
"juan.perez@example.com",
"Calle 123",
"Colombia",
"Bogotá",
3000.00,
150.00,
"EPS001")
reg = em.buscar_employee_name("juan")
print(reg)
