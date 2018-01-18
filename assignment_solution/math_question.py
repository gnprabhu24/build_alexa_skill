import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def ready_for_question():

    welcome_msg = render_template('welcome')

    return question(welcome_msg)

@ask.intent("YesIntent")
def ask_question():

    number1 = randint(0, 20)
    number2 = randint(0, 20)

    randomQuestionList = {
        0:  {question: str(number1) +" times "+str(number2), answer: number1 * number2 },
        1:  {question: str(number1) + " plus " + str(number2), answer: number1 + number2 },
        2:  {question: str(number1) + " minus " + str(number2), answer: number1 - number2 }
    }

    randomQuestion = randint(0, 2)

    round_msg = render_template('round', question=randomQuestionList[randomQuestion][question])

    session.attributes['answer'] = randomQuestionList[randomQuestion][answer]

    return question(round_msg)

@ask.intent("AnswerIntent")
def answer(answer_given):

    correct_answer = session.attributes['answer']

    if int(answer_given) == correct_answer:

        msg = render_template('correct')

    else:

        msg = render_template('wrong', answer=correct_answer)

    return statement(msg)

if __name__ == '__main__':
    app.run(debug=True)