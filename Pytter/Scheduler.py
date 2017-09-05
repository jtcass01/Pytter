import sched, time
from datetime import datetime
from DataProcessor import DataProcessor
import datetime

class Scheduler(object):
    """description of class"""
    def __init__(self):
        self.schedule = DataProcessor("C:/Users/JakeT/OneDrive/documents/visual studio 2017/Projects/Pytter/Pytter/database/tweet_schedule.csv")

    def schedule_tweet(self, tweet):
#        print(self.schedule, "schedule before")
        self.schedule.add_row(tweet.to_list())
#        print(self.schedule, "schedule after")
        pass

"""IMPORTANT!!! Must use datetime.datetime since time does not hold day and year values!!!"""
class Tweet(object):
    """description of class"""
    def __init__(self, status = None, media = None, tweet_time=None):
        self.status = status
        self.media = media
        if tweet_time == None:
            self.tweet_time = datetime.datetime.now() + datetime.timedelta(seconds=15)
        else:
            self.tweet_time = tweet_time

    def __str__(self):
        return str(self.to_list())

    def to_list(self):
        return [self.status,self.media,self.tweet_time]