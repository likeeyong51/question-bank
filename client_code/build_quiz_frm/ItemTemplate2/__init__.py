from ._anvil_designer import ItemTemplate2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...edit_question_frm import edit_question_frm


class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # if self.item["answer"]:
    #   self.true_rdb.selected = True
    # else:
    #   self.false_rdb.selected = True

  

  def answer_rdb_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    if self.item["answer"]:
      self.true_rdb.selected = True
    else:
      self.false_rdb.selected = True

  def add_chk_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.add_chk.checked:
      # add question to the quiz question list
      pass
    else:
      # remove question from the quiz question list
      pass
