import smtplib
import email.utils
from email.mime.text import MIMEText

msg_author_name = input('Enter your name - ')
msg_author_mail = input('Enter your mail - ')
msg_subject = input('Enter subject of message - ')
msg_content = input('Enter your message - ')
msg_recipient_name = input('Enter recipient name - ')
msg_recipient_mail = input('Enter recipient mail - ')


# Create the message
msg = MIMEText(msg_content) #MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr((msg_recipient_name, msg_recipient_mail))
msg['From'] = email.utils.formataddr((msg_author_name, msg_author_mail))
msg['Subject'] = msg_subject

server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(True) # show communication with the server

try:
    server.sendmail(msg_author_mail, [msg_recipient_mail], msg.as_string())
finally:
    server.quit()