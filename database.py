import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="cybsec"
)

mycursor = mydb.cursor()

def all_records():
	query = 'SELECT * FROM status'
	mycursor.execute(query)
	x = mycursor.fetchall()
	return x

def get_status(id):
	if (get_record(id)):
		return get_record(id)[1]
	return "None"

def get_record(id):
	query = 'SELECT * FROM status where id = ' + str(id)
	mycursor.execute(query)
	return mycursor.fetchone()

def inser_record(status):
	sql = "INSERT INTO status (status) VALUES ('" + status + "')"
	mycursor.execute(sql)
	mydb.commit()
	return mycursor.lastrowid

def update_record(id, status):
	date = "NULL"
	if(status == "Finished"):
		date = datetime.datetime.now().strftime("%x")
	sql = "UPDATE status SET status = '" + status + "', finish_time ='" + date + "' WHERE id = " + str(id)
	mycursor.execute(sql)
	mydb.commit()
	return mycursor.rowcount

def delete_record(id):
	sql = "DELETE FROM status WHERE id=" + str(id)
	mycursor.execute(sql)
	mydb.commit()
	return mycursor.rowcount

# print "status of second row: " + str(get_status(89))
# print update_record(2, 'Not Done')
# print update_record(8, 'Finished')
# print "inserted with id: " + str(inser_record("Processing"))
# print delete_record(2)
# x = all_records()
# for i in x:
# 	print i