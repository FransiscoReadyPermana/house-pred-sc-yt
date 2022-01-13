from urllib import response
from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/hallo', methods=['GET']) 

def getLocationName():
  response = jsonify({'location': util.getLocationName()})  

if __name__ == '__main__':
    app.run(debug=True)
