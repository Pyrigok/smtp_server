import smtpd
import asyncore
import mysql.connector

import smtplib


class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        print ('Receiving message from:', peer)
        print ('Message addressed from:', mailfrom)
        print ('Message addressed to  :', rcpttos)
        print('data - ', data)
        print ('Message length:', len(data))

        for addres in rcpttos:
        	mail_addres=addres

        db=mysql.connector.connect(
						 host='localhost',
						 user='root',
						 password='1592648',
						 database='mail10_db')

        db_cursor = db.cursor()
        sql = 'INSERT INTO received_mails (author, message_content, recipient) VALUES (%s, %s, %s)'
        val = (mailfrom, data, mail_addres)
        db_cursor.execute(sql, val)

        db.commit()
        db_cursor.close()
        print('Letter saved!')

        return

server = CustomSMTPServer(('localhost', 1025), None)

asyncore.loop()