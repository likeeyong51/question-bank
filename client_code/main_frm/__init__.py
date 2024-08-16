from ._anvil_designer import main_frmTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class main_frm(main_frmTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def main_options_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    if self.build_quiz_rdb.checked:
      # create a quiz
      pass
    elif self.take_quiz_rdb.checked:
      # take a quiz
      pass
    else:
      # go to my test bank
      pass
