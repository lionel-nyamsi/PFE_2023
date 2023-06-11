import sqlite3
import datetime


def message_a_contact(contact, message_content):

    global connection
    date_today = datetime.date.today()
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute

    time_now = str(hour) + ":" + str(minute)

    try:
        connection = sqlite3.connect("../data_base/db_liionAssist.db")
        cursor = connection.cursor()

        newMessage = (cursor.lastrowid, contact.name, contact.number_1, message_content, date_today, time_now)
        request = 'INSERT INTO sent_message VALUES (?, ?, ?, ?, ?, ?)'

        cursor.execute(request, newMessage)
        connection.commit()

    except Exception as error:
        print("[ERROR] : {}".format(error))

    finally:
        connection.close()


class Contact:

    def __init__(self, name, number1, color, first_name='', number2='', number3=''):
        self.name = str(name)
        self.first_name = first_name
        self.number_1 = str(number1)
        self.number_2 = number2
        self.number_3 = number3
        self.color = color

    def display_contact_info(self):
        print("{} {} {}".format(self.name, self.color, self.number_1))  # temporaire

