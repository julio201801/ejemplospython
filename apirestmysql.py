# ejemplo de AnderCode 
#https://www.youtube.com/watch?v=-qZoZhFHo8Q
from flask import Flask, jsonify, request
from flask_sqlalchemy import sqlalchemy
from flask_marshmallow import marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']
#instalar para este ejemplo pip install flask-sqlalchemy
# pip install flask-marshmallow
# pip install marshmallow-sqlalchemy
# pip install pymysql
@app.route('/demo',methods=['GET'])
def demo():
    return jsonify({'mensaje':'hola peru'})


#LANZAR
if __name__ == '__main__':
     app.run(debug=True, port=5008)
    