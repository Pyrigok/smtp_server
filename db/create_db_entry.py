import mysql.connector

# connect with DB
def new_entry(msg_author_name, msg_author_mail, msg_subject, msg_content, msg_recipient_name, msg_recipient_mail):
	db=mysql.connector.connect(
		 host='localhost',
		 user='root',
		 password='1592648',
		 database='mail_db')

	db_cursor = db.cursor()
	sql = 'INSERT INTO received_letters (author, author_mail, message_subject, message_content, recipient_name, recipient_mail, message_status) VALUES (%s, %s, %s, %s, %s, %s, %s)'
	val = (msg_author_name, msg_author_mail, msg_subject, msg_content, msg_recipient_name, msg_recipient_mail)
	db_cursor.execute(sql, val)

	db.commit()
	print(db_cursor.rowcount, 'letter saved!')