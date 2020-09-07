import requests

def get_prediction(tweet):
    """
    Gets a prediction from app.py running locally
    """
    url = url = "http://127.0.0.1:5000/"
    response = requests.get(url + 'predict', params={'tweet': tweet})

    return response

if __name__ == '__main__':
    # prompt a user for a message whose 
    # sentiment will be predicted  
    tweet = input("Enter a message: ")
    response = get_prediction(tweet)
    print('Status code: {}'.format(response.status_code))
    print(response.text)
