#import core
import random
import json

#import public
from sqlalchemy.sql.expression import func

#import privat
from .. import db
from ..models import Question, Answer, AnswerMeta, QuestionText

fail_questions = json.dumps({"questions":[
							[{"questionId": "1","questionText":"1"},
								{"questionId": "2","questionText":"2"}],
							[{"questionId": "3","questionText":"3"},
								{"questionId": "4","questionText":"4"}],
							[{"questionId": "5","questionText":"5"},
								{"questionId": "6","questionText":"6"}],
							[{"questionId": "7","questionText":"7"},
								{"questionId": "8","questionText":"8"}],
							[{"questionId": "9","questionText":"9"},
								{"questionId": "10","questionText":"10"}],
							[{"questionId": "11","questionText":"11"},
								{"questionId": "12","questionText":"12"}],
							[{"questionId": "13","questionText":"13"},
								{"questionId": "14","questionText":"14"}],
							[{"questionId": "15","questionText":"15"},
								{"questionId": "16","questionText":"16"}],
							[{"questionId": "17","questionText":"17"},
								{"questionId": "18","questionText":"18"}],
							[{"questionId": "19","questionText":"19"},
								{"questionId": "20","questionText":"20"}],
							]})

#build a json object with 10 questions where every
# questions has questionsID, option1 and option2
def build_questions(language='EN', owner=None):
	db.session
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
		questions = {"questions": [ 
					[ 
						{"questionId":question.questionId,
							 "questionText":question.text},
						{"questionId":question2.questionId,
							 "questionText":question2.text}
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

	# Session.query.offset(
    #    	func.floor(
    #        	func.random() *
    #         	db.session.query(func.count(model_name.id))
    #     	)
    # 	).limit(20).all()


def getusertype():
	random.randint(1,20)

def save_answers(answers, owner=None):
	try:
		parsed_answer = json.loads(answer)
	except:
		print("failed to parse answer json")
		return None

	#Answer.bulk_insert_mappings(
	#	[{'questionId' = parsed_answer[answer][questionId],
	#		'altQuestionId' = parsed_answer[answer][altQuestionId],
	#		'answerValue' = parsed_answer[answer][answerValue],
	#		'source' = owner
	#		} for 
	#Answer.commit()

	for answer in parsed_answer[answers]:
		#create new answer
		try:
			new_answer = Answer(
						questionId = parsed_answer[answer][questionId],
						altQuestionId = parsed_answer[answer][altQuestionId],
						answerValue = parsed_answer[answer][answerValue],
						source = owner
					)
		except:
			print("not able to build answer")
			continue

		try:
			#save answer to db
			db.session.add(new_answer)
			db.session.commit()
			
		except:
			print("Failed to save answer in db for questionID {0}".format(parsed_answer[answer][questionId]))
			continue
		
		try:
			assert len(parsed_answer[metadata]) >= 1
		except AssertionError:
			print("no meta Data")
			continue


		for metaKey in parsed_answer[metadata]:
			#create new meta data
			try:
				new_metadata = AnswerMeta(
						answerId = new_answer.id,
						key = metaKey,
						value = parsed_answer[metadata][metaKey]
					)
			except:
				print("not able to build metadata")
				continue

			try:
				#save metadata
				db.add(new_metadata)
				db.commit()
				#save metadata
			except:
				print("Failed to save metadata in dbfor questionID {0}".format(parsed_answer[answer][questionId]))
				continue
		