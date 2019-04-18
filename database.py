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

	def get_processing(self):
	    query = 'SELECT * FROM status where status = "Processing"'
	    self.mycursor.execute(query)
	    x = self.mycursor.fetchall()
	    return x

	def all_records(self):
		query = 'SELECT * FROM status'
		self.mycursor.execute(query)
		x = self.mycursor.fetchall()
		return x

	def get_record(self, id):
		query = 'SELECT * FROM status where id = ' + str(id)
		self.mycursor.execute(query)
		return self.mycursor.fetchone()


	def get_status(self, id):
		if (self.get_record(id)):
			return self.get_record(id)[1]
		return "None"

	def inser_record(self, filename, status):
		sql = "INSERT INTO status (status, name) VALUES ('" + status + "', '" + filename + "' )"
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

# database_inst = database()
# print "status of second row: " + str(database_inst.get_status(89))
# print database_inst.update_record(60, 'Finished')
# print database_inst.update_record(8, 'Finished')
# print "inserted with id: " + str(database_inst.inser_record("demo.apk", "Processing"))
# print delete_record(2)
# x = database_inst.all_records()
# for i in x:
# 	print i
# print "\n\n"
# y = database_inst.get_processing()
# for j in y:
# 	print j