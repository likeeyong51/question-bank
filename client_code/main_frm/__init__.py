from ._anvil_designer import main_frmTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import Notification
from ..user_frm import user_frm

class main_frm(main_frmTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.item['username'] = properties['username']
    self.item['group']    = properties['group']

    # process and set group privilege options
    self.set_group_privilege()
    

  def main_options_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    if self.goto_testbank_rdb.selected:
      # go to my test bank
      open_form(
        'test_bank_frm', 
        username=self.item['username'], 
        group=self.item['group'])
      
    elif self.build_quiz_rdb.selected:
      # build a quiz
      open_form(
        'build_quiz_frm', 
        username=self.item['username'], 
        group=self.item['group'])
      
    else:
      # take a quiz
      open_form(
        'quiz_frm', 
        username=self.item['username'], 
        group=self.item['group'])

  def set_group_privilege(self):
    # hide options not available to students
    if self.item['group'] == 'Student':
      self.goto_testbank_rdb.visible = False
      self.build_quiz_rdb.visible    = False

      # populate user dropdown
      self.user_drp.items = [
        self.item['username'],
        'Change password',
        'Log out'
      ]
      
    else:
      self.goto_testbank_rdb.visible = True
      self.build_quiz_rdb.visible    = True

      # populate user dropdown
      self.user_drp.items = [
        self.item['username'],
        'Switch user',
        'Change Password',
        'Log out'
      ]

  def user_drp_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.user_drp.selected_value == 'Log out':
      Notification('Good bye!', title='Logging out...').show()
      open_form('user_frm')

    elif self.user_drp.selected_value == 'Switch user':
      # reset user drop box
      self.user_drp.selected_value = self.user_drp.items[0]
      # store user before switching
      previous_user = self.item['username']
      
      switch_user = alert(
        content=user_frm(mode='switch-user'),
        title='Switch User Login',
        large=True,
        buttons=[('Cancel', False)]
      )

      if not switch_user and previous_user == self.item['username']:
        Notification('Switch user cancelled').show()

    elif self.user_drp.selected_value == 'Change password':
      pass
