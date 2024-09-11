from ._anvil_designer import main_frmTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class main_frm(main_frmTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.item['username'] = properties['username']
    self.item['group']    = properties['group']

    # populate user dropdown
    self.user_drp.items = [
      self.item['username'],
      'Log out'
    ]

  def main_options_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    if self.open_testbank_rdb.selected:
      # go to my test bank
      open_form('test_bank_frm')
      
    elif self.build_quiz_rdb.selected:
      # build a quiz
      open_form('build_quiz_frm')
      
    else:
      # take a quiz
      open_form('quiz_frm')
