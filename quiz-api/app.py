from flask import Flask, request
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

###
# Participation Management
###

if __name__ == "__main__":
	app.run(ssl_context='adhoc')