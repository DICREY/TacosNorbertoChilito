import mysql.connector as con
import mysql.connector.errorcode as err
class DataBase:
    __HOST = '127.0.0.1'
    __USER = 'root'
    __PASSWORD = ''
    __DATABASE = 'tacos_norberto_chilito'
    __PORT = 3306
    __conexion = None
    __cursor = None

    @classmethod
    def conectar(cls):
        try:
            cls.__conexion = con.connect(
                host=cls.__HOST,
                user=cls.__USER,
                password=cls.__PASSWORD,
                database=cls.__DATABASE,
                port=cls.__PORT
            )
            cls.__cursor = cls.__conexion.cursor()
            return cls.__conexion
        except con.Error as error:
            if err.errno == error.ER_ACCESS_DENIED_ERROR:
                print('Verifique las credenciales de conexión')
            elif err.errno == error.ER_BAD_DB_ERROR:
                print('Base de datos no existe')
            elif err.errno == error.ER_BAD__HOST_ERROR:
                print('El nombre del host es incorrecto')
            elif err.errno == error.ER_CONN__HOST_ERROR: 
                print('Error al intentar conectar con el host')
            elif err.errno == error.ER_DBACCESS_DENIED_ERROR:
                print('Acceso denegado a la base de datos')
            elif err.errno == error.CR_CONN__HOST_ERROR:
                print('No se pudo conectar al servidor MySQL')
            else:
                print(f'Error desconocido: {err}')
        except Exception as ex:
            print(f'Error general: {ex}')

    @classmethod
    def desconectar(cls):
        try:
            if cls.__cursor:
                cls.__cursor.close()
            else:
                cls.__conexion.close()
        except con.Error as err:
            print(f'Error al cerrar la conexión: {err}')

dataBase = DataBase()