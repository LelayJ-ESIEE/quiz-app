from question import Question
import sqlite3

class NonExistingObjectError(Exception):
	"""
	Exception raised for errors while attempting to access database objects that do not exist
	"""
	def __init__(self, message="Attempting to access non existing object in database"):
		self.message = message
		super().__init__(self.message)

class DBHelper:
	###
	# Helper Management
	###

	def __init__(self):
		db_connection = None
		try:
			db_connection = sqlite3.connect("../quiz-db.db")
			db_connection.isolation_level = None
		except Exception as e:
			print(e)
			raise
		self.db_connection = db_connection
	
	def close(self):
		self.db_connection.close()

	###
	# Questions Management
	###

	def getQuestionId(self, position):
		"""
		Gets the requested question ID in the connected database
		Args:
			position: position of the question to get the ID from the database
		"""
		try:
			# initialize cursor
			cursor = self.db_connection.cursor()
			# get question id
			cursor.execute(f"""SELECT id FROM question WHERE position = {position}""")
			questionId = cursor.fetchone()
			if questionId is None:
				raise NonExistingObjectError()
			return questionId[0]
		except:
			raise

	def getQuestionsCount(self):
		try:
			# initialize cursor
			cursor = self.db_connection.cursor()
			cursor.execute(f"""SELECT id FROM question""")
			questions_ids = cursor.fetchall()
			if questions_ids is None:
				return 0
			return len(questions_ids)
		except Exception as e:
			print(e)
			return 0

	def increase_questions_position_from(self, position):
		cursor = self.db_connection.cursor()
		try :
			cursor.execute("BEGIN")
			cursor.execute(f"UPDATE question SET position=position+1 WHERE position>="+str(position))
			cursor.execute("COMMIT")
		except Exception as e:
			print(e)
			cursor.execute('ROLLBACK')

	def addQuestion(self, input_question: Question):
		"""
		Adds the requested question and its answers to the connected database
		Args:
			input_question: question to add to the database
		"""
		# Add question to database
		try:
			max_position = self.getQuestionsCount() + 1
			if input_question.position > max_position:
				input_question.position = max_position
			# initialize cursor
			cursor = self.db_connection.cursor()
			# shift questions position if necessary
			if(max_position > 0):
				self.increase_questions_position_from(input_question.position)
			# start transaction
			cursor.execute("BEGIN")
			# save the question to db
			insertion_result = cursor.execute(
				f"INSERT INTO question (title, text, position, image) VALUES"
				f"""("{input_question.title}","{input_question.text}",{input_question.position},"{input_question.image}")""")
			# send the request
			cursor.execute("COMMIT")
		except:
			# in case of exception, rollback the transaction and raise
			cursor.execute("ROLLBACK")
			raise
		# Add answers to database
		try:
			# initialize cursor
			cursor = self.db_connection.cursor()
			# start transaction
			cursor.execute("BEGIN")
			# get question id
			questionId = self.getQuestionId(input_question.position)
			# save the answers to db
			for answer in input_question.possibleAnswers:
				insertion_result = cursor.execute(
					f"INSERT INTO answer (text, is_correct, question_id) VALUES"
					f"""("{answer["text"]}",{answer["isCorrect"]},{questionId})""")
			# send the request
			cursor.execute("COMMIT")
		except:
			# in case of exception, rollback the transaction and raise
			cursor.execute("ROLLBACK")
			raise

	###
	# Participation Management
	###
