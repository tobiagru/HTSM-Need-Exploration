#import core
import random
import json

#import public
from sqlalchemy.sql.expression import func
from flask import jsonify

#import privat
from .. import db
from ..models import Question, Answer, AnswerMeta, QuestionText

fail_questions = json.dumps({"questions":[
							[{"questionId": "1", "questionText": "1"},
								{"questionId": "2", "questionText": "2"}],
							[{"questionId": "3", "questionText": "3"},
								{"questionId": "4", "questionText": "4"}],
							[{"questionId": "5", "questionText": "5"},
								{"questionId": "6", "questionText": "6"}],
							[{"questionId": "7", "questionText": "7"},
								{"questionId": "8", "questionText": "8"}],
							[{"questionId": "9", "questionText": "9"},
								{"questionId": "10", "questionText": "10"}],
							[{"questionId": "11", "questionText": "11"},
								{"questionId": "12", "questionText": "12"}],
							[{"questionId": "13", "questionText": "13"},
								{"questionId": "14", "questionText": "14"}],
							[{"questionId": "15", "questionText": "15"},
								{"questionId": "16", "questionText": "16"}],
							[{"questionId": "17", "questionText": "17"},
								{"questionId": "18", "questionText": "18"}],
							[{"questionId": "19", "questionText": "19"},
								{"questionId": "20", "questionText": "20"}],
							]})


# build a json object with 10 questions where every
# questions has questionsID, option1 and option2
def build_questions(language='EN', owner=None):
	try:
		#query 20 random questions
		questionList = QuestionText.query\
						.filter(QuestionText.language == language)\
						.order_by(func.rand())\
						.limit(10)\
						.all()

		questionList2 = QuestionText.query\
						.filter(QuestionText.language == language)\
						.order_by(func.rand())\
						.limit(10)\
						.all()
	except:
		print("Failed to load 20 questions from the database")
		return fail_questions

	try:
		questions = {"questions":
						[
							[
								{"questionId": question.questionId,
									"questionText": question.text},
								{"questionId": question2.questionId,
									"questionText": question2.text}
							] for question, question2 in zip(questionList, questionList2)
						]
					}
	except:
		print("Failed to turn list of 20 questions into 10 tuples of 2 questions")
		return fail_questions

	try:
		return json.dumps(questions)
	except:
		print("failed to convert dict of questions to json")
		return fail_questions


def getusertype():
	return str(random.randint(1, 20))


def save_answers(answers, owner=None):
	for answer in answers["answers"]:
		#create new answer
		try:
			if answer["answer"]["answerValue"] in ["true", "True", "TRUE", "1"]:
				ansValue = True
			else:
				ansValue = False

			new_answer = Answer(
						questionId=int(answer["answer"]["questionId"]),
                    	altQuestionId=int(answer["answer"]["altQuestionId"]),
						answerValue=ansValue,
						source=owner
					)
			print("created answer")
		except:
			print("not able to build answer")
			continue

		try:
			#save answer to db
			db.session.add(new_answer)
			db.session.commit()
			print("commited answer")
			
		except:
			print("Failed to save answer in db for questionID {0}".format(answer["answer"]["questionId"]))
			continue
		
		try:
			assert len(answers["metadata"]) >= 1
		except AssertionError:
			print("no meta Data")
			continue

		for meta in answers["metadata"]:
			#create new meta data
			try:
				new_metadata = AnswerMeta(
						answerId=new_answer.id,
						key=meta["key"],
						value=meta["value"]
					)
				print("created meta")
			except:
				print("not able to build metadata")
				continue

			try:
				#save metadata
				db.session.add(new_metadata)
				db.session.commit()
				#save metadata
				print("commited meta")
			except:
				print("Failed to save metadata in dbfor questionID {0}".format(answer["questionId"]))
				continue
