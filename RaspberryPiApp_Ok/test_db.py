import sqlite3
import datetime

'''connection = sqlite3.connect("data_base/db_liionAssist.db")

cursor = connection.cursor()

new_contact = (cursor.lastrowid, "Abena", "TITI", "+237 699989796", "", "")
request = 'INSERT INTO contact VALUES(?,?,?,?,?,?)'
cursor.execute(request, new_contact)
connection.commit()
# print(cursor.fetchall())

connection.close()'''

date_today = datetime.date.today()
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute

time_now = str(hour) + ":" + str(minute)
print(date_today)
print(time_now)

dt = datetime.datetime(2023, 2, 20)
print(dt)
