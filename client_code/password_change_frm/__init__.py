from ._anvil_designer import password_change_frmTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class password_change_frm(password_change_frmTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # reset ui
    self.old_password_txb.text       = ''
    self.new_password_txb.text       = ''
    self.confirmed_password_txb.text = ''

  
  def confirmed_password_txb_changed(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.new_password_txb.text == self.confirmed_password_txb.text:
      self.tick1_lbl.foreground = '#174d25'
      self.tick1_lbl.icon       = 'fa:check'
      self.tick2_lbl.icon       = 'fa:check'
      self.tick2_lbl.tooltip    = 'Your confirmation password is the same as your new password'
    else:
      self.tick1_lbl.foreground = '#5f1725'
      self.tick2_lbl.icon       = 'fa:ban'
      self.tick2_lbl.tooltip    = 'Your confirmation password is different from your new password'

  def new_password_txb_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.old_password_txb.text == self.new_password_txb.text:
      self.tick1_lbl.icon       = 'fa:ban' # password cannot be the same
      self.tick1_lbl.foreground = '#5f1725'
      self.tick1_lbl.tooltip    = 'The new password cannot be the same as your old one'
    else:
      self.tick1_lbl.icon       = '' # remove indicator
      self.tick1_lbl.foreground = '#174d25'
      self.tick1_lbl.tooltip    = ''
      
