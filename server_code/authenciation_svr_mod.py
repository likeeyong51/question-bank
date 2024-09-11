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

@anvil.server.callable
def create_user(user_info):
  row = app_tables.user_tbl.search(username=user_info['username'], password=user_info['password'])

  # check if user exists
  if len(row) == 1:
    return False # user exists 

  # add new user to the user table
  # print(user_info)
  group = app_tables.group_tbl.get(group=user_info['group'])
  
  app_tables.user_tbl.add_row( #**user_info)
    username   = user_info['username'], 
    password   = user_info['password'],
    group      = group,
    first_name = user_info['first_name'], 
    last_name  = user_info['last_name'], 
    email      = user_info['email'])
  
  return True # new user added to the database

@anvil.server.callable
def authenticate_user(username, password, group):
  # print(username, password)
  user = app_tables.user_tbl.search(username=username, password=password)

  if user:
    user_group = user['group']
    group = app_tables.group_tbl.get(group=user_group['group'])

    if group
  # if user exist
  if len(user) == 1:
    return True # found

  # user does not exist yet
  return False # not found