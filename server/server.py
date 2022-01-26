from urllib import response
from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/hallo', methods=['GET']) 

def hallo():
  return "Hallo"

@app.route('/predict', methods=['GET','POST'])

def predict():
  total_sqft = float(request.form['total_sqft'])
  location = request.form['location']
  bhk = int(request.form['bhk'])
  bath = int(request.form['bath'])
  response = jsonify({'estimated_price': util.getEstimatedPrice(location, total_sqft, bath, bhk)})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/get_location_name', methods=['GET'])

def get_location_name():
  response = jsonify({
    'location': util.get_location_name()
  })  
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response



if __name__ == '__main__':
  util.loadSavedArtifacts()
  app.run()
