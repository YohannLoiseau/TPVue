import base64
from .app import app, db
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from .models import (Question, Questionnaire, QuestionSimple, QuestionMultiple)

@app.cli.command('initdb')
def initdb():
    db.drop_all()
    db.create_all()
    print('Base de données initialisée.')

    # Créer une session pour interagir avec la base de données
    Session = sessionmaker(bind=db.engine, autoflush=True)
    session = Session()

    # create a new questionnaire
    questionnaire = Questionnaire(name="Questionnaire sur les capitales")
    quesionnaire2 = Questionnaire(name="Questionnaire sur les pays")
    session.add(questionnaire)
    session.add(quesionnaire2)

    # create a new simple question
    simple_question = QuestionSimple(title="Quelle est la capitale de la France ?", reponse="Paris", 
                                     choix1="Paris", choix2="Berlin", choix3="Madrid", questionnaire_id=1)
    session.add(simple_question)

    # create a new multiple choice question
    multiple_question = QuestionMultiple(title="Quelle sont les capitales de l'Afrique du Sud ?", 
                                         reponse1 = "Le Cap", reponse2 = "Pretoria", choix1="Le Cap", 
                                         choix2="Paris", choix3="Alger", choix4="Pretoria", questionnaire_id=1)
    session.add(multiple_question)

    # commit the transaction
    session.commit()