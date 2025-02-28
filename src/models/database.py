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
            print('Conexión abierta...')
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
    def ejecutar_query(cls, query, params=None):
        try:
            cls.__cursor.execute(query, params)
            if query.strip().lower().startswith('select'):           
                resultado = cls.__cursor.fetchall()
                if resultado:
                    for fila in resultado:
                        print(fila)
                else:
                    print('No hay resultados...')
                    return None
                return resultado
            else:
                cls.conexion.commit()
                print('Query ejecutada con éxito')
        except con.ProgrammingError as pe:
            print(f'Error en la query: {pe}')
        except con.DataError as de:
            print(f'Error de datos: {de}')
        except con.IntegrityError as ie:
            print(f'Error de integridad de datos: {ie}')
        except con.OperationalError as oe:
            print(f'Error operacional: {oe}')
        except con.InternalError as ie:
            print(f'Error interno del sistema: {ie}')
        except con.NotSupportedError as nse:
            print(f'Error de operación no soportada: {nse}')
        except con.InterfaceError as ie:
            print(f'Error de interfaz de conexión: {ie}')
        except Exception as ex:
            print(f'Error general: {ex}')

    @classmethod
    def desconectar(cls):
        try:
            if cls.__cursor:
                cls.__cursor.close()
            if cls.__conexion == None:
                print('No hay una conexión abierta. Intente de nuevo')
            else:
                cls.__conexion.close()
                print('Conexión cerrada...')
        except con.Error as err:
            print(f'Error al cerrar la conexión: {err}')

DataBase.conectar()