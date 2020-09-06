from flask import Flask, request

import gzip
import dill

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'

@app.route('/about')
def about():
    return 'This page is all about my ML model'

@app.route('/predict', methods=['GET'])
def predict():
    """
    Show prediction of the sentiment of a tweet input by a user
    """
    tweet = request.args.get('tweet')

    # load persistent model
    with gzip.open('sentiment_model.dill.gz', 'rb') as f:
        model = dill.load(f)

    # predict the sentiment of the tweet
    proba = model.predict_proba([tweet])[0, 1]

    return 'Probability of being a positive sentiment: {}'.format(proba)


if __name__ == '__main__':
    app.run()