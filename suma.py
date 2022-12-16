# instaciar la dependencia
from flask import Flask, jsonify, request
app = Flask(__name__)

#
@app.route('/suma', methods=["GET"])
def suma():
    total=8+6
    return jsonify({'total':total})
    
#lanza
if __name__ == '__main__':
     app.run(debug=True, port=5000)
