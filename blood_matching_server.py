from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

server_name = "http://vcm-7631.vm.duke.edu:5002"


@app.route("/get_patients/<name>", methods=['GET'])
def get_patients(name):
    indata = request.get_json()
    ID1 = indata["Recipient"]
    ID2 = indata["Donor"]
    return jsonify(ID1), jsonify(ID2)


@app.route("/get_blood_type/<id>", methods=['GET'])
def get_blood_type(id):
    indata = request.get_json()
    return indata


@app.route("/match_check", methods=['POST'])
def match_check():
    indata = request.get_json()
    return indata


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
