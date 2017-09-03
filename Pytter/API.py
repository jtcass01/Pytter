import twitter

class API(object):
    """description of class -- UPDATE"""
    def __init__(self, TOKEN = "417857575-fRZFQbM6N2z7Hd6vYn8EAOfufsDoA1JPBebFKUBI", TOKEN_KEY = "oCRnAlteVwKfxUBIkfvKCueUTJTW6EL68lgcMeBPVDrFf", CON_SEC_KEY = "bpnYcmfXsoGVka9KIp1mooNFyMkesM2wJsBLEFLzwvD8DM7DDa", CON_SEC = "z8KJ9B0zX8EuHINoJuYtd8E6B"):
        self.consumer_key = CON_SEC
        self.consumer_secret = CON_SEC_KEY
        self.access_token = TOKEN
        self.access_token_secret = TOKEN_KEY        
        self.o_auth = twitter.OAuth(TOKEN, TOKEN_KEY, CON_SEC, CON_SEC_KEY)
        self.api = twitter.Twitter(auth = self.o_auth)

    def tweet(self, status):
        assert type(status) == type(""), "Status update must be a string."

        self.api.statuses.update(status=status)