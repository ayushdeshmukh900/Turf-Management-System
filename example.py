# m.py
def generate_order_id():
    # logic to generate the order ID
    print('ABC123')

import subprocess

def get_order_id():
    result = subprocess.run(['python', 'example.py'], stdout=subprocess.PIPE)
    order_id = result.stdout.decode().strip()
    return order_id

import tkinter as tk

root = tk.Tk()

order_id_label = tk.Label(root, text='Order ID:')
order_id_label.pack()

order_id_value = tk.Label(root, text='')
order_id_value.pack()

def update_order_id():
    order_id = get_order_id()
    order_id_value.config(text=order_id)

update_order_id_button = tk.Button(root, text='Update Order ID', command=update_order_id)
update_order_id_button.pack()

root.mainloop()
