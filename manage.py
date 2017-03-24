#!/usr/bin/env python
import os
import subprocess
from config import Config

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from redis import Redis
from rq import Connection, Queue, Worker

from app import create_app, db
from app.models import Role, User, fill_the_db, Question, QuestionText, Answer, AnswerMeta, Result

from app.main.src import build_questions

from sqlalchemy.sql.expression import func, case, literal_column
import json

if os.path.exists('config.env'):
    print('Importing environment from .env file')
    for line in open('config.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def fill_db():
    fill_the_db.fill_the_db()


@manager.command
def test_questions():
    questionList = QuestionText.query\
                        .filter(QuestionText.language == 'EN')\
                        .order_by(func.rand())\
                        .limit(10)\
                        .all()
    questionList2 = QuestionText.query\
                    .filter(QuestionText.language == 'EN')\
                    .order_by(func.rand())\
                    .limit(10)\
                    .all()

    questions_tmp = []
    for question, question2 in zip(questionList, questionList2):
        print(question.__dict__)
        print(question2.__dict__)
        question_tpl = [{"questionId": question.questionId,
                         "questionText": question.text},
                        {"questionId": question2.questionId,
                         "questionText": question2.text}]
        questions_tmp.extend(question_tpl)

    questions = {"questions": questions_tmp}

    print(json.dumps(questions))


@manager.command
def test_answers():
    print(Answer.query.order_by(Answer.id.desc()).first())
    print(Answer.query.count())
    print(AnswerMeta.query.order_by(AnswerMeta.id.desc()).first())

@manager.command
def test_results():
    print("number of different results {0}".format(Result.query.count()))

@manager.command
def test_POST_request():
    owner = None
    answers = {"answers":
                    [
                        {"answer":
                            {"questionId":38,
                             "answerValue": "True",
                             "altQuestionId":34}
                         },
                         {"answer":
                            {"questionId":34,
                             "answerValue": "false",
                             "altQuestionId":38}
                         }
                    ],
                "metadata":
                    [
                        {"key":"lang",
                         "value":"DE"},
                        {"key":"country",
                         "value":"Switzerland"}
                    ]
               }

    for answer in answers["answers"]:
        #create new answer
        if answer["answer"]["answerValue"] in ["true", "True", "TRUE", "1", 1]:
                ansValue = True
        else:
            ansValue = False

        new_answer = Answer(
                    questionId=int(answer["answer"]["questionId"]),
                    altQuestionId=int(answer["answer"]["altQuestionId"]),
                    answerValue=answer["answer"]["answerValue"],
                    source=owner
                )
        print("created answer")

        #save answer to db
        db.session.add(new_answer)
        db.session.commit()
        print("commited answer")

        for meta in answers["metadata"]:
            #create new meta data
            
            new_metadata = AnswerMeta(
                    answerId=new_answer.id,
                    key=meta["key"],
                    value=meta["value"]
                )
            print("created meta")

            #save metadata
            db.session.add(new_metadata)
            db.session.commit()
            #save metadata
            print("commited meta")

@manager.command
def analytics():
    numAns = func.count(Answer.questionId)
    trueAns = func.count(case([((Answer.answerValue == True),Answer.questionId)],else_=literal_column("NULL")))
    numMaleAns = func.count(case([((AnswerMeta.value == "male"),Answer.questionId)],else_=literal_column("NULL")))
    trueMaleAns = func.count(case([((Answer.answerValue == True) & (AnswerMeta.value == "male"),Answer.questionId)],else_=literal_column("NULL")))
    numFemaleAns = func.count(case([((AnswerMeta.value == "female"),Answer.questionId)],else_=literal_column("NULL")))
    trueFemaleAns = func.count(case([((Answer.answerValue == True) & (AnswerMeta.value == "female"),Answer.questionId)],else_=literal_column("NULL")))

    #(Answer.questionId, QuestionText.text, numAns, trueAns)
    #                 
    #                 
    #                 
    # an                

    analytics_data = db.session.query(Answer.questionId.label("questionID"),
                                      QuestionText.text.label("questionText"),
                                      numAns.label("numAns"),
                                      trueAns.label("trueAns"),
                                      numMaleAns.label("numMaleAns"),
                                      trueMaleAns.label("trueMaleAns"),
                                      numFemaleAns.label("numFemaleAns"),
                                      trueFemaleAns.label("trueFemaleAns"))\
                     .join(Answer.questionId)
                     .join(Question.id)\
                     .join(QuestionText.questionId)\
                     .join(Answer.id)
                     .join(AnswerMeta.answerId)\
                     .filter_by(QuestionText.language == "EN")\
                     .group_by(Answer.questionId)\
                     .first()
                     
    print(json.dumps(analytics_data))

@manager.option(
    '-n',
    '--number-users',
    default=10,
    type=int,
    help='Number of each model type to create',
    dest='number_users')
def add_fake_data(number_users):
    """
    Adds fake data to the database.
    """
    User.generate_fake(count=number_users)


@manager.command
def setup_dev():
    """Runs the set-up needed for local development."""
    setup_general()


@manager.command
def setup_prod():
    """Runs the set-up needed for production."""
    setup_general()


def setup_general():
    """Runs the set-up needed for both local development and production.
       Also sets up first admin user."""
    Role.insert_roles()
    admin_query = Role.query.filter_by(name='Administrator')
    if admin_query.first() is not None:
        if User.query.filter_by(email=Config.ADMIN_EMAIL).first() is None:
            user = User(
                first_name='Admin',
                last_name='Account',
                password=Config.ADMIN_PASSWORD,
                confirmed=True,
                email=Config.ADMIN_EMAIL)
            db.session.add(user)
            db.session.commit()
            print('Added administrator {}'.format(user.full_name()))


@manager.command
def run_worker():
    """Initializes a slim rq task queue."""
    listen = ['default']
    conn = Redis(
        host=app.config['RQ_DEFAULT_HOST'],
        port=app.config['RQ_DEFAULT_PORT'],
        db=0,
        password=app.config['RQ_DEFAULT_PASSWORD'])

    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()


@manager.command
def format():
    """Runs the yapf and isort formatters over the project."""
    isort = 'isort -rc *.py app/'
    yapf = 'yapf -r -i *.py app/'

    print('Running {}'.format(isort))
    subprocess.call(isort, shell=True)

    print('Running {}'.format(yapf))
    subprocess.call(yapf, shell=True)


if __name__ == '__main__':
    manager.run()
