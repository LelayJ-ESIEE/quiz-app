from flask import Flask, request
import json
import jwt_utils
import database
from question import Question
import sqlite3

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
	# get sent login payload
	payload = request.get_json()
	# check if the password is right
	if payload["password"] == "Vive l'ESIEE !":
		# generate token  and return it with HTTP code 200 (OK)
		token = jwt_utils.build_token()
		return {"token" : token}, 200
	else :
		# return no token with HTTP code 401 (Unauthorized)
		return '', 401

@app.route('/questions', methods=['POST'])
def addQuestion():
	# get token
	auth = request.headers.get('Authorization')
	try:
		token = auth.split(" ")[1]
		if jwt_utils.decode_token(token) != "quiz-app-admin":
			return '', 401
	except:
		return '', 401
	
	# get json object sent in request body
	body = request.get_json()
	try:
		input_question = Question.from_json(body)
	except json.decoder.JSONDecodeError:
		return '', 415
	except KeyError:
		return '', 415
	except:
		return '', 500
	# create connection
	db_connection = sqlite3.connect("../quiz-db.db")
	db_connection.isolation_level = None

	# add question to database
	try:
		database.addQuestion(db_connection, input_question)
	except:
		# in case of exception, close the connection and return HTTP code 500 (Internal Server Error)
		db_connection.close()
		return '', 500

	db_connection.close()
	return '', 200

@app.route('/questions/<position>', methods=['GET'])
def getQuestion(position):
	db_connection = sqlite3.connect("../quiz-db.db")
	db_connection.isolation_level = None

	# add question to database
	try:
		question = database.getQuestion(db_connection, position)
		result = question.to_json()
	except:
		# in case of exception, close the connection and return HTTP code 500 (Internal Server Error)
		db_connection.close()
		return '', 500

	db_connection.close()
	return result, 200

@app.route('/questions/<position>', methods=['DELETE'])
def deleteQuestion(position):
	# check token
	auth = request.headers.get('Authorization')
	try:
		token = auth.split(" ")[1]
		if jwt_utils.decode_token(token) != "quiz-app-admin":
			return '', 401
	except:
		return '', 401

	db_connection = sqlite3.connect("../quiz-db.db")
	db_connection.isolation_level = None

	# delete question from database
	try:
		question = database.deleteQuestion(db_connection, position)
	except:
		# in case of exception, close the connection and return HTTP code 500 (Internal Server Error)
		db_connection.close()
		return '', 500

	db_connection.close()
	return '', 204

if __name__ == "__main__":
    app.run(ssl_context='adhoc')