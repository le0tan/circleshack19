import flask
from flask import request, jsonify, abort, Response, render_template
import json
import calc
import misc

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    #calc.from_postal_code_to_income_distribution(12345)
    return render_template("index.html")

@app.route('/api/v1/postal_code_to_income', methods=['GET'])
def postal_code_to_income():
    if 'postal_code' in request.args:
        return calc.from_postal_code_to_income_distribution(int(request.args['postal_code']))
    else:
        abort(400, "Please provide postal_code as an argument.")

@app.route('/api/v1/average_income_by_area', methods=['GET'])
def average_income_by_area():
    with open('monthly_income_by_area.json') as input:
        data = json.load(input)
        d = {}
        for i in range(len(data)):
            d[data[i]['Planning Area']] = data[i]
        return d

@app.route('/api/v1/district_code', methods=['GET'])
def get_district_code_from_postal_code():
    if 'postal_code' in request.args:
        return misc.get_district_code(postal_code=request.args['postal_code'])
    else:
        abort(400, "Please provide postal_code as an argument.")

app.run()