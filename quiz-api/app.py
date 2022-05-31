from flask import Flask, request
import jwt_utils
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def IsLoginCorrect():
	payload = request.get_json()
	print(payload)
	if payload["password"] == "Vive l'ESIEE !":
		token = jwt_utils.build_token()
		return {"token" : token}, 200
	else :
		return '', 401

if __name__ == "__main__":
    app.run()