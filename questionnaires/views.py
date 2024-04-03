from flask import jsonify, abort, make_response, request, url_for
from .app import app, db
from .models import Questionnaire, Question, QuestionSimple, QuestionMultiple

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

# API Question
@app.route('/questionnaires', methods=['GET'])
def get_questionnaires():
    questionnaires = Questionnaire.query.all()
    return jsonify([q.to_json() for q in questionnaires])

@app.route('/questionnaires/<string:name>', methods=['POST'])
def add_questionnaire(name):
    #name = request.json.get('name')
    questionnaire = Questionnaire(name=name)
    db.session.add(questionnaire)
    db.session.commit()
    return jsonify(questionnaire.to_json()), 201

@app.route('/questionnaires/<int:id>', methods=['GET'])
def get_questionnaire(id):
    questionnaire = Questionnaire.query.get(id)
    if questionnaire is None:
        abort(404)
    return jsonify(questionnaire.to_json())

@app.route('/questionnaires/<int:id>/<string:name>', methods=['PUT'])
def update_questionnaire(id, name):
    questionnaire = Questionnaire.query.get(id)
    if questionnaire is None:
        abort(404)
    #name = request.json.get('name')
    questionnaire.name = name
    db.session.commit()
    return jsonify(questionnaire.to_json())

@app.route('/questionnaires/<int:id>', methods=['DELETE'])
def delete_questionnaire(id):
    questionnaire = Questionnaire.query.get(id)
    if questionnaire is None:
        abort(404)
    db.session.delete(questionnaire)
    db.session.commit()
    return jsonify(questionnaire.to_json())

@app.route('/questionnaires/<int:id>/questions', methods=['GET'])
def get_questions(id):
    questionnaire = Questionnaire.query.get(id)
    if questionnaire is None:
        abort(404)
    return jsonify([q.to_json() for q in questionnaire.questions])

@app.route('/questionnaires/<int:id>/questions', methods=['POST'])
def add_question(id):
    questionnaire = Questionnaire.query.get(id)
    if questionnaire is None:
        abort(400)
    title = "Nouvelle question"
    question_type = "simple"
    
    if question_type == 'simple':
        reponse = "réponse"
        choix1 = "choix1"
        choix2 = "choix2"
        choix3 = "choix3"
        choix4 = "choix4"
        print(reponse)

        try:
            question = QuestionSimple.add_question(title=title, question_type=question_type, reponse=reponse, choix1=choix1, choix2=choix2, choix3=choix3, choix4=choix4, questionnaire_id=id)
            return jsonify(question.to_json()), 201
        except ValueError as e:
            abort(400, str(e))
    elif question_type == 'multiple':
        reponse1 = request.json.get('reponse1')
        reponse2 = request.json.get('reponse2')
        choix1 = request.json.get('choix1')
        choix2 = request.json.get('choix2')
        choix3 = request.json.get('choix3')

        try:
            question = QuestionMultiple.add_question(title=title, question_type=question_type, reponse1=reponse1, reponse2=reponse2, choix1=choix1, choix2=choix2, choix3=choix3, questionnaire_id=id)
            return jsonify(question.to_json()), 201
        except ValueError as e:
            abort(400, str(e))
    else:
        abort(400, "Invalid question type")

@app.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    #questionnaire = Questionnaire.query.get(id)
    #if questionnaire is None:
    #    abort(404)

    question = Question.query.get(question_id)
    if question is None:
        abort(404)

    db.session.delete(question)
    db.session.commit()

    return jsonify({'message': 'Question deleted successfully'}), 200

@app.route('/questions/<int:question_id>/<string:title>', methods=['PUT'])
def update_question(question_id, title):
    question = Question.query.get(question_id)
    if question is None:
        abort(404)
    question.title = title
    db.session.commit()
    return jsonify(question.to_json())
