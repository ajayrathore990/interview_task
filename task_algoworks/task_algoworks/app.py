import json
from flask_api import FlaskAPI
from flask import render_template
from req import *

app = FlaskAPI(__name__)


@app.route('/latest/<user>/')
def tweet_latest(user):
    calls = api.GetUserTimeline(screen_name=user, count=100)
    for i in calls:
        call= str(i)
        new = json.loads(call)
        return {
            'Time': new['created_at'],
             'Tweet': new['text']}


@app.route('/all/<user>/')
def tweet_info(user):
    call = api.GetUserTimeline(screen_name=user, count=10)
    all_tweets = [(s.text, s.created_at) for s in call]
    return {'All Tweets': all_tweets}


if __name__ == "__main__":
    app.run(debug=True)
