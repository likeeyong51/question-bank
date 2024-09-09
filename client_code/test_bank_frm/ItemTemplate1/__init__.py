from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


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

   
      
