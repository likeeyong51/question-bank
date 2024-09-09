from ._anvil_designer import edit_question_frmTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class edit_question_frm(edit_question_frmTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def answer_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    if self.true_rdb.selected:
      self.item['answer'] = True
    else:
      self.item['answer'] = False

