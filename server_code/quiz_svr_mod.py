import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from random import sample

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_random_questions(n):
    # Fetch all questions from the table
    questions = anvil.server.get_app_table('Questions').search()
    # Convert to a list
    questions_list = list(questions)
    # Randomly select n questions
    selected_questions = sample(questions_list, n)
  
    return selected_questions