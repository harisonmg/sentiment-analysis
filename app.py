from flask import Flask, request, render_template

import gzip
import dill

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    Present a form for submitting some text for 
    sentiment prediction
    """
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """
    Show prediction of the sentiment of a tweet input by a user
    """
    if request.method == 'GET':
        tweet = request.args.get('tweet')

    else:
        tweet = request.form['text-area']

    # load persistent model
    with gzip.open('sentiment_model.dill.gz', 'rb') as f:
        model = dill.load(f)

    # predict the sentiment of the tweet
    proba = model.predict_proba([tweet])[0, 1]

    return render_template('predict.html', proba=proba)


if __name__ == '__main__':
    app.run()