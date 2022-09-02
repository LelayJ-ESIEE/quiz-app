import sqlite3

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

	###
	# Participation Management
	###
