import os
import stripe
from twilio.rest import Client

def stripePayment( recipient = 0 ):
	amount = 1000
	currency = "usd"
	description = "Charge via HiFriend handshake"
	twilioNum = os.environ.get('SaraAnn_Phone_Number')
	twilioSid = os.environ.get('SaraAnn_Twilio_SID')
	twilioToken = os.environ.get('SaraAnn_Twilio_Token')
	print(twilioNum, twilioSid, twilioToken)
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
		dollaramount = (float)(result.amount) / 100
		#recbody = 
		#paybody = result.outcome.seller_message + '\n' + 'Paid: ${:10.2f} \n'.format(result.amount) + 'to: ' + receiverNum
		
		





	client = Client(twilioSid, twilioToken)

	
	client.messages.create(
    		to= payerNum,
    		from_= twilioNum,
		body= result.outcome.seller_message + "\n" + "Paid: $" + str(dollaramount) + "\nTo: HiFriend") 

	client.messages.create(
		to=receiverNum,
		from_ = twilioNum,
		body= result.outcome.seller_message + "\n" + "Received: $" + str(dollaramount) + "\nFrom: HiFriend") 


stripePayment(0)
