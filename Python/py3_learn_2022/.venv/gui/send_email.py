
import smtplib

sender = "carlmukoyi@gmail.com"
receiver = "carlos@visightsolutions.co.za"
password = "xhqjfhsgmodgtnvy"
subject = "GTC Administrators"
body = "I sent email using python"

message = f"""From: GTC Administrators {sender}
To:{receiver}
Subject:{subject}\n
{body}

"""
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

try:
    server.login(sender,password)
    print("logged in")

    server.sendmail(sender,receiver,message)    
    print("Email has been sent")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")