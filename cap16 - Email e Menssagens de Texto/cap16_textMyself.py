#!/home/pdajgs/python_labs/py3.7/bin/python3

# configurações pré-definidas
accountSID = 'my_account_sid'
authToken = 'my_auth_token'
myNumber = 'my_number'
twilioNumber = 'my_twilio_number'

# função de envio
from twilio.rest import Client

def textmyself(message):    # alterado para minúsculo
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)