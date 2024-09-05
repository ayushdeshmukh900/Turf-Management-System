import razorpay
import tkinter as tk

class PaymentForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        import razorpay
        self.razorpay_client = razorpay.client(auth=('rzp_test_mmKKo3Cgpov418', 'lGmr6xButxlh0x0W4UKO5auq'))
        self.create_widgets()


# Initialize the Razorpay client with your API keys
razorpay_client = razorpay.client(auth=('YOUR_KEY_ID', 'YOUR_KEY_SECRET'))

class PaymentForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.amount_label = tk.Label(self, text="Enter Amount (in paisa):")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()

        self.name_label = tk.Label(self, text="Enter Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.email_label = tk.Label(self, text="Enter Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.phone_label = tk.Label(self, text="Enter Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self)
        self.phone_entry.pack()

        self.pay_button = tk.Button(self, text="Pay", command=self.pay)
        self.pay_button.pack()

    def pay(self):
        amount = int(self.amount_entry.get())
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        # Create the Razorpay order
        order_amount = amount / 100  # Convert from paisa to rupees
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        data = {
            "amount": order_amount,
            "currency": order_currency,
            "receipt": order_receipt,
            "payment_capture": '1'
        }
        order = razorpay.client.order.create(data=data)

        # Create the payment link
        payment_link = order['short_url']

        # Open the payment link in a web browser
        import webbrowser
        webbrowser.open(payment_link)

root = tk.Tk()
app = PaymentForm(master=root)
app.mainloop()
