import sched, time
from DataProcessor import DataProcessor

class Scheduler(object):
    """description of class"""
    def __init__(self):
        self.schedule = DataProcessor("C:/Users/JakeT/OneDrive/documents/visual studio 2017/Projects/Pytter/Pytter/database/tweet_schedule.csv")

    def schedule_tweet(self):
        pass


class Tweet(object):
    """description of class"""
    def __init__(self, status = None, media = None):
        self.status = status
        self.media = media

    def __str__(self):
        return "[status:\"" + str(self.status), "\",[media:\"" + str(self.media) + "]"
