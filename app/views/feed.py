import http.client
import urllib.parse
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/v1/news/all')
def get_news():
    # Define the API endpoint and parameters
    conn = http.client.HTTPSConnection('api.marketaux.com')
    params = urllib.parse.urlencode({
        'api_token': 'D3tkz0oplu4NP8gJ1xcvKuHRXsTWK0jz7SCrNyGS',
        'symbols': 'AAPL,TSLA',
        'limit': 50,
    })

    # Send the API request and get the response
    conn.request('GET', '/v1/news/all?{}'.format(params))
    res = conn.getresponse()
    data = res.read()

    # Return the response as a JSON object
    return jsonify({'news': data.decode('utf-8')})

if __name__ == '__main__':
    app.run(debug=True)