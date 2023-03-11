from flask import Flask,request,jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/Get',methods=['GET'])
def hello():
    language = request.args.get('filter')
    response = {"data":[{"AppointmentId":3,"Text":"Isssnstall New Router in Dev Room","Description":None,"StartDate":"2021-04-26T21:30:00.000Z","EndDate":"2021-04-26T22:30:00.000Z","AllDay":False,"RecurrenceRule":None,"RecurrenceException":None}]}
    response = jsonify(response)
    #response.headers.add('Access-Control-Allow-Origin', '')
    return response
