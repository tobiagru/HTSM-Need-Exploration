from .. import db 
from ..models import Question, QuestionText

adjectives = [
				"fast",
				"slow",
				"safe",
				"small",
				"large",
				"diesel",
				"gasoline",
				"quiet",
				"loud",
				"electric",
				"self driving",
				"swimming",
				"hybrid",
				"flying",
				"thick",
				"slim",
				"high",
				"low",
				"cabriolet",
				"comfortable",
				"sporty",
				"expensive",
				"cheap",
				"attractive",
				"manual",
				"automatic",
				"second-hand",
				"new",
				"futuristic",
				"economical"
			]

nouns = [
			"movement",
			"mobility"
		]

def fill_the_db():
	try:
		print Question.query.first()
	except:
		print("no element in question")

	try:
		print QuestionText.query.first()
	except:
		print("no element in questionText")

	for adjective in adjectives:
		for noun in nouns:
			#cotry:
				new_question = Question(owner = "FB")
				db.session.add(new_question)
				db.session.commit()
				new_questionText = QuestionText(questionId = new_question.id
										language = 'EN',
										text = adjective + " " +noun)
				db.session.add(new_questionText)
				db.session.commit()
			#except:
			#	print("failed to save questions to Question DB")