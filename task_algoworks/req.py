import twitter


all_auth = {
    'access_token': "xxxxx",
    'access_token_secret': "xxxx",
    'consumer_key': "xxxx",
    'consumer_secret': "xxxx"
    }

api = twitter.Api(consumer_key=all_auth['consumer_key'],
                  consumer_secret=all_auth['consumer_secret'],
                  access_token_key=all_auth['access_token'],
                  access_token_secret=all_auth['access_token_secret'])

t = api.GetUserTimeline(screen_name="RahulGandi", count=100)
