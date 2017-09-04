import twitter
from DataProcessor import DataProcessor

USERPATH = "C:/Users/JakeT/OneDrive/Documents/Visual Studio 2017/Projects/Pytter/Pytter/database/user.csv"

class API(object):
    """Description:  Object used for tweeting and accessing information from twitter.
       TODO: tweet() function needs to be updated to work with images.
    """

    def __init__(self):
        self.profile = Profile()
        self.api = twitter.Twitter(auth = self.profile.authenticate())

    def tweet(self, status=None, image=None):
        if status != None and image == None:
            assert type(status) == type(""), "Status update must be a string."
            self.api.statuses.update(status=status)
        if image != None:
            assert type(status) == type("") or status == None, "Status update must be a string."
            
            with open(image, "rb") as image_file:
                image_data = image_file.read()
                t_up = twitter.Twitter(domain='upload.twitter.com', auth = self.profile.authenticate())
                id_img1 = t_up.media.upload(media=image_data)
                id_img2 = t_up.media.upload(media=image_data)

                self.api.statuses.update(status=status, media_ids=",".join([id_img1, id_img2]))

class Profile(object):
    """TODO: ADD CLASS DESCRIPTION"""
    def __init__(self):
        self.processor = DataProcessor(file_path=USERPATH)

    def authenticate(self):
        consumer_key = list(self.processor.get_column_np("consumer_key"))[0]
        consumer_secret = list(self.processor.get_column_np("consumer_secret"))[0]
        access_token = list(self.processor.get_column_np("access_token"))[0]
        access_token_secret = list(self.processor.get_column_np("access_token_secret"))[0]

        return twitter.OAuth(access_token, access_token_secret, consumer_key, consumer_secret)