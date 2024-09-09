from ._anvil_designer import test_bank_frmTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..edit_question_frm import edit_question_frm

class test_bank_frm(test_bank_frmTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.refresh_questions()

    # set delete_reminder event handler to the reminders_pnl
    self.preview_questions_rpnl.set_event_handler('x-delete-question', self.delete_question)

  def back_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('main_frm')

  def add_question_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Initialise an empty dictionary to store the user inputs
    new_question = {}
    # open an alert displaying the ARticleEdit form
    save_clicked = alert(
      content = edit_question_frm(item=new_question, edit=False),
      title   = "Add Question",
      large   = True,
      buttons = [("Save", True),("Cancel", False)]
    )
    
    # If the alert returned 'True', the save button was clicked
    if save_clicked:
      # Then, add new reminder to the database
      anvil.server.call('add_question', new_question) #, self.item['username'])
      self.refresh_questions()

  def refresh_questions(self):
    # populate reminders_pnl items with the list of reminders
    #print(self.item['username'])
    self.preview_questions_rpnl.items = anvil.server.call('get_questions') #, self.item['username'])

  def delete_question(self, question, **event_args):
    anvil.server.call('delete_question', question)
    self.refresh_questions()

    
