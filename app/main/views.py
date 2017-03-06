#import core

#import public
from flask import render_template, request, Flask, redirect, url_for

#import privat
from . import main
import src

#Session

@main.route('/')
def index():
     return redirect(url_for('static', filename = "index.html"))

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
@main.route('/postanswer', methods=['POST'])
def postanswer():
	return "test"
	# src.save_answers(request.get_json())
	# return src.getusertype()

#return: ...
@main.route('/analytics')
def analytics():
	pass
