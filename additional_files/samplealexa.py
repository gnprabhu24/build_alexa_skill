import logging # required packages
from random import randint
from flask import Flask
from flask_ask import Ask, statement

app = Flask(__name__) # Creating a flask ask app

ask = Ask(app, "/") # Assigning the directory for the flask ask app as the root of the project

logging.getLogger("flask_ask").setLevel(logging.DEBUG) # Enabling debugger for the app while helps in testing


@ask.intent("MultiplicationIntent") # name of the intent mentioned in the schema
def multiply(firstnum, secondnumber):
    value = int(firstnum) * int(secondnumber) # variables passed to the funciton are always string values even though
                                              # we mentioned the type as AMAZON.NUMBER
    Message = firstnum+" times "+secondnumber+" equals "+str(value)
    return statement(Message) # statement take in a string which Alexa will use as the reply to the request

if __name__ == '__main__':
    app.run(debug=True)