import os
import urllib, json
from twilio.rest import Client
from twilio.twiml.voice_response import Dial, Play, VoiceResponse
from flask import Flask
account_sid = "AC7788c9bc0efe0c99795a9fd1c93cce1a"
auth_token  = "b00440261911f15310141bb2ceff295c"
client = Client(account_sid, auth_token)
phone_numbers = ["+19082178884", "+19178651377"]
#"_17327591778"

app = Flask(__name__)
@app.route('/conference', methods=['GET', 'POST'])
def call():
  r = VoiceResponse()
  r.dial().conference('1')
  for number in phone_numbers:
    ca(to=number, from_="+17322274290", url='http://twimlets.com/conference')

@app.route('/text', methods=['GET','POST'])
def text():
  for number in phone_numbers:
    client.messages.create(
      to=number,
      from_ = "+17322274290",
      body = ":)")

@app.route('/gif', methods=['GET', 'POST'])
def gif():	
   for number in phone_numbers:
	data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=cow&api_key=gCrGm8PFejkEP3uHX61dnDg6FQ5dNRow&limit=5").read())
	
	medialink = data['data'][0]['images']['fixed_height']['url']
	print(medialink)
#	print(mediallink)
	client.messages.create(
		to=number,
		from_="+17322274290",
		body="MOOOOOOOOOOOOOOOOO",
		media_url= medialink
	)

#if __name__ == "__main__":
#  call()
#  text()
#  app.run()
