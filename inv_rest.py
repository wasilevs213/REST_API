#!/bin/python3
from flask import Flask, jsonify, make_response, request
import os
import json
import pickle

dir_collection = "./collection"

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/inv/api/v1.0/lists', methods=['GET'])
def get_lists():
    files = os.listdir(dir_collection)
    return jsonify({'return OPS': files})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/inv/api/v1.0/new', methods=['POST'])
def create_record():
    if not request.json or not 'version' in request.json:
        abort(400)
    hostname = dir_collection + '/' + request.json['hostname']

#    file_id = open(hostname, 'w')

    inp_string = request.json
    pickle.dump( inp_string, open( hostname, "wb" ))
    return jsonify({'return OPS': inp_string}), 201

############################
if __name__ == '__main__':
    app.run(debug=True)
