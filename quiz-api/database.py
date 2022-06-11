import sqlite3
from unittest import result
from question import Question

class Database():
    def __init__(self, db_connection: str):
        self.db_connection = db_connection


    def addQuestion(self, input_question:Question):
        try:
            db = sqlite3.connect(self.db_connection)
            db.isolation_level = None

            cur = db.cursor()
            cur.execute("begin")

            insertion_result = cur.execute(
                f"insert into question (title, text, position, image) values (?, ?, ?, ?)",
                (input_question.title, input_question.text,  input_question.position, input_question.image))

            id = insertion_result.lastrowid
            
            for answers in input_question.possibleAnswers: 
                insertion_result = cur.execute(
                    f"insert into answer (text, isCorrect, question_id) values (?, ?, ?)",
                    (answers['text'], answers['isCorrect'], id))
            
            cur.execute("commit")
            db.close()
            return True
            
        except sqlite3.Error as err:
            cur.execute('rollback')
            db.close()
            return False
    
    def getQuestion(self, position:int):
        try:
            db = sqlite3.connect(self.db_connection)
            db.isolation_level = None
            db.row_factory = sqlite3.Row

            cur = db.cursor()
            cur.execute("begin")

            result = cur.execute(
                f"select * from question where position = ?",
                (position,))
            
            question = result.fetchone()

            result = cur.execute(
                f"select * from answer where question_id = ?",
                (question['id'],))

            answers_result = result.fetchall()
            possibleAnswers = []
            for answers in answers_result:
                answer_dict = dict(answers)
                possibleAnswers.append(answer_dict)

            db.close()
            return Question(question['title'], question['text'], question['position'], question['image'], possibleAnswers)
            
        except sqlite3.Error as err:
            db.close()
            return False
    
    def checkPosition(self, position:int):
        try:
            db = sqlite3.connect(self.db_connection)
            db.isolation_level = None
            db.row_factory = sqlite3.Row

            cur = db.cursor()
            cur.execute("begin")

            result = cur.execute(
                f"select * from question where position = ?",
                (position,))
            
            result = result.fetchone()
            db.close()
            
            if result is None:
                return None
            return result['id']
        
        except sqlite3.Error as err:
            db.close()
            return False
    
    def deleteQuestion(self, id:int):
        try:
            db = sqlite3.connect(self.db_connection)
            db.isolation_level = None
            db.row_factory = sqlite3.Row

            cur = db.cursor()
            cur.execute("begin")

            result = cur.execute(
                f"delete from question where id = ?",
                (id,))
            
            question = result.fetchone()

            result = cur.execute(
                f"delete from answer where question_id = ?",
                (id,))

            cur.execute("commit")
            db.close()
            return True
            
        except sqlite3.Error as err:
            cur.execute('rollback')
            db.close()
            return False

    def updateQuestion(self, question:Question, id:int):
        try:
            db = sqlite3.connect(self.db_connection)
            db.isolation_level = None
            db.row_factory = sqlite3.Row
            cur = db.cursor()
            cur.execute("begin")

            cur.execute(
                "update question set title = ?, text = ?, image = ?, position = ? WHERE id = ?",
                (question.title, question.text, question.image, question.position, id)
            )

            cur.execute(
                "delete from answer where question_id = ?",
                (id,)
            )

            for answer in question.possibleAnswers:
                cur.execute(
                    "insert into answer (question_id, text, isCorrect) values (?, ?, ?)",
                    (id, answer['text'],  answer['isCorrect'])
                )

            cur.execute("commit")
            db.close()
            return True

        except sqlite3.Error as err:
            cur.execute('rollback')
            db.close()
            return False



