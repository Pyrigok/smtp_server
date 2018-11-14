import mysql.connector

# create connect with DB
mydb = mysql.connector.connect(
	 host='localhost',
	 user='root',
	 password='1592648'
	 )


# create DB 'mail_db'
mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE mail10_db')

# create table
mycursor.execute('USE mail_db')
mycursor.execute('CREATE TABLE received_mails (id INT AUTO_INCREMENT PRIMARY KEY, author VARCHAR(100), message_content VARCHAR(255), recipient VARCHAR(100), message_status VARCHAR(20))')