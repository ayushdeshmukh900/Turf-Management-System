import razorpay
from tkinter import *


root = Tk()
root.geometry("300x200")

amount_label = Label(root, text="Enter Amount")
amount_label.pack()

amount_entry = Entry(root)
amount_entry.pack()

pay_button = Button(root, text="Pay", command=lambda: handle_razorpay_payment(float(amount_entry.get())))
pay_button.pack()


razorpay_key_id = "rzp_test_mmKKo3Cgpov418"
razorpay_key_secret = "lGmr6xButxlh0x0W4UKO5auq"



client = razorpay.Client(auth=(razorpay_key_id, razorpay_key_secret))

def create_razorpay_order(amount):
    amount_in_paisa = int(amount * 100)
    order_data = {
        "amount": amount_in_paisa,
        "currency": "INR",
        "payment_capture": 1
    }
    razorpay_order = client.order.create(data=order_data)
    return razorpay_order

def handle_razorpay_payment_success(payment_id):
    print("Payment Success!")

def handle_razorpay_payment_failure(payment_id):
    print("Payment Failed!")

def initiate_razorpay_payment(amount):
    razorpay_order = create_razorpay_order(amount)
    payment_data = {
        "amount": razorpay_order['amount'],
        "currency": "INR",
        "order_id": razorpay_order['id'],
        "receipt": "receipt#1",
        "payment_capture": 1
    }
    razorpay_payment = client.payment.capture(payment_data['order_id'], payment_data['amount'], payment_data)
    return razorpay_payment['id']

def handle_razorpay_payment(amount):
    payment_id = initiate_razorpay_payment(amount)
    while True:
        payment = client.payment.fetch(payment_id)
        if payment['status'] == 'captured':
            handle_razorpay_payment_success(payment['id'])
            break
        elif payment['status'] == 'failed':
            handle_razorpay_payment_failure(payment['id'])
            break
    print("Payment Data: ", payment)


root.mainloop()
