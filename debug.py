import smtpd
import asyncore

server = smtpd.DebuggingServer(('localhost', 1025), None)

asyncore.loop()