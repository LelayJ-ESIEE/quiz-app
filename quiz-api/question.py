from email.mime import image
import json
from turtle import position

class Question():
    def __init__(self, title: str, text: str, position: int, image: str, possibleAnswers: list):
        self.title = title
        self.text = text
        self.position = position
        self.image = image
        self.possibleAnswers = possibleAnswers
        for answer in self.possibleAnswers:
            answer['isCorrect'] = True if answer['isCorrect'] == 1 else False

    @staticmethod
    def toPython(jsonString):
        dico = json.loads(jsonString)
        return Question(dico['title'], dico['text'], dico['position'], dico['image'], dico['possibleAnswers'])

    def toJson(self):
        return json.dumps({
            "title": self.title,
            "text": self.text,
            "image": self.image,
            "position": self.position,
            "possibleAnswers": self.possibleAnswers
        })
