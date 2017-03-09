from .. import db 
from ..models import Question, QuestionText

adjectives = [
				#movement
				["fast movement", "schnelle Fortbewegung", "locomotion vite"],
				["slow movement", "langsamme Fortbewegung", "locomotion doucement"],
				["safe mobility", "sichere Mobilitaet", "mobilite assure"],
				["quiet movement", "leise Fortbewegung", "locomotion bas"],
				["noisy movement", "geraeuschvolle Fortbewegung", "locomotion bruyant"],
				["autonomous movement", "Autopilot", "pilote automatique"],
				#engine
				["diesel engine", "Diesel Motor","moteur diesel"],
				["gasoline engine", "Benzin Motor", "moteur benzine"],
				["electric engine", "Elektromotor", "moteur electrique"],
				["hydro engine", "Wasserstoff Motor", "moteur hydrogene"],
				["hybrid engine", "hybrid Motor", "moteur hybride"],
				#type
				["swimming vehicle", "schwimmendes Fahrzeug", "vehicule folttant"],
				["flying vehicle", "fliegendes Fahrzeug", "vehicule volant"],
				["road based vehicle", "Strassenfahrzeug", "vehicule pour la route"],
				#size
				["small vehicle", "kleines Fahrzeug", "petit vehicule"],
				["large vehicle", "grosses Fahrzeug", "grand vehicule"],
				["wide vehicle", "breites Fahrzeug", "vehicule large"],
				["slim vehicle", "duennes Fahrzeug", "vehicule fin"],
				["high vehicle", "hohes Fahrzeug", "vehicule haut"],
				["low vehicle", "niedriges Fahrzeug", "vehicule bas"],
				#transformation
				["convertible", "Cabriolet", "cabriolet"],
				["transformable vehicle", "transformierendes Fahrzeug", "vehicule transformable"],
				#interieur
				["comfortable interieur", "gemuetliche Innenaustattung", "interieur confortable"],
				["sporty interieur", "sportliche Innenaustattung", "interieur sportif"],
				["elegant interieur", "elegante Innenaustattung", "interieur elegant"],
				["expensive interieur", "teure Innenaustattung", "interieur cher"],
				["retro interieur", "Retroinnenaustattung", "interieur retro"],
				["futuristic interieur", "futuristische Innenaustattung", "interieur futuriste"],
				#exterieur
				["protective car body", "behuetende Karosserie", "carrosserie protective"],
				["sporty car body", "sportliche Karosserie", "carrosserie sportif"],
				["elegant car body", "elegante Karosserie", "carrosserie elegant"],
				["edged car body", "kantige Karosserie", "carosserie anguleux"],
				["curved car body", "geschwungene Karosserie", "carosserie arque"],
				["expansive car body", "teure Karosserie", "carrosserie cher"],
				["retro car body", "Retro-Karosserie", "carrosserie retro"],
				["futuristic car body", "futuristische Karosserie", "carrosserie futuriste"],
				["invisible car body", "durchsichtige Karosserie", "carosserie "],
				#transmission
				["manual transmission", "Handschaltung", "changement de vitesse manuel"],
				["automatic transmission", "Automatik Schaltung", "changement de vitesse automatique"],
				#price
				["affordable base configuration", "guenstige Grundaustattung", "equipement de base bon pris"],
				["all-inclusive base configuration", "allumfassende Grundaustattung", "equipement de base universel"],
				["affordable add-ons", "guenstige Erweiterungen", "equipement extension bon pris"],
				["special add-ons", "besondere Erweiterungen", "equipement extension privilegie"],
				#other
				["large storage", "grosser Gepaeckraum", "grandes compartiment a bagages"]
			]

user_results = [

				]

def fill_the_db():
	try:
		print Question.query.first()
	except:
		print("no element in question")

	try:
		print QuestionText.query.first()
	except:
		print("no element in questionText")

	for adjective in adjectives:
		#cotry:
			new_question = Question(owner = "FB")
			db.session.add(new_question)
			db.session.commit()
			new_questionText = QuestionText(questionId = new_question.id,
									language = 'EN',
									text = adjective[0])
			db.session.add(new_questionText)
			db.session.commit()
			new_questionText = QuestionText(questionId = new_question.id,
									language = 'DE',
									text = adjective[1])
			db.session.add(new_questionText)
			db.session.commit()
			new_questionText = QuestionText(questionId = new_question.id,
									language = 'FR',
									text = adjective[2])
			db.session.add(new_questionText)
			db.session.commit()
		#except:
		#	print("failed to save questions to Question DB")