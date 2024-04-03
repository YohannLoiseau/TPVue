from sqlalchemy import *
from .app import db

class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Questionnaire (%d) %s>' % (self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'questions': [question.to_json() for question in self.questions]
        }

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), nullable=False)
    question_type = db.Column(db.String(120))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship('Questionnaire', backref=db.backref("questions", lazy="dynamic"))

    __mapper_args__ = {
        'polymorphic_identity': 'question',
        'polymorphic_on': question_type
    }

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'question_type': self.question_type,
            'questionnaire_id': self.questionnaire_id
        }

class QuestionSimple(Question):
    __tablename__ = 'questionsimple'
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    reponse = db.Column(db.String(120))
    choix1 = db.Column(db.String(120))
    choix2 = db.Column(db.String(120))
    choix3 = db.Column(db.String(120))
    choix4 = db.Column(db.String(120))

    __mapper_args__ = {
        'polymorphic_identity': 'simple',
    }

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'question_type': self.question_type,
            'reponse': self.reponse,
            'choix1': self.choix1,
            'choix2': self.choix2,
            'choix3': self.choix3,
            'choix4': self.choix4
        }
    
    def add_question(title, question_type, reponse, choix1, choix2, choix3, choix4, questionnaire_id):
        if question_type != 'simple':
            raise ValueError('Invalid question type')
        question = QuestionSimple(title=title, question_type=question_type, reponse=reponse, 
                                  choix1=choix1, choix2=choix2, choix3=choix3, choix4=choix4, questionnaire_id=questionnaire_id)
        db.session.add(question)
        db.session.commit()
        return question

class QuestionMultiple(Question):
    __tablename__ = 'questionmultiple'
    id = db.Column(db.Integer, db.ForeignKey('question.id'), primary_key=True)
    reponse1 = db.Column(db.String(120))
    reponse2 = db.Column(db.String(120))
    choix1 = db.Column(db.String(120))
    choix2 = db.Column(db.String(120))
    choix3 = db.Column(db.String(120))
    choix4 = db.Column(db.String(120))

    __mapper_args__ = {
        'polymorphic_identity': 'multiple',
    }

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'question_type': self.question_type,
            'reponse1': self.reponse1,
            'reponse2': self.reponse2,
            'choix1': self.choix1,
            'choix2': self.choix2,
            'choix3': self.choix3,
            'choix4': self.choix4
        }
    
    def add_question(title, question_type, reponse1, reponse2, choix1, choix2, choix3, questionnaire_id):
        if question_type != 'simple':
            raise ValueError('Invalid question type')
        question = QuestionSimple(title=title, question_type=question_type, reponse1=reponse1, reponse2=reponse2, 
                                  choix1=choix1, choix2=choix2, choix3=choix3, questionnaire_id=questionnaire_id)
        db.session.add(question)
        db.session.commit()
        return question