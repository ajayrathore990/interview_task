import twitter


all_auth = {
    'access_token': "3021282864-PA48qApRQxPjJs7crqcONZfQZvjBsyHWECAoAaj",
    'access_token_secret': "YznXV4BP2FOPVbLeuPkheCbH5jVO0lWL4DtD5mvWwal8a",
    'consumer_key': "S6w3NzIHzOlGty0IN7XbIOU65",
    'consumer_secret': "Jy4cWGwfJnMHPrBy1C4f9Zcp8NEML6bJlGsdneOAhNQsOz8koQ"
    }

api = twitter.Api(consumer_key=all_auth['consumer_key'],
                  consumer_secret=all_auth['consumer_secret'],
                  access_token_key=all_auth['access_token'],
                  access_token_secret=all_auth['access_token_secret'])

t = api.GetUserTimeline(screen_name="RahulGandi", count=100)