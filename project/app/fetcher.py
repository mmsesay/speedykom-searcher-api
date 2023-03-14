"""
Filename        :   fetcher.py
Description     :   This file has a function that make request to the external api
Author          :   Muhammad Sesay
Email           :   contact@maej.dev
Started writing :   8/March/2023
Completed on    :   in progress
"""

import requests
from requests.exceptions import Timeout
from flask import jsonify

def get_data_from_health_gov(params: str):
    """
    Fetches data from health gov health finder
    :param params: this is the keyword to query
    :return : the json data response if available or an error
    """
    try:
      # make a call to the external api and get the response
      response = requests.get(f'https://health.gov/myhealthfinder/api/v3/topicsearch.json?keyword={params}', timeout=4).json()

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
    except Timeout:
      return jsonify({
            "status": 408,
            "data": "The request has timeout"
        })

def get_all_data_from_health_gov():
    """
    Fetches all data from health gov health finder
    :return : the json data response if available or an error
    """
    try:
      # make a call to the external api and get the response
      response = requests.get(f'https://health.gov/myhealthfinder/api/v3/topicsearch.json?keyword=health', timeout=3).json()

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
    except Timeout:
      return jsonify({
            "status": 408,
            "data": "The request has timeout"
        })

def get_single_data_from_health_gov(params: str):
    """
    Fetches data for a single item from health gov health finder
    :param params: this is the keyword to query
    :return : the json data response if available or an error
    """
    try:
      # make a call to the external api and get the response
      response = requests.get(f'https://health.gov/myhealthfinder/api/v3/topicsearch.json?topicId={params}', timeout=3).json()

      # validate we got available result and return it otherwise 
      if response['Result']['Total'] > 0:
        items = []
        for item in response['Result']['Resources']['Resource']:
          items = item['Sections']['section']
          
        return jsonify({
            "status": 200,
            "data": {
              "records": items,
              "totalRecordsCount": response['Result']['Total']
            }
        })
      else:
        return jsonify({
            "status": 404,
            "data": "No result match for the provided id"
        })
    except Timeout:
      return jsonify({
            "status": 408,
            "data": "The request has timeout"
        })