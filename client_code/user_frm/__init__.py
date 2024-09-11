from ._anvil_designer import user_frmTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class user_frm(user_frmTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def sign_up_chk_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.sign_up_chk.checked:
      self.login_signup_btn.text = 'Sign Up'
      self.login_signup_lbl.text = 'New User Sign Up'
      self.login_signup_btn.icon = 'fa:check-circle-o'
      self.firstname_txb.visible = True
      self.lastname_txb.visible  = True
      self.email_txb.visible     = True
    else:
      self.login_signup_btn.text = 'Log In'
      self.login_signup_lbl.text = 'User Log In'
      self.login_signup_btn.icon = 'fa:arrow-circle-o-right'
      self.firstname_txb.visible = False
      self.lastname_txb.visible  = False
      self.email_txb.visible     = False
