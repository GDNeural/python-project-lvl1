import prompt

name = prompt.string('May I have your name?')

def welcome_user():
     greeting = print('Hello, %s!'%(name))
     return greeting
