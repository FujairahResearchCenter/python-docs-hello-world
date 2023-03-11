from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/Get',methods=['GET']")
def hello():
    language = request.args.get('filter')
    t = {"data":[{"AppointmentId":3,"Text":"Isssnstall New Router in Dev Room","Description":None,"StartDate":"2021-04-26T21:30:00.000Z","EndDate":"2021-04-26T22:30:00.000Z","AllDay":False,"RecurrenceRule":None,"RecurrenceException":None}]}
    return t
