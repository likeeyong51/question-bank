from ._anvil_designer import build_quiz_frmTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class build_quiz_frm(build_quiz_frmTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.item['username'] = properties['username']
    self.item['group']    = properties['group']

  def back_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('main_frm', username=self.item['username'], group=self.item['group'])
