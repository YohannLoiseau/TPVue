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

    Session = sessionmaker(bind=db.engine, autoflush=True)
    session = Session()

    questionnaire = Questionnaire(name="Questionnaire sur les capitales")
    quesionnaire2 = Questionnaire(name="Questionnaire sur les pays")
    session.add(questionnaire)
    session.add(quesionnaire2)

    simple_question = QuestionSimple(title="Quelle est la capitale de la France ?", reponse="Paris", 
                                     choix1="Paris", choix2="Berlin", choix3="Madrid", choix4="Londres", questionnaire_id=1)
    session.add(simple_question)

    multiple_question = QuestionMultiple(title="Quelle sont les capitales de l'Afrique du Sud ?", 
                                         reponse1 = "Le Cap", reponse2 = "Pretoria", choix1="Le Cap", 
                                         choix2="Paris", choix3="Alger", choix4="Pretoria", questionnaire_id=1)
    session.add(multiple_question)
    
    multiple_question2 = QuestionMultiple(title="Quelles sont les couleurs du drapeau de Monaco ?", reponse1 = "Rouge", reponse2 = "Blanc", 
                                     choix1="Rouge", choix2="Bleu", choix3="Vert", choix4="Blanc", questionnaire_id=2)
    session.add(multiple_question2)

    session.commit()