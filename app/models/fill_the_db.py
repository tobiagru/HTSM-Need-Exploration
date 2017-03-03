from .. import db

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

for adjective in adjectives:
	for noun in nouns:
		question_tmp = Questions.insert().values(owner = "FB")
		Questions.insert().values(questionId = questions_tmp.id,
									language = "EN",
									text = adjective + " " +noun)