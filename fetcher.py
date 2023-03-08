import requests
from flask import jsonify

def get_data_from_health_gov(params: str):
    # make a call to the external api and get the response
    response = requests.get(f'https://health.gov/myhealthfinder/api/v3/topicsearch.json?keyword={params}').json()

    # validate we got available result and return it otherwise 
    if response['Result']['Total'] > 0:
      return jsonify({
          "status": 200,
          "data": {
            "records": response['Result']['Resources']['Resource'],
            "totalRecordsCount": response['Result']['Total']
          }
      })
    else:
      return jsonify({
          "status": 404,
          "data": "No result match for the searched keyword"
      })