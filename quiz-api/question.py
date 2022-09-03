import json

class Question:
	def __init__(self, title: str, text: str, image: str, position: int, possibleAnswers: list):
		"""
		Initializes a new instance of Question
		>>> out = Question("Test Question", "Test", "falseb64imagecontent", 0, [])
		>>> print(out.title)
		Test Question
		>>> print(out.text)
		Test
		>>> print(out.image)
		falseb64imagecontent
		>>> print(out.position)
		0
		>>> print(out.possibleAnswers)
		[]
		"""
		self.title = title
		self.text = text
		self.image = image
		self.position = position
		self.possibleAnswers = possibleAnswers

	def to_json(self) -> json:
		"""
		Converts a question into a json string
		Returns:
			json: a JSON string containing the question informations
		>>> question = Question("Test Question", "Test", "falseb64imagecontent", 0, [])
		>>> out = question.to_json()
		>>> print(out)
		{"title": "Test Question", "text": "Test", "image": "falseb64imagecontent", "position": 0, "possibleAnswers": []}
		"""
		return json.dumps({"title": self.title, "text": self.text, "image": self.image, "position": self.position, "possibleAnswers": self.possibleAnswers})
	
	def from_json(input: json):
		"""
		Converts a json into a question
		Args:
			input (json): JSON string containing question informations to parse
		Returns:
			from_json(input): the parsed Question
		>>> jsonStr = {"title": "Test Question", "text": "Test", "image": "falseb64imagecontent", "position": 0, "possibleAnswers": []}
		>>> out = Question.from_json(jsonStr)
		>>> print(out.title)
		Test Question
		>>> print(out.text)
		Test
		>>> print(out.image)
		falseb64imagecontent
		>>> print(out.position)
		0
		>>> print(out.possibleAnswers)
		[]
		>>> out = Question.from_json({})
		Traceback (most recent call last):
		...
		KeyError: 'title'
		>>> out = Question.from_json({"test": "wrong"})
		Traceback (most recent call last):
		...
		KeyError: 'title'
		"""
		return Question(input["title"], input["text"], input["image"], input["position"], input["possibleAnswers"])