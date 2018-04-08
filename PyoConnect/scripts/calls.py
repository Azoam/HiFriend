import os
from twilio.rest import Client
from twilio.twiml.voice_response import Dial, Play, VoiceResponse
from flask import Flask
account_sid = os.environ.get('SaraAnn_Twilio_SID')
auth_token  = os.environ.get('SaraAnn_Twilio_Token')
client = Client(account_sid, auth_token)
phone_numbers = ["+17327591778", os.environ.get('Ez_Phone_Number'), os.environ.get('Sam_Phone_Number')]

app = Flask(__name__)
app.route('/conference', methods=['GET', 'POST'])
def call():
  r = VoiceResponse()
  r.dial().conference('1')
  for number in phone_numbers:
    call = client.calls.create(to=number, from_=os.environ.get('SaraAnn_Phone_Number'), url='http://twimlets.com/conference')

app.route('/text', methods=['POST'])
def text():
  for number in phone_numbers:
    client.messages.create(
      to=number,
      from_ = os.environ.get('SaraAnn_Phone_Number'),
      body = "Test 123")





if __name__ == "__main__":
  call()
  text()
  app.run()
