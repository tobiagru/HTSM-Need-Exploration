#import core

#import public
from flask import render_template, request

#import privat
from . import main
import src

#Session

@main.route('/')
def index():
     return redirect(url_for('static'))

#returns: questions
@main.route('/getquestion', methods=['GET', 'POST'])
def getquestion():
	if request.method == 'POST':
		return src.build_questions(
			language = request.form['language']
		)
	if request.method == 'GET':
		return src.build_questions()

'''
#returns: questions
@main.route('/getquestion/<owner>', methods=['GET', 'POST'])
def getquestion():
	if request.method == 'POST':
		return build_questions(
			language = request.form['language'],
			owner = owner
		)
	if request.method == 'GET':
		return build_questions(
			language = "EN",
			owner = owner)
'''

#recieve: answers, asnwer_meta
#return: usertype
@main.route('/postanswer', methods=['GET', 'POST'])
def postanswer():
	if request.method == 'POST':
		src.save_answers(request.form['answers'])
		return src.getusertype()

'''
#recieve: answers, asnwer_meta
#return: usertype
@main.route('/postanswer/<owner>', methods=['GET', 'POST'])
def postanswer():
	if request.method == 'POST':
		save_answers(request.form['answers'], owner)
		return getusertype()
'''

#return: ...
@main.route('/analytics')
def analytics():
	pass
