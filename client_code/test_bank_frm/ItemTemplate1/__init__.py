from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...edit_question_frm import edit_question_frm

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if self.item['answer']:
      self.true_rdb.selected  = True
    else:
      self.false_rdb.selected = True

  def delete_clicked(self, **event_args):
    """This method is called when the button is clicked"""
    if confirm("Are you sure you want to delete?"):
      self.parent.raise_event('x-delete-question', question=self.item)

  def edit_btn_click(self, **event_args):
    """update current question"""
    old_question = self.item['question']
      
    new_question = dict(self.item)
    
    print(old_question)
    # open an alert displaying the ArticleEdit form
    save_clicked = alert(
      content = edit_question_frm(item=new_question, edit=True),
      title   = "Update Question",
      large   = True,
      buttons = [("Save", True),("Cancel", False)]
    )

    if save_clicked:
      print(new_question)
      # referesh form interface with new change(s)
      self.question_txa.text = new_question['question']
      
      if new_question['answer']:
        self.true_rdb.selected  = True
      else:
        self.false_rdb.selected = True
      # update question database
      anvil.server.call('update_question', old_question, new_question)

  def answer_rdb_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    if self.item['answer']:
      self.true_rdb.selected  = True
    else:
      self.false_rdb.selected = True

   
      
