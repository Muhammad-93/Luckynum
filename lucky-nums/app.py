from flask import Flask, render_template, request
from flask.helpers import url_for
from flask.json import jsonify
from flask.wrappers import Response
import random

import requests

app = Flask(__name__)

API_BASE_URL = "http://numbersapi.com"

@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route("/api/get-lucky-num", methods=["POST"])
def luckynum():
    """Return JSON body"""

    name = request.json.get("name", None)
    email = request.json.get("email", None)
    year = request.json.get("year", None)
    color = request.json.get("color", None)

    response = {}
    if name is None or name == "":
        response["errors"] = {"name": ["This field is required"]}
    
    if email is None or email == "":
        #response["errors"] = {"email": ["This field is required"]}
        if "errors" in response:
            response["errors"]["email"] = ["This field is required"]
        else:
            response["errors"] = {"email": ["This field is required"]}
    
    if year is None or year == "":
        if "errors" in response:
            response["errors"]["year"] = ["This field is required"]
        else:
            response["errors"] = {"year": ["This field is required"]}
     
    if year is not "" and int(year) not in range(1900, 2000):
        if "errors" in response:
            if "year" in response["errors"]:
                response["errors"]["year"].append("must be between 1900 and 2000")
            else:
                response["errors"]["year"] = ["must be between 1900 and 2000"]
        else:
            response["errors"] = {"year": ["must be between 1900 and 2000"]}
     
    if color is None or color == "":
        if "errors" in response:
            response["errors"]["color"] = ["This field is required"]
        else:
            response["errors"] = {"color": ["This field is required"]}
    
    if color not in ['red', 'green', 'orange', 'blue']:
        if "errors" in response:
            if "color" in response["errors"]:
                response["errors"]["color"].append("Invalid value, must be one of: red, green, orange, blue")
            else:
                response["errors"]["color"] = ["Invalid value, must be one of: red, green, orange, blue"]
        else:
            response["errors"] = {"color": ["Invalid value, must be one of: red, green, orange, blue"]}

    num = random.randint(1,100) 

    if "errors" not in response:
        url = f"{API_BASE_URL}/{num}?json"
        res = requests.get(url)
        r = res.json()
        response["num"] = {"fact": r["text"], 
        "num": num}
        x = response["num"]

        
        url2 = f"{API_BASE_URL}/{year}/year?json"
        res2 = requests.get(url2)
        r2 = res2.json()
        response["year"] = {"fact": r2["text"], 
        "year": year}
        y = response["year"]
        

    return jsonify(response)







