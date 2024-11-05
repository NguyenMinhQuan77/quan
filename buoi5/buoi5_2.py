import getpass
import imaplib
import pprint
import poplib
GOOGLE_IMAP_SERVER = 'imap.googlemail.com'
IMAP_SERVER_PORT = '995'

def check_mail(username, password):
    mailbox = poplib.POP3_SSL(GOOGLE_IMAP_SERVER,IMAP_SERVER_PORT)
    mailbox.user(username)
    mailbox.pass_(password)
    num_message = len(mailbox.list()[1])
    print("Total email: {}".format(num_message))
    for msg in mailbox.retr(num_message)[1]:
        print(msg)
    mailbox.quit()

if __name__=='__main__':
    username = input("enter email account: ")
    password = getpass.getpass(prompt = "enter password: ")
    check_mail(username,password)