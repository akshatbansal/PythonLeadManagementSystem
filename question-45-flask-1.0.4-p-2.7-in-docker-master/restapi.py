from flask import Flask, Response, jsonify, request
from flask_api import status
import databaseAccess as dataAccess
from Person import person
import json
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/leads", methods = ["GET"])
def fetchLead():
    lead_id = request.args.get('leadId', None)
    print(lead_id)
    if lead_id == 0 or lead_id is None:
        content=  jsonify(
                  {'status': 'failure',
                   'reasons':'explaination'})
        return content, status.HTTP_400_BAD_REQUEST
    else:
        databaseAcc = dataAccess.DatabaseAccess
        userData = databaseAcc.fetchMethod(lead_id)
        if userData is None:
            content = {}
            return content, status.HTTP_404_NOT_FOUND
        else:
            content=  jsonify(
                {
                'status': 'success',
                'result':{
                    'id': userData.id,
                    'First Name': userData.firstname,
                    'Last Name': userData.lastname, 
                    'Mobile': str(userData.mobile),
                    'Email'  : userData.email,
                    'Location Type' : userData.locationtype,
                    'Location String' : userData.locationstring,
                    'Status':userData.status,
                    'Communication': userData.communication       
                }
                })
            return content, status.HTTP_200_OK
        

@app.route("/api/leads/create")
def create():
    return dataAccess.DatabaseAccess.createTable()

@app.route("/api/leads", methods = ["Post"])        
def loadPerson():
    data = request.get_json()
    id = data["id"]
    firstname = data["firstname"]
    lastname = data["lastname"]
    mobile = data["mobile"]
    email = data["email"]
    locationtype = data["locationtype"]
    locationstring = data["locationstring"]
    status = data["status"]
    communication = data["communication"]
    
    pers= person(id,firstname, lastname, mobile, email, locationtype, locationstring, status, communication)
    dataAccess.DatabaseAccess.insertData(pers)
    return  "success"

@app.route("/api/drop")        
def drop():
    databaseAcc = data.DatabaseAccess
    databaseAcc.deletTable()
    return  "success"

if __name__ == "__main__":
    app.run( port=5002, debug=True)
