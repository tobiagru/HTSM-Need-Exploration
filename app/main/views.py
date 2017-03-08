#import core

#import public
from flask import render_template, request, Flask, redirect, url_for

#import privat
from . import main
import src

#Session

@main.route('/')
def index():
     return render_template('main/quizapp.html')

#returns: questions
@main.route('/getquestion', methods=['GET', 'POST'])
def getquestion():
	if request.method == 'POST':
		return src.build_questions(
			language = request.get_json()['language']
		)
	if request.method == 'GET':
		return src.build_questions()

#recieve: answers, asnwer_meta
#return: usertype
@main.route('/postanswer', methods=['GET', 'POST'])
def postanswer():
#	try:
#		print(request.form.keys()[0])
#		print("version form.keys")
#	except:
#		pass

	print(request.get_json(force=True))
	#src.save_answers(request.get_json(force=True))
	return src.getusertype()

#	if request.is_json:
#	 	src.save_answers(request.get_json(force=True))
#	 	return src.getusertype()
#	else:
#		try:
#			src.save_answers(json.loads(request.get_data()))
#		except:
#			print("cannot handle this type of data")
#			print(request.get_data()) 
#	 	return src.getusertype()


#return: ...
@main.route('/analytics')
def analytics():
	return 200
