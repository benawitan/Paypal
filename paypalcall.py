import paypalrestsdk

#configure through non-global object
my_api = paypalrestsdk.Api({
	'mode' : 'sandbox',
	'client_id' : 'AVjs9hBnsXrNRFPkf6mb_yR3LulfFCQskg4ykW5VoldpIdD5wLpG8rmVL62G',
	'client_secret' : 'EAow8BAohtlukqznNXFCQp5VKgVgMMZQ9PWW8SiMXw4LOcDR3vkQh8VQWKuE'})
#print my_api.get_token_hash()

#get payment history
payment_history = paypalrestsdk.Payment.all({"count": 10},api=my_api)
print payment_history.payments


payment = paypalrestsdk.Payment({
  "intent": "sale",
  "payer": {
    "payment_method": "paypal",
    },
  "transactions": [{
    "amount": {
      "total": "7.47",
      "currency": "USD",
      "details": {
        "subtotal": "7.41",
        "tax": "0.03",
        "shipping": "0.03"}},
    "description": "This is the payment transaction description." }],
    "redirect_urls":{
    "return_url": "http://www.tanchoonyan.com",
    "cancel_url": "http://www.tanchoonyan.com"}
    },api=my_api)

if payment.create(): 
	print ("Payment success")
else:
	print(payment.error)
