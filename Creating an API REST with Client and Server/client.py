import requests

# requests
req = '/exchange_rate/'
req2 = '/multiply_by7/4.5'
req3 = '/get_cpf/?nome=pedro_jose_lobao&idade=20'
req4 = '/table/'

# api_url
api_url= 'https://happy-cub-daring.ngrok-free.app'

# exchange rate route
rate = requests.get(api_url+req)

# standard route
standard_403 = requests.get(api_url)

# multiply by 7
multiply = requests.get(api_url+req2)

# receiving dictionary of values
cpf = requests.get(api_url+req3)

# returning json format to client
info = requests.get(api_url+req4)

# print received value
print(info.text)

# run the command -> python client.py