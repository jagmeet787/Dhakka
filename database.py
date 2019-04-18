import mysql.connector
import datetime

class database(object):
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="ooad",
	  passwd="root",
	  database="cybsec"
	)

	mycursor = mydb.cursor()

	def all_records(self):
		query = 'SELECT * FROM status'
		self.mycursor.execute(query)
		x = self.mycursor.fetchall()
		return x

	def get_status(self, id):
		if (get_record(id)):
			return get_record(id)[1]
		return "None"

	def get_record(self, id):
		query = 'SELECT * FROM status where id = ' + str(id)
		self.mycursor.execute(query)
		return self.mycursor.fetchone()

	def inser_record(self, status):
		sql = "INSERT INTO status (status) VALUES ('" + status + "')"
		self.mycursor.execute(sql)
		self.mydb.commit()
		return self.mycursor.lastrowid

	def update_record(self, id, status):
		date = "NULL"
		if(status == "Finished"):
			date = datetime.datetime.now().strftime("%x")
		sql = "UPDATE status SET status = '" + status + "', finish_time ='" + date + "' WHERE id = " + str(id)
		self.mycursor.execute(sql)
		self.mydb.commit()
		return self.mycursor.rowcount

	def delete_record(self, id):
		sql = "DELETE FROM status WHERE id=" + str(id)
		self.mycursor.execute(sql)
		self.mydb.commit()
		return self.mycursor.rowcount

# print "status of second row: " + str(get_status(89))
# print update_record(2, 'Not Done')
# print update_record(8, 'Finished')
# print "inserted with id: " + str(inser_record("Processing"))
# print delete_record(2)
# x = all_records()
# for i in x:
# 	print i