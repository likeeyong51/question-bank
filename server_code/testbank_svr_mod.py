import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

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

# implementing CRUD principle

# Create
@anvil.server.callable
def add_question(question): # , current_user):
  # if question is not None:
  #   current_user = app_tables.user_tbl.search(username=current_user)
  #   # print(*current_user[0]['username'])
  
  # if current_user is not None:
  print(question)
  app_tables.question_tbl.add_row(**question) #, user=current_user[0])
  
# Read
@anvil.server.callable
def get_questions(): # username):
  # current_user = app_tables.user_tbl.search(username=username)
  # print(*current_user[0]['username'])

  # if current_user is not None:
  return app_tables.question_tbl.search(
    tables.order_by("question_name", ascending=True) #,
    # user=current_user[0]
  )
  
# Update
@anvil.server.callable
def update_question(old_question, new_question):
  # print(f"updating question {question['question']} {new_status}")
  # get the task from the reminders table
  print(old_question)
  print(new_question)
  row = app_tables.question_tbl.get(question=old_question) #, user=new_question['user'])

  if row: # if exist, update task description and status of reminder
    row['question_name'] = new_question['question_name']
    row['question']      = new_question['question']
    row['answer']        = new_question['answer']
  
# Delete
@anvil.server.callable
def delete_question(question):
  question.delete()
