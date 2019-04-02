#!/usr/bin/env python3
# 
from flask import Flask, render_template, request, json
import datetime

dataFile = 'data/units.json'
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/addUnit',methods=['POST'])
def addUnit():
    # read the posted values from the UI
    _name = request.form['inputName']
    _type = request.form['inputType']

    # validate the received values
    if _name and _type:
        with open(dataFile, "r+") as json_file:  
            unitData = json.load(json_file)
            unitData.append({ "id":len(unitData), "unitName":_name, "unitUser":"", "unitTime":"" } )
            json_file.seek(0)
            json.dump(unitData, json_file)
            print('Added unit ' + _name)
            return json.dumps({'status':'OK'})
    return 'Failed to add unit ' + _name

@app.route('/getUnits')
def getUnits():
    with open(dataFile) as json_file:  
        unitData = json.load(json_file)
        return json.dumps(unitData)
    print("Failed to read unit data")
    return "[]"

@app.route('/releaseUnit',methods=['POST'])
def releaseUnit():
    # read the posted values from the UI
    _id = request.form['id']
    # validate the received values
    if _id:
        with open(dataFile, "r+") as json_file:
            unitData = json.load(json_file)
            print('Release unit id ' + str(_id))
            for unit in unitData:
                if unit["id"] == int(_id):
                    unit["unitUser"] = ""
                    unit["unitTime"] = ""
                    json_file.seek(0)
                    json.dump(unitData, json_file)
                    json_file.truncate()
                    print('Released unit ' + unit["unitName"])
                    return json.dumps({'status':'OK'})
    return json.dumps({'status':'Failure'})

@app.route('/claimUnit',methods=['POST'])
def claimUnit():
    # read the posted values from the UI
    _id = request.form['id']
    _user = request.form['unitUser']
    # validate the received values
    if _id and _user:
        with open(dataFile, "r+") as json_file:
            unitData = json.load(json_file)
            print('Claim unit id ' + str(_id))
            for unit in unitData:
                if unit["id"] == int(_id):
                    unit["unitUser"] = _user
                    unit["unitTime"] = datetime.datetime.now().date().strftime("%A-%d-%B-%Y")
                    json_file.seek(0)
                    json.dump(unitData, json_file)
                    json_file.truncate()
                    print('Claimed unit ' + unit["unitName"])
                    return json.dumps({'status':'OK'})
    return json.dumps({'status':'Failure'})

if __name__ == "__main__":
    app.run()