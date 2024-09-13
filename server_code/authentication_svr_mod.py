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
  user = app_tables.user_tbl.get(username=user_info['username']) #, password=user_info['password'])

  # check if user exists
  if user:
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
  # get user record based on login credential
  user = app_tables.user_tbl.get(username=username, password=password)
  # print(*user['group'])
  
  if user: # if user exists
    # get the actual user group
    user_group = user['group']
    
    if user_group: # if  user group exists
      # retrieve user group name
      group_name = app_tables.group_tbl.get(group=user_group['group'])
      # if group name exists and it matches user's login group
      if group_name and group_name['group'] == group:
        return True
  
  # user does not exist yet or does not belong to the right group
  return False # not found

@anvil.server.callable
def update_user_password(user_info):
  # get user record on login credential
  user = app_tables.user_tbl.get(username=user_info['username'], password=user_info['old_password'])
  # print(*user_info)

  if user: # if user exists
    # update user password
    user['password'] = user_info['new_password']
    return True

  # update fails - user not found
  return False