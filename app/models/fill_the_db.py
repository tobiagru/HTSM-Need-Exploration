from .. import db 
from .. import models

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
			"vehicle"
			"mobility"
		]

def fill_the_db():
	for adjective in adjectives:
		for noun in nouns:
			#cotry:
				new_question = models.Question(owner = "FB")
				db.session.add(new_question)
				db.session.commit()
				new_questionText = models.QuestionText(questionId = new_question,
										language = "EN",
										text = adjective + " " +noun)
				db.session.add(new_questionText)
				db.session.commit()
			#except:
			#	print("failed to save questions to Question DB")