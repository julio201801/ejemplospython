#importamos la libreria para conectarnos al sql
#pip install pyodbc
import pyodbc
#variable para la conexion de la base de datos
#colocar el usuario administrador de la
server='192.168.0.131'
usuario="admin"
clave="123456"
#llevanos a cabo la conexion primera fomma
#conexion= pyodbc.connect(driver='{SQL server}',host=server)
#segunda forma
conexion=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';UID='+usuario+';PWD='+clave,autocommit=True)
print("conexión exitosa")

#creamos cursor para almacenar en memoria
cursor=conexion.cursor()
#crear un base de datos desde python
cursor.execute("CREATE DATABASE DB_PYTHON")

#cerrar conexion
conexion.close()