#import core
import random
import json

#import public

#import privat
from .. import models

#build a json object with 10 questions where every
# questions has questionsID, option1 and option2
def build_questions(language="EN", owner=None):

	#query 20 random questions
	Session.query.offset(
       	func.floor(
           	func.random() *
            	db.session.query(func.count(model_name.id))
        	)
    	).limit(20).all()

def getusertype():
	random.randint(1,20)

def save_answers(answers, owner=None):
	parsed_answer = json.loads(answer)
	for answer in parsed_answer[answers]:
		#save answer
		answer_tmp = answers.insert().values(
			questionId = parsed_answer[answer][questionId],
			answer = parsed_answer[answers][answer],
			altQuestionId = parsed_answer[answers][altAnswerId],
			source = owner
		)
		#save metadata
		answer_meta.insert().values(
			answerId = answer_tmp.
			parsed_answer[metadata][language]
			#parsed_answer[metadata][country]


