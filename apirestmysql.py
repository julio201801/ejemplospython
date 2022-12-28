# ejemplo de AnderCode 
#https://www.youtube.com/watch?v=-qZoZhFHo8Q
#https://www.sqlalchemy.org/
#instalar para este ejemplo pip install flask-sqlalchemy
# pip install flask-marshmallow
# pip install marshmallow-sqlalchemy
# pip install pymysql
#https://flask-marshmallow.readthedocs.io/en/latest/
#documentacion de java
#https://github.com/osopromadze/Spring-Boot-Blog-REST-API
from flask import Flask, jsonify, request
#from flask_sqlalchemy import Sqlalchemy
from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import marshmallow
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:@localhost/myDbName"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
ma = Marshmallow(app)
#creacion de la tabla
class categoria(db.Model):
    cat_id = db.Column(db.Integer,primary_key=True)
    cat_nom= db.Column(db.String(100))
    cat_desc=db.Column(db.String(100))
    #contructor
    def __init__(self,cat_nom,cat_desc):
        self.cat_nom = cat_nom
        self.cat_desc = cat_desc
#crear table
db.create_all()
#Esquema categoria
class categoriaSchema(ma.Schema):
    class Meta:
        fields=('cat_id','cat_nom','cat_desc')
#una sola respuesta        
categoria_schema=categoriaSchema()
#muchas respuestas
categorias_schema=categoriaSchema(many=True)
#GET
@app.route('/categorias',methods=['GET'])
def get_categorias():
    all_categorias=categoria.query.all()
    result=categorias_schema.dump(all_categorias)
    return jsonify(result)

@app.route('/demo',methods=['GET'])
def demo():
    return jsonify({'mensaje':'hola peru'})


#LANZAR
if __name__ == '__main__':
     app.run(debug=True, port=5000)
    