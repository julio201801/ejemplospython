#instanciar al flask
from flask import Flask, jsonify, request
app= Flask(__name__)

#crear el controler
@app.route('/multiplica/<int:uno>/<int:dos>',methods=["GET"])
def multiplica(uno,dos):
    total= uno * dos
    return jsonify({'total':total})

#lanza
if __name__=='__main__':
    app.run(debug=True,port=5000)
