#from API import API
from Scheduler import Scheduler, Tweet
import sys

class Tasks(object):
    """TODO:description of class"""
    def __init__(self):
#        self.twitter_api = API()
        self.scheduler = Scheduler()
        pass

    def store_tweet(self):
        """TODO: These inputs need to have assertions in place."""
#        self.scheduler.print_some_times()
        status = input("Status: ")

        media = input("Media Location (press enter if None):")
        if media == "":
            media = None

        print("Now lets talk about when you want it posted. If you enter enter through all prompts, it will assume 15 seconds from now.")
        year = input("year: ")
        day = input("day: ")
        hour = input("hour: ")

        self.scheduler.schedule_tweet(tweet)
        pass

    def start_server(self):
#        self.twitter_api.tweet(status="test")
        pass

    def analyze(self):
        pass

    def quit(self):
        sys.exit()
