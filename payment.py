
key_id = 'rzp_test_mmKKo3Cgpov418'
key_Secret= 'lGmr6xButxlh0x0W4UKO5auq'

import razorpay
client = razorpay.Client(auth=(key_id,key_Secret))

#checkout
data ={
    'amount' : 100*1000,
    "currency" : "INR",
    "receipt" : "enjoy your day , where homies made it",
    "notes" : {
        "name" : "Homies",
        "payment_for" : "Turf"
    }
}

#server orderid
order = client.order.create(data=data)
print(order)
def func():
    return order['id']


{'id': 'order_Lh9sRLcpdYTDaX',
 'entity': 'order', 'amount': 100000,
 'amount_paid': 0, 'amount_due': 100000,
 'currency': 'INR',
 'receipt': 'enjoy your day , where homies made it', 'offer_id': None,
 'status': 'created', 'attempts': 0,
 'notes': {'name': 'Homies', 'payment_for': 'Turf'},
 'created_at': 1682236628}

datadict =  {'razorpay_payment_id': 'pay_LhAV8Tm2itRT4o', 'razorpay_order_id': 'order_Lh9sRLcpdYTDaX', 'razorpay_signature': '7c1e96180d5ad05aedece1b29691d86230f890c6f98982a5d02c80a6470e30ab'}

func()
# ver = client.utility.verify_payment_signature(datadict)
# print(ver)

