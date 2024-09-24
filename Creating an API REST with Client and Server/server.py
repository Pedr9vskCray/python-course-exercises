import json
from flask import jsonify, Flask, request
from flask_ngrok import run_with_ngrok
import requests

# accessing credentials

global credentials
credentials = {}
with open('credentials.json', 'rt') as file:
    credentials = json.load(file)

# developing the server side of the API

app = Flask(__name__)

# standard route
@app.route('/')
def standard_route():
    return "403 - This is a standard routing process, try again using a non-standard route."

# exchange_rate route
@app.route('/exchange_rate/')
def exchange_rate():
    global credentials
    api_key = credentials['exchangeAPI_KEY']
    api_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    response = requests.get(url=api_url)
    values = json.loads(response.text)
    rate = values['conversion_rates']['BRL']
    return str(rate)

# receiving values test
@app.route('/multiply_by7/<float:num>/')
def multiply_by10(num: float):
    return str(num * 7)

# receiving dictionary of values
@app.route('/get_cpf/', methods=['GET'])
def return_cpf():
    args = request.args
    nome = args['nome']
    idade = int(args['idade'])

    if nome == 'pedro_jose_lobao' and idade == 20:
        return '300.638.430-05'
    else: return '403 - Nome não encontrado no banco de dados'

# returning json format to client
@app.route('/table/')
def return_table():
    return jsonify(
        pedro_jose_lobao = '300.638.430-05',
        julia_machado_de_oliveira_martins = '881.766.490-15',
        ronaldo_dos_santos_amorim = '806.245.280-81',
        maria_eduard_alecrim_dos_anjos = '262.895.120-72'
    )


# starting the localhost client

app.run()

# run the command -> ngrok http --domain=happy-cub-daring.ngrok-free.app 5000