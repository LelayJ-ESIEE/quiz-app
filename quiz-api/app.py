from flask import Flask, request
import json
import jwt_utils
from database import Database
from question import Question

db = Database('../quiz-db.db')

app = Flask(__name__)

def isAuth():
	# get token
	auth = request.headers.get('Authorization')
	try:
		if jwt_utils.decode_token(auth.split(" ")[1]) != "quiz-app-admin":
			return False
		return True
	except:
		return False


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
		return {"token" : jwt_utils.build_token()}, 200
	else :
		# return no token with HTTP code 401 (Unauthorized)
		return '', 401

@app.route('/questions', methods=['POST'])
def addQuestion():

	if not isAuth():
		return 'Vous n\'êtes pas authentifier', 401
	
	# get json object sent in request body
	body = request.get_json()
	try:
		input_question = Question(body['title'], body['text'], body['position'], body['image'], body['possibleAnswers'])
	except json.decoder.JSONDecodeError:
		return 'json.decoder.JSONDecodeError exception', 415
	except KeyError:
		return 'KeyError exception', 415

	# add question to database
	if db.addQuestion(input_question):
		return 'Ajout de la question reussi', 200
	
	return 'Erreur durant l\'ajout de la question', 500


@app.route('/questions/<position>', methods=['GET'])
def getQuestion(position):

	# get question from database
	if db.checkPosition(position) is None:
		return 'La question n\'existe pas', 404

	question = db.getQuestion(position)
	if question:
		result = question.toJson()
		return result, 200
	else:
		return 'Erreur dans la récupération de la question', 500
	
@app.route('/questions/<position>', methods=['DELETE'])
def DelQuestion(position):

	if not isAuth():
		return 'Vous n\'êtes pas authentifier', 401
    
	id = db.checkPosition(position)
	if id is None:
		return 'La question n\'existe pas', 404

	if not db.deleteQuestion(id):
		return 'Erreur lors de la suppression de la question', 500

	return 'Suppression reussi', 204

@app.route('/questions/<position>', methods=['PUT'])
def UpdQuestion(position):

	# get json object sent in request body
	body = request.get_json()
	try:
		input_question = Question(body['title'], body['text'], body['position'], body['image'], body['possibleAnswers'])
	except json.decoder.JSONDecodeError:
		return 'json.decoder.JSONDecodeError exception', 415
	except KeyError:
		return 'KeyError exception', 415

	if not isAuth():
		return 'Vous n\'êtes pas authentifier', 401
    
	id = db.checkPosition(position)
	if id is None:
		return 'La question n\'existe pas', 404

	if not db.updateQuestion(input_question, id):
		return 'Erreur lors de la modification de la question', 500

	return 'Modification reussi', 200

if __name__ == "__main__":
    app.run()