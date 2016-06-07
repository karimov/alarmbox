

from alarmbox import alarm

class Message(object):
    def __init__(self, alarm):
        self.alarm = alarm
        self.to = []
        self.from = None
        self.message = ''

    def __str__(self):
        return "Messege"+"("+str(self.message)+")"

