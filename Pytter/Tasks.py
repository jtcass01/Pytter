from DataProcessor import DataProcessor
from API import API
from Scheduler import Scheduler
import sys

class Tasks(object):
    """description of class"""
    def __init__(self):
        self.twitter_api = API()
#        self.scheduler = Scheduler()

    def store_tweet(self):
#        self.scheduler.print_some_times()

        pass

    def start_server(self):
#        self.twitter_api.tweet(status="test")
        pass

    def analyze(self):
        pass

    def quit(self):
        sys.exit()
