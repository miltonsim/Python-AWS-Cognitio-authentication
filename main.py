import os
from warrant import Cognito

os.environ['AWS_DEFAULT_REGION'] = 'YOUR-AWS-REGION'
os.environ['AWS_ACCESS_KEY_ID'] = 'YOUR-AWS-ACCESS-KEY-ID'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'YOUR-AWS-SECRET-ACCESS-KEY'

pool_id = 'YOUR-POOL-ID'
# Generate app client without secret
app_client_id = 'YOUR-APP-CLIENT-ID'

def authenticate(username, password):
  u = Cognito(pool_id, app_client_id, username=username)
  u.authenticate(password=password)

  print(u.access_token)

def register(username, password, email):
  u = Cognito(pool_id, app_client_id)
  u.add_base_attributes(email=email)
  u.register(username, password)

def confirm_sign_up(username, verification_code):
  u = Cognito(pool_id, app_client_id)
  u.confirm_sign_up(verification_code, username=username)

# Register with username, password and email address
register('myusername', 'mypassword', 'myemail')

# After registering, confirm sign up with verification code sent to email 
# confirm_sign_up('myusername', 'myverificationcode')

# After confirm sign up, authenticate. If authenticated, access token will be printed
# authenticate('myusername', 'mypassword')