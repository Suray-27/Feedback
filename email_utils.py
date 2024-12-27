import smtplib # Required Libraries
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

# Initialise Email system
def email_coupon(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['to'] = to


    user = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    msg['from'] = user

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465) # Gmail port
    server.login(user, password)

    server.send_message(msg)
    server.quit()


