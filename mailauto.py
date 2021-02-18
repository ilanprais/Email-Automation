import smtplib
import sys
import os
import imghdr
from email.message import EmailMessage
class EmailConnection():

    def __init__(self, sender, senderPass):
        self.sender = sender
        self.senderPass = senderPass
        self.smtp = None

    def setup(self):
        #creating smtp port
        self.smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        #connecting to email
        self.smtp.login(self.sender, self.senderPass)

    def sendMessage(self, recievers, subject, content, imagePath = None):
        #message
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = recievers
        msg.set_content(content)

        if imagePath != None:
            img = open(imagePath, 'rb')
            data = img.read()
            imgtype = imghdr.what(img.name)
            imgname = img.name
            msg.add_attachment(data, maintype='image', subtype=imgtype, filename=imgname)

        print(f'sending email to {recievers}')
        #sending the message
        self.smtp.send_message(msg)

        print("Email Sent Successfully!")
    
    def close(self):
        self.smtp.close()


DEFAULT_EMAIL = "****"
DEFAULT_PASSWORD = "****"

if len(sys.argv) == 3:
    EMAIL = sys.argv[0]
    PASSWORD = sys.argv[1]
else:
    print("Using default email and password")
    EMAIL = DEFAULT_EMAIL
    PASSWORD = DEFAULT_PASSWORD

if len(sys.argv) == 2 or len(sys.argv) == 4:
    RECIEVER_ADDRESS = sys.argv[len(sys.argv) - 1]
else:
    RECIEVER_ADDRESS = EMAIL

connection = EmailConnection(EMAIL, PASSWORD)
connection.setup()
connection.sendMessage([RECIEVER_ADDRESS], "test email", f'This is an automated email from {EMAIL}\n Do not Replay')
connection.close()


