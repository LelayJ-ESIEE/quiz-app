import sqlite3
from unittest import result
from question import Question

class Database():
    def __init__(self, db_connection: str):
        self.db_connection = db_connection


    def addQuestion(self, input_question:Question):
        try:
            self.reordering(input_question.position)
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

            position = cur.execute(
                f"select position from question where id = ?",
                (id,))
            position = position.fetchone()

            cur.execute(
                f"delete from question where id = ?",
                (id,))

            cur.execute(
                f"delete from answer where question_id = ?",
                (id,))

            cur.execute("commit")
            db.close()
            self.reordering(position['position'], True)
            return True
            
        except sqlite3.Error as err:
            cur.execute('rollback')
            db.close()
            return False

    def updateQuestion(self, question:Question, id:int):
        if not self.deleteQuestion(id):
            return False
        if not self.addQuestion(question):
            return False
        return True

    def reordering(self, position:int, isDelete:bool = False):
        try:
            db = sqlite3.connect(self.db_connection)
            db.isolation_level = None
            db.row_factory = sqlite3.Row
            cur = db.cursor()
            cur.execute("begin")

            if isDelete:
                cur.execute(
                    "update question set position = position - 1 where position >= ?",
                    (position,))
            else:
                cur.execute(
                    "update question set position = position + 1 where position >= ?",
                    (position,))
            cur.execute("commit")
            db.close()
            return

        except sqlite3.Error:
            cur.execute('rollback')
            db.close()
            return



