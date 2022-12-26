#importamos la libreria
import pyodbc
#conectar
server='192.168.0.131'
usuario="admin"
clave="123456"
db_name="db_PRUEBAA"
#segunda forma
conexion= pyodbc.connect(driver='{SQL server}',host=server,database=db_name)
print("conexión exitosa")

#creamos cursor para almacenar en memoria
cursor=conexion.cursor()
#crear un base de datos desde python
cursor.execute("CREATE TABLE ciudad(ciudad varchar(100) NOT NULL,pais varchar(100) NOT NULL)")



#cerrar la conexion
conexion.close()