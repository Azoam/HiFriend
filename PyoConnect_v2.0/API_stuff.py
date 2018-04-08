import os
from twilio.rest import Client
from twilio.twiml.voice_response import Play, VoiceResponse


account_sid = "AC7788c9bc0efe0c99795a9fd1c93cce1a"
auth_token  = "b00440261911f15310141bb2ceff295c"#"b895cced74836dd8172877ae49bc73bb"# "b00440261911f15310141bb2ceff295c"
client = Client(account_sid, auth_token)
#response = VoiceResponse()
#response.play('garbage.mp3', loop=2)



call = client.calls.create(to="+17327591778", from_ = "+17322274290", url="http://demo.twilio.com/docs/voice.xml")
print (call.sid)
