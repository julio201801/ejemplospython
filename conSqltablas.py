#importamos la libreria
import pyodbc
#conectar
server='192.168.0.131'
usuario="admin"
clave="123456"
db_name="db_PRUEBAA"
#segunda forma
#conexion= pyodbc.connect(driver='{SQL server}',host=server,database=db_name)
conexion=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+db_name+';UID='+usuario+';PWD='+clave,autocommit=True)

print("conexión exitosa")

#creamos cursor para almacenar en memoria
cursor=conexion.cursor()
#crear un base de datos desde python
cursor.execute("CREATE TABLE ciudad(city varchar(100) NOT NULL,pais varchar(100) NOT NULL)")
print("creo la tabla")
Variable_ciudad=[('lima','peru'),('cuzco','peru'),('piura','peru'),
                ('quito','ecuador'),('cuenca','ecuador'),('machala','ecuador'),
                ('la paz','bolivia'),('cochabamba','bolivia'),('beni','bolivia')]
#inserta registros
cursor.executemany("INSERT INTO ciudad VALUES(?,?)",Variable_ciudad)
print('insert las ciudades')
cursor.commit()
#cerrar la conexion
conexion.close()