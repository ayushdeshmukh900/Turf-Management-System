import pyotp
import random
import mysql.connector
from twilio.rest import Client

# connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="turf"
)

# generate an OTP
def generate_otp():
    # generate a random 6-digit OTP code
    otp = random.randint(100000, 999999)
    return otp

# send the OTP to the user's phone number
def send_otp_sms(phone_number, otp):
    # Your Account SID from twilio.com/console
    account_sid = "your_account_sid"
    # Your Auth Token from twilio.com/console
    auth_token  = "your_auth_token"
    client = Client(account_sid, auth_token)
    # send the OTP code to the user's phone number
    message = client.messages.create(
        to=phone_number,
        from_="your_twilio_number",
        body=f"Your OTP code is: {otp}")
    print(message.sid)

# verify the OTP for the given user
def verify_otp(phone_number, otp):
    # get the secret key for the user from the database
    cursor = db.cursor()
    cursor.execute("SELECT secret_key FROM users WHERE phone_number=%s", (phone_number,))
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
    # get the user's phone number from the database
    cursor = db.cursor()
    cursor.execute("SELECT user_phone_no FROM user WHERE user_id=1")
    result = cursor.fetchone()
    phone_number = result[0]
    # generate an OTP code
    otp = generate_otp()
    # send the OTP code to the user's phone number
    send_otp_sms(phone_number, otp)
    # ask the user to enter the OTP code
    user_otp = input("Enter the OTP code sent to your phone: ")
    # verify the OTP code for the user
    if verify_otp(phone_number, user_otp):
        print("OTP code is valid")
    else:
        print("OTP code is invalid")

if __name__ == "__main__":
    main()
