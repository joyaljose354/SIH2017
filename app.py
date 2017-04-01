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
    kannur = { College of Engineering Thalassery ,
KALA MANDIR COLLEGE OF MUSIC AND DANCE KANNUR ,
Lasya College of Music  DancePilathara P.O.Kannur670 501 ,
Indian Naval Academy Ezhimala, 
Aditya Kiran College of Applied Studies Krishnagiri POKuttor,
AlMaquar Arabic CollegeDarul Aman NadukaniTaliparamba, 
AMSTECK Arts  Science College Kalliassery, 
A.W.H. AlBadar Special College Near New Bus stand Payyannur Kannur, 
Chinmaya Arts  College for women Govindagiri Chala ,
Chinmaya Institute of Technology Govindagiri.Chala Kannur, 
College of Applied Science NeruvambramPayyanur, 
College of Applied Science PattuvamKuttikkol ,
College of Applied SciencePinarayi Kannur, 
College of Applied SciencePO KuthuparambaKannur ,
College of Engineering and Technology Payyannur, 
CONCORD ARTS AND SCIENCE COLLEGEMUTTANUR, 
CoOperative Arts  Science CollegeMadai Pazhayangadi ,
Crescent B.Ed college Madayipara P.O. Payangadi, 
Darul Irshad Arabic College P.O. Paral Thalassery Kannur, 
DE PAUL ARTS AND SCIENCE COLLEGE, 
Deva Matha Arts  Science CollegePaisakari, 
Don Bosco Arts  Science CollegeAngadikkadavu, 
Don Bosco College Angadikadavu Kannur, 
EMS Memorial College of Applied ScienceVallithode Iritty Kannur, 
Govt. Brennen College DharmadamThalasseryKannur, 
Govt. Brennen College of Teacher Education Thalassery 
Govt. College of Engineering P.O. Parassinikadavu Kannur 
GOVT. COLLEGE PERINGOME 
GOVT COLLEGE THALASSERYCHOKLI 
Gurudev Arts  Science College MathilPOMathil 

Institute of Technology Mayyil Pavannoor Motta Kannur 
I.T.M College of Arts  ScienceMayyil 
Jaybees Training College of B. Ed. Kuttoor P.O. Mathamangalam 
Kannur Salafi B. Ed. College ChekkikulamKannur 
Keyi Sahib Training College Karimbam Taliparamba Kannur 
K.M.M Govt Womens CollegeKannur 
Mahatma Gandhi Arts  Science College ChendayadPO 
Mahatma Gandhi CollegeIrittiPOKeezhur 
Malabar B. Ed. Training College Peravoor 
Malabar Institute of Technology Anjarakandi Kannur 
Mary Matha Arts  Science College Alakode 
MECF College of Teacher Education Peringathur Kannur 
M.E.S CollegeNaravoor SouthPO Kuthuparamba 
MM KNOWLEDGE ARTS AND SCIENCE COLLEGE 
Morazha Cooperative Arts  Science College Morazha P.O.Kannur 
Naher Arts  Science College Kanhirode P.O KanhirodeVia Koodali Kannur 
N.A.M CollegeKallikandy 
Navajyothi College Cherupuzha P.O Chunda Kannur 670511 
NEST INSTITUTE OF HUMANITIES AND BASIC SCIENCES 
Nirmalagiri CollegePONirmalagiri 
Nusrathul Islam Arabic College P.O. Kadavathur Kannur 
Our College of Applied SciencesTimiri 
Payyannur College PayyannurPOEdat 
Pazhassiraja NSS CollegeMattannur 
Pilathara Coop Arts  Science CollegePazhichiyil P.O. Nareekamvalli Kannu 
P.K.M. College of Education Kaithapram P.O Madampam Kannur 
Rajeev Memorial College of Teacher Education Mattanur 
S.E.S College SreekandapuramKannur 
SIBGA Institute of Advanced Studies Irikkur 
Sir Syed CollegePO KarimbamTaliparamba 
Sir Syed Institute for Technical Studies 
SREENARAYAGURU COLLEGE OF ARTS AND SCIENCE 
Sree Narayana CollegeP.O Thottada 
SREE NARAYANA GURU COLLEGE OF ADVANCED STUDIES 
Sree Narayana Guru College of Engineering  Technology P.O. Chalakode Payyanur Kannur 
St. Josephs College Pilathara Kannur 
St Thomas College of Engineering and Technology Mattannur 
S.U.M. College of Teacher Education P.O. Mamba Kannu 
Taliparamba Arts  Science College PO Kanhirangad 
Vimal Jyothi Engineering College Jyothi Nagar Chemperi Kannur 
Vimal Jyothi Institute of Management and Research Chemperi Kannur 
Wadihuda Institute of Research and Advanced Studies Vilayancode Kannur 
Academy of Medical Sciences Pariyaram Medical College 
Academy of Pharmaceutical Sciences Pariyaram Medical College Campus Pariyaram Medical College P.O Kannur 
A.K.G. Memorial Cooperative College of Nursing Mavilayi Kannur 
Canossa College of Nursing. St. martin De Porres Hospital Cherukunnu 
College of Nursing ACME Pariyaram Kannur 
College of Nursing Kannur Medical College A unit of Prestige Educational Trust Anjarakandy Post Mamba Kannur 
College of Nursing Nettoor P.O. Thalassery 
COLLEGE OF NURSING THALASSERY 
College of Pharmacy Kannur Medical College 
Cooperative Institute of Health Sciences Thalassery. 
Crescent College of Nursing Mottambram Kannur 
CrescentCollege of Pharmaceutical Sciences Madaipara Payangadi 
DHANALAKSHMI COLLEGE OF NURSING 
Govt. Ayurveda College Kannur 
Govt Institute for paramedical Sciences Pilathara 
INSTITUTE OF PARAMEDICAL SCIENCES ANJARAKANDY 
Kannur DentalCollege Anjarakandy P.O. Mamba 
Kannur Medical College Anjarakandy Post Mamba Kannur 
Koyili College of Nursing Kannadiparamba P.OKannur 
Lourde College of Nursing Ariyil P.O. Taliparamba 
Malabar Cancer Centre College Thalassery 
Parassinikadavu Ayurveda Medical College Parassinikadavu 
Pariyaram Dental College A.C.M.E.Pariyaram Kannur 
SAJI V T 
John Paul Memorial B.Ed College Labbakkada Kanchiyar P.O. ldukki 685 511 
NATIONAL INSTITUTE OF FASHION TECHNOLOGY KANNUR 
Payyanur }

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
