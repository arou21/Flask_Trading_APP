import requests

url = 'https://{apiserver_domain}/v2/account'
headers = {
    'APCA-API-KEY-ID': '{PKBL4DREIY800L0SL7J4}',
    'APCA-API-SECRET-KEY': '{Oec9vb0djgaxLfiYYksnzG3GNjMJOjIyQgvZ4ASw}'
}

response = requests.get(url, headers=headers)

# Print the response content
print(response.content)

# from flask import Blueprint, request, redirect, url_for, jsonify
# import requests

# trade = Blueprint('trade', __name__,url_prefix="/trade")

def get_news_data(api_key_id, api_secret_key):
    url = 'https://data.alpaca.markets/v1beta1/news'
    headers = {
        'Apca-Api-Key-Id': 'PKBL4DREIY800L0SL7J4',
        'Apca-Api-Secret-Key': 'Oec9vb0djgaxLfiYYksnzG3GNjMJOjIyQgvZ4ASw',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Return the response JSON data
        response_data = response.json()
        return response_data
    else:
        # Raise an exception if there's an error
        raise Exception('Error: ' + str(response.status_code))



# trade = Blueprint('trade', __name__, url_prefix= "/trade")

# @trade.route('/api/polygon/<ticker>/<date>')
# def get_polygon_data(ticker, date):
#     api_key = "RrDmtncR5mw_qpwqwSJJrzJHycXc0XoT"
#     endpoint = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{date}/{date}"
#     params = {
#         "apiKey": api_key
#     }

#     response = requests.get(endpoint, params=params)
#     if response.status_code == 200:
#         data = response.json()
#         return jsonify(data)
#     else:
#         return "Error: Unable to retrieve data from Polygon API."


# @trade.route('/chartdata', methods=["GET"])
# def chartdata():
    
#     url = "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=RrDmtncR5mw_qpwqwSJJrzJHycXc0XoT"

#     url = "https://bb-finance.p.rapidapi.com/market/get-chart"

#     querystring = {"id":"inmex:ind","interval":"y1"}

#     headers = {
#         "X-RapidAPI-Key": "ef0eeefccdmshc08de5a0c42a9e2p14d438jsne0c985eb3133",
#         "X-RapidAPI-Host": "bb-finance.p.rapidapi.com"
#     }

#     response = requests.request("GET", url, headers=headers, params=querystring)

#     print(response.text)
#     return response.text