import http.client
import urllib.parse
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/get_data')
def get_data():
    # Your existing code that returns a list of data
    data = ['item1', 'item2', 'item3']

    # Make the API request to MarketAux
    conn = http.client.HTTPSConnection("api.marketaux.com")
    params = {
        "api_token": "D3tkz0oplu4NP8gJ1xcvKuHRXsTWK0jz7SCrNyGS",
        "symbols": "AAPL,TSLA",
        "limit": 50
    }
    encoded_params = urllib.parse.urlencode(params)
    conn.request("GET", f"/v1/news/all?{encoded_params}")
    res = conn.getresponse()
    data += json.loads(res.read().decode("utf-8"))

    # Return the combined data as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)







# from flask import Flask, jsonify
# import requests

# app = Flask(__name__)

# @app.route('/latest_news')
# def get_latest_news():
#     headers = {
#         'Apca-Api-Key-Id': '<PKBL4DREIY800L0SL7J4>',
#         'Apca-Api-Secret-Key': '<Oec9vb0djgaxLfiYYksnzG3GNjMJOjIyQgvZ4ASw>'
#     }
#     url = 'https://data.alpaca.markets/v1beta1/news'
#     response = requests.get(url, headers=headers)
#     return jsonify(response.json())

# if __name__ == '__main__':
#     app.run()



# url = "https://data.alpaca.markets/v1beta1/news"
# headers = {
#     "Apca-Api-Key-Id": "<PKBL4DREIY800L0SL7J4>",
#     "Apca-Api-Secret-Key": "<Oec9vb0djgaxLfiYYksnzG3GNjMJOjIyQgvZ4ASw>",
# }

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     news = response.json()["news"]
#     print(f"Latest {len(news)} news articles:")
#     for article in news:
#         print(f"\nHeadline: {article['headline']}")
#         print(f"Author: {article['author']}")
#         print(f"Date: {article['created_at']}")
#         print(f"Summary: {article['summary']}")
#         print(f"Source: {article['source']}")
#         print(f"URL: {article['url']}\n")
# else:
#     print(f"Error: {response.status_code}")