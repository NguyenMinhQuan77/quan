import getpass
import imaplib
import pprint
GOOGLE_IMAP_SERVER = 'imap.googlemail.com'
IMAP_SERVER_PORT = '993'

def check_mail(username, password):
    mailbox = imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER,IMAP_SERVER_PORT)
    mailbox.login(username, password)
    mailbox.select('Inbox')
    tmp, data = mailbox.search(None, 'ALL')
    for num in data[0].split():
        tmp, data =mailbox.fetch(num, '(RFC822)')
        print('Email: {0}\n'.format(num))
        pprint.pprint(data[0][1])
    mailbox.close()
    mailbox.logout()

if __name__=='__main__':
    username = input("enter email account: ")
    password = getpass.getpass(prompt = "enter password: ")
    check_mail(username,password)