"""import os
from email.message import EmailMessage
import ssl
import smtplib
email_sender = 'homiesturf2410@gmail.com'
password='homiesturf2410@'
email_receiver='saksham.g1012@gmail.com'

subject='sdfghjkl'
body=""""""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
"""
from tkinter import messagebox

import pymysql
import pyotp
import smtplib
import random

# connect to the database
"""db = pymysql.connect(
    host="localhost",
    user="username",
    password="password",
    database="database_name"
)"""

try:
    con = pymysql.connect(host='localhost', user='root', password='root')
    mycursor = con.cursor()
except:
    messagebox.showerror('Error', 'Database Connectivity Issue, Please try Again')


# generate an OTP
def generate_otp():
    # generate a random 6-digit OTP code
    otp = random.randint(100000, 999999)
    return otp

# send the OTP to the user's email
def send_otp_email(email, otp):
    # set up the email server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # login to your email account
    server.login("your_email_address", "your_email_password")
    # create the email message
    message = f"Your OTP code is: {otp}"
    # send the email
    server.sendmail("your_email_address", email, message)
    # close the email server
    server.quit()

# verify the OTP for the given user
def verify_otp(email, otp):
    # get the secret key for the user from the database
    cursor = con.cursor()
    cursor.execute("SELECT secret_key FROM users WHERE email=%s", (email,))
    result = cursor.fetchone()
    secret_key = result[0]
    # create an OTP object with the secret key
    totp = pyotp.TOTP(secret_key)
    # verify the OTP code
    if totp.verify(otp):
        return True
    else:
        return False

# main function
def main():
    # get the user's email from the database
    cursor =con.cursor()
    cursor.execute("SELECT email FROM users WHERE id=1")
    result = cursor.fetchone()
    email = result[0]
    # generate an OTP code
    otp = generate_otp()
    # send the OTP code to the user's email
    send_otp_email(email, otp)
    # ask the user to enter the OTP code
    user_otp = input("Enter the OTP code sent to your email: ")
    # verify the OTP code for the user
    if verify_otp(email, user_otp):
        print("OTP code is valid")
    else:
        print("OTP code is invalid")

if __name__ == "__main__":
    main()
