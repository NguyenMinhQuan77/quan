import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

SMTP_SERVER ='aspmx.l.google.com'
SMTP_PORT = 25

def send_email(sender, receipt):
    msg = MIMEMultipart()
    msg['To'] = receipt
    msg['From'] = sender
    subject = input("enter subject: ")
    msg['Subject'] =subject
    massage = input('Email content: ')
    part = MIMEText('text','plain')
    part.set_payload(massage)
    msg.attach(part)

    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.set_debuglevel(1)
    session.ehlo()
    session.starttls()
    session.ehlo()
    password = getpass.getpass("Enter your email password: ")

    session.sendmail(sender, receipt, msg.as_string())
    print("your email is sent to {0}".format(receipt))
    session.quit()

if __name__ == '__main__':
    sender = input("From address: ")
    receipt = input("To address")
    send_email(sender, receipt)