import sched, time
from DataProcessor import DataProcessor
from datetime import datetime
from Scheduler import Tweet

class Server(object):
    """description of class"""
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.tweet_schedule = DataProcessor("C:/Users/JakeT/OneDrive/documents/visual studio 2017/Projects/Pytter/Pytter/database/tweet_schedule.csv")
        pass

"""    def print_time(self, a='defualt'):
        print("From print_time", time.time(),a)

    def print_some_times(self):
        print(time.time())
        self.scheduler.enter(10, 1, self.print_time)
        self.scheduler.enter(5,1,self.print_time, kwargs={'a':'keyword'})
        self.scheduler.run()
        print(time.time())"""

