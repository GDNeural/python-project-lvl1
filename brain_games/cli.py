import prompt

def get_name():
     get_name.name = prompt.string('May I have your name? ')

def welcome_user():
     get_name()
     greeting = print('\nHello, %s!\n'%(get_name.name))
     return greeting
