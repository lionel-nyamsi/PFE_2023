import datetime


class Message:
    def __init__(self, sender, reciever, number_texted, message_content, date, time):
        self.sender = sender
        self.reciever = reciever
        self.number = number_texted
        self.content = message_content
        self.date = date
        self.time = time
