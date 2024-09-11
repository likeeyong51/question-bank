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

    # Any code you write here will run before the form opens
    # populate group dropdown items
    self.group = [
      grp['group'] for grp in app_tables.group_tbl.search()
    ]
    # print(self.item['group'])
    self.group_drp.items = self.group

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

  def login_signup_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.sign_up_chk.checked:
      # sign up mode
      if self.validate_input_data():
        # print(self.item)
        if not anvil.server.call('create_user', self.item):
          Notification('User already exists.').show()
          self.reset_form()
          return

        # check if new user has been successfully added into the user table 
        if anvil.server.call('authenticate_user', self.item['username'], self.item['password'], self.item['group']):
          self.reset_form()
          Notification('You are signed up! Please attempt your first login', 
                       title='Welcome to your Test Bank App').show()
      else:
        alert('Please enter your username, password and email', title='Error')
    else:
      # log in mode
      if self.validate_input_data():
        user_exist = anvil.server.call('authenticate_user', self.item['username'], self.item['password'], self.item['group'])
    
        if user_exist:
          open_form('main_frm', username=self.item['username'], group=self.item['group'])
          Notification('Welcome to your test bank!', title='Welcome').show()
        else:
          alert('Please check your login credentials and try again...', title='Error')

  def validate_input_data(self):
    # validate login data
    if self.username_txb.text == '':
      alert('Please enter your username',    title='Error')
      return False
    if self.password_txb.text == '':
      alert('Please enter a valid password', title='Error')
      return False
    if self.group_drp.selected_value not in self.group_drp.items:
      alert('Please select your user group', title='Error')
      return False
      
    if self.sign_up_chk.checked:
      # sign up mode - additional validations
      if self.firstname_txb.text == '':
        alert('Please enter your first name', title='Error')
        return False
      if self.lastname_txb.text == '':
        alert('Please enter your last name',  title='Error')
        return False
      if self.email_txb.text == '':
        alert('Please enter your email',      title='Error')
        return False

    return True # no error'

  def reset_form(self):
    """reset form to login mode"""
    self.sign_up_chk.checked      = False
    self.login_signup_btn.text    = 'Log In'
    
    self.username_txb.text        = ''
    self.password_txb.text        = ''
    self.group_drp.selected_value = None
    self.firstname_txb.text       = ''
    self.lastname_txb.text       = ''
    self.email_txb.text           = ''

    self.username_txb.focus()
        