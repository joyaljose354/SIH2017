#!/usr/bin/env python

import urllib
import json
import os


from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode
from flask import Flask
from flask import request
from flask import make_response


def myfunc(qry):
    DB_NAME='shihad'
    cnx = mysql.connector.connect(user='root')
    cursor = cnx.cursor()
    cnx.database = DB_NAME

    cursor.execute(qry)

    return



# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "college_details":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("college-names")
    cost = {'NSS':5000, 'CET':200, 'FISAT':300, 'NIT':400, 'GEC':500}
    speech = "The college details  " + zone + " is " + str(cost[zone])

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "UGC_Pandit"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
