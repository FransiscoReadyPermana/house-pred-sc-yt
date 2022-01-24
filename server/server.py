from urllib import response
from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/hallo', methods=['GET']) 

@app.route('/predict', methods=['POST'])

def predict():
  total_sqft = float(request.form['total_sqft'])
  location = request.form['location']
  bhk = int(request.form['bhk'])
  bath = int(request.form['bath'])
  response = jsonify({'estimated_price': util.getEstimatedPrice(location, total_sqft, bath, bhk)})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

def getLocationName():
  response = jsonify({'location': util.getLocationName()})  

if __name__ == '__main__':
    app.run(debug=True)
