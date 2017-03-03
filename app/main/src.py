#import core
import random
import json

#import public

#import privat
from .. import db

#build a json object with 10 questions where every
# questions has questionsID, option1 and option2
def build_questions(language="EN", owner=None):

	#query 20 random questions
	questionList = db.Question.query\
						.join(db.QuestionText)\
						.filter(QuestionText.language == language)\
						.order_by(rand())\
						.limit(10)\
						.all()

	questionList2 = db.Question.query\
						.join(db.QuestionText)\
						.filter(QuestionText.language == language)\
						.order_by(rand())\
						.limit(10)\
						.all()
	
	questions = {}

	questions[questions] = [
								[
									{"questionId":question.questionId,
										 "questionText":question.questionText},
									{"questionId":question2.questionId,
										 "questionText":question2.questionText}
								]for zip(questionList, questionList2)
							]

	for question in questions:
		questions['questions']['questionId'] = question.questionsID
		questions['questions']['questionText'] = question.QuestionText.text

	# Session.query.offset(
    #    	func.floor(
    #        	func.random() *
    #         	db.session.query(func.count(model_name.id))
    #     	)
    # 	).limit(20).all()



def getusertype():
	random.randint(1,20)

def save_answers(answers, owner=None):
	parsed_answer = json.loads(answer)

	#Answer.bulk_insert_mappings(
	#	[{'questionId' = parsed_answer[answer][questionId],
	#		'altQuestionId' = parsed_answer[answer][altQuestionId],
	#		'answerValue' = parsed_answer[answer][answerValue],
	#		'source' = owner
	#		} for 
	#Answer.commit()

	for answer in parsed_answer[answers]:
		#save answer
		answer_tmp = Answer.insert().values(
			questionId = parsed_answer[answer][questionId],
			altQuestionId = parsed_answer[answer][altQuestionId],
			answerValue = parsed_answer[answer][answerValue],
			source = owner
		)
		#save metadata
		for metaKey in parsed_answer[metadata]:
			AnswerMeta.insert().values(
				answerId = answer_tmp.id,
				key = metaKey,
				value = parsed_answer[metadata][metaKey]
