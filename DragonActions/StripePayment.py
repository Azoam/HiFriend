import os
import stripe
from twilio.rest import Client

def stripePayment( recipient = 0 ):
	amount = 1000
	currency = "usd"
	description = "Charge via HiFriend handshake"
	twilioNum = os.environ.get('Ez_Twilio_Number')
	twilioSid = os.environ.get('Ez_Twilio_SID')
	twilioToken = os.environ.get('Ez_Twilio_Token')
	print("Attempting charge ...")
	if(recipient == 0):
		stripe.api_key = os.environ.get('Ez_Stripe_Secret')
		
		result = stripe.Charge.create(
			amount = 1000,
			currency = "usd",
			source = "tok_mastercard", 
			description = "Charge via HiFriend handshake"
		)
		
		payerNum = os.environ.get('Sam_Phone_Number')
		receiverNum = os.environ.get('Ez_Phone_Number')





	client = Client(twilioSid, twilioToken)
	
	dollaramount = (float)(result.amount) / 100
	recbody = result.outcome.seller_message + '\n' + 'Received: ${,.2f}\n'.format(dollaramount) + 'from: ' + payerNum 	
	paybody = result.outcome.seller_message + '\n' + 'Paid: ${:10.2f} \n'.format(result.amount) + 'to: ' + receiverNum
	
	client.api.account.messages.create(
    		to=payerNum,
    		from_=twilioNum,
    		body=paybody)
	client.api.account.messages.create(
		to=receiverNum,
		from_=twilioNum,
		body=paybody)


stripePayment(0)
