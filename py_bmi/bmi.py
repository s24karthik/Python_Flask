# Service API to calculate BMI #
from flask import request, jsonify
from services import services as app

@app.route("/bmi", methods=['POST'])
def bmi():
	data = request.get_json()
	weight = float(data["weight in kg"])
	height = float(data["height in cm"])

	result = float((weight/(height*height))*10000)
	return jsonify("BMI IS:",result)