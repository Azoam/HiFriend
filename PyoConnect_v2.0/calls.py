import os
from twilio.rest import Client
from twilio.twiml.voice_response import Dial, Play, VoiceResponse
from flask import Flask
account_sid = "AC7788c9bc0efe0c99795a9fd1c93cce1a"
auth_token  = "b00440261911f15310141bb2ceff295c"
client = Client(account_sid, auth_token)
phone_numbers = ["+17327591778", "+19178651377"]

app = Flask(__name__)
@app.route('/conference', methods=['GET', 'POST'])
def call():
  r = VoiceResponse()
  r.dial().conference('1')
  for number in phone_numbers:
    call = client.calls.create(to=number, from_="+17322274290", url='http://twimlets.com/conference')

@app.route('/text', methods=['GET','POST'])
def text():
  for number in phone_numbers:
    client.messages.create(
      to=number,
      from_ = "+17322274290",
      body = ":)")





#if __name__ == "__main__":
#  call()
#  text()
#  app.run()
