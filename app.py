# instaciar la dependencia
from flask import Flask, jsonify, request
app = Flask(__name__)

#metodo
@app.route('/listo',methods=['GET'])
def saludo():
    return jsonify({'response': 'EL PRIMER EJEMPLO EN PYTHON'})

#LANZAR
if __name__ == '__main__':
     app.run(debug=True, port=5000)