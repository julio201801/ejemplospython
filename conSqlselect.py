import pyodbc ##pip install pyodbc
import pandas as pd #pip install pandas
server='192.168.0.131'
usuario="admin"
clave="123456"

db_name="db_PRUEBAA"
#segunda forma
#conexion= pyodbc.connect(driver='{SQL server}',host=server,database=db_name)
conexion=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+db_name+';UID='+usuario+';PWD='+clave,autocommit=True)
print("conexion exitosa")
#leer la informacion de la base de datos
ciudad=pd.read_sql("SELECT * FROM ciudad",conexion)
#cerrar conexion
conexion.close()
#https://github.com/wpcodevo/python_fastapi
