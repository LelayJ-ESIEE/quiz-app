from db_helper import DBHelper, NonExistingObjectError
from flask import Flask, request
from question import Question
import json
import jwt_utils

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
		return 'Unauthorized', 401

###
# Questions Management
###

@app.route('/questions', methods=['POST'])
def addQuestion():
	# check token
	auth = request.headers.get('Authorization')
	try:
		token = auth.split(" ")[1]
		if jwt_utils.decode_token(token) != "quiz-app-admin":
			return 'Unauthorized', 401
	except:
		return 'Unauthorized', 401
	
	# get question sent in request body
	body = request.get_json()
	try:
		input_question = Question.from_json(body)
	except json.decoder.JSONDecodeError:
		return 'Unsupported Media Type: unparseable body', 415
	except KeyError:
		return 'Unsupported Media Type: wrong or missing arguments in the body', 415
	except Exception as e:
		print(e)
		return 'Internal Server Error', 500
	# create connection
	dbHelper = DBHelper()

	# add question to database
	try:
		dbHelper.addQuestion(input_question)
	except Exception as e:
		# in case of exception, close the connection and return HTTP code 500 (Internal Server Error)
		dbHelper.close()
		print(e)
		return 'Internal Server Error', 500

	dbHelper.close()
	return '', 200

@app.route('/questions/<position>', methods=['GET'])
def getQuestion(position):
	# get question from database
	try:
		dbHelper = DBHelper()
		question = dbHelper.getQuestion(position)
		result = question.to_json()
	except NonExistingObjectError:
		# in case of TypeError (= no row returned) close the connection and return HTTP code 404 (Not Found)
		dbHelper.close()
		return '', 404
	except Exception as e:
		# in case of exception, close the connection and return HTTP code 500 (Internal Server Error)
		dbHelper.close()
		print(e)
		return 'Internal Server Error', 500

	dbHelper.close()
	return result, 200

@app.route('/questions/<position>', methods=['DELETE'])
def deleteQuestion(position):
	# check token
	auth = request.headers.get('Authorization')
	try:
		token = auth.split(" ")[1]
		if jwt_utils.decode_token(token) != "quiz-app-admin":
			return 'Unauthorized', 401
	except:
		return 'Unauthorized', 401

	dbHelper = DBHelper()

	# delete question from database
	try:
		dbHelper.deleteQuestion(position)
	except NonExistingObjectError:
		# in case of TypeError (= no row returned) close the connection and return HTTP code 404 (Not Found)
		dbHelper.close()
		return '', 404
	except Exception as e:
		# in case of exception, close the connection and return HTTP code 500 (Internal Server Error)
		dbHelper.close()
		print(e)
		return 'Internal Server Error', 500

	dbHelper.close()
	return '', 204

@app.route('/questions/<position>', methods=['PUT'])
def updateQuestion(position):
	# check token
	auth = request.headers.get('Authorization')
	try:
		token = auth.split(" ")[1]
		if jwt_utils.decode_token(token) != "quiz-app-admin":
			return 'Unauthorized', 401
	except:
		return 'Unauthorized', 401

	# get question sent in request body
	body = request.get_json()
	try:
		input_question = Question.from_json(body)
	except json.decoder.JSONDecodeError:
		return '', 415
	except KeyError:
		return '', 415
	except Exception as e:
		print(e)
		return 'Internal Server Error', 500

	dbHelper = DBHelper()

	# delete question from database
	try:
		dbHelper.updateQuestion(position, input_question)
	except NonExistingObjectError:
		# in case of TypeError (= no row returned) close the connection and return HTTP code 404 (Not Found)
		dbHelper.close()
		return '', 404
	except Exception as e:
		# in case of exception, close the connection and return HTTP code 500 (Internal Server Error)
		dbHelper.close()
		print(e)
		return 'Internal Server Error', 500

	dbHelper.close()
	return '', 200

###
# Participation Management
###

@app.route('/participations', methods=['POST'])
def addParticipation():
	# add participation sent in request body
	return 'Not Implemented Yet', 405

@app.route('/participations', methods=['DELETE'])
def deleteParticipations():
	return 'Not Implemented Yet', 405

if __name__ == "__main__":
	app.run(ssl_context='adhoc')