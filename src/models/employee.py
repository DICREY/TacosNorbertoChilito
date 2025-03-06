# Imports
from database import DataBase
from people import People 

# Librarys

class Employee(People):
    # Method Constructor
    @classmethod
    def __init__(
        cls,
        sal: float = None,
        arl: float = None,
        eps: str = None,
        data = None
        ):

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
    
    # def catch_data(cls):
        # cls.__name = ;
    
    @classmethod
    def registrar_employee(cls):
        conexion = DataBase.conectar()
        employee = cls.buscar_employee_name()
        if not employee:
            try:
                cursor_employee = conexion.cursor()
                cursor_employee.callproc('Registemployee', [
                    cls.get__name,
                    cls.get__lastname,
                    cls.get__cel,
                    cls.get__doc,
                    cls.get__email,
                    cls.get__address,
                    cls.get__country,
                    cls.get__city,
                    cls.get__sal,
                    cls.get__arl,
                    cls.get__eps
                ])
            except Exception as e:
                return f'Error al buscar employee: {e}'
            finally:
                if conexion:
                    cursor_employee.close()
                    DataBase.desconectar()
        else:
            return 'Ya existe'
        
    @classmethod
    def buscar_employee_name(cls, name=None):
        conexion = DataBase.conectar()
        if conexion:
            try:
                cursor_employee = conexion.cursor()
                cursor_employee.callproc('SearchemployeeName', [name])
                for busqueda in cursor_employee.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        cls.__data = resultado
                        print(cls.__data)
                        return 'employee encontrado'
                    else:
                        return 'employee not encontrado'
            except Exception as e:
                return e
            finally:
                if conexion:
                    cursor_employee.close()
                    DataBase.desconectar()
        
    @classmethod
    def eliminar_employee(cls, name = None):
        conexion = DataBase.conectar()
        employee = cls.buscar_employee_name(name)
        if employee:
            try:
                cursor_employee = conexion.cursor()
                cursor_employee.callproc('Desactivaremployee', [name])
                conexion.commit()
                cursor_employee.close()
                return 'employee eliminado'
            except Exception as error:
                return f'Error al eliminar el employee: {error}. Intente de nuevo'
            finally:
                DataBase.desconectar()

    @classmethod
    def buscar_employees(cls):
        conexion = DataBase.conectar()
        if conexion:
            try:
                cursor_employee = conexion.cursor()
                cursor_employee.callproc('SearchEmployees')
                for i in cursor_employee.stored_results():
                    res = i.fetchall()
                if res:
                    cls.__data = res
                    return cls.__data
                else:
                    return "No hay employee registrados"
                
                return
            except Exception as error:
                return f'Error al buscar los employee: {error}. Intente de nuevo'
            finally:
                if conexion:
                    cursor_employee.close()
                    DataBase.desconectar()


cl = Employee()
# search = cl.buscar_employee_name("cristi")
# print(search)
# delete = cl.eliminar_employee("123456789")
# print(delete)
# regis = cl.registrar_employee(
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
all = cl.buscar_employees()
print(all)