import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def get_dollar_rate():
    # URL do site de onde você deseja extrair a cotação do dólar
    url = "https://economia.uol.com.br/cotacoes/cambio/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response_text = response.text

    soup = BeautifulSoup(response_text, "html.parser")

    cotacao = soup.find_all('input', class_='field')
    valor_cotacao = cotacao[1]['value']
    print(valor_cotacao)

    return valor_cotacao

get_dollar_rate()

@app.route('/get_cambio', methods=['GET'])
def get_cambio():
    valor_cotacao = get_dollar_rate()  # Suponha que você tenha uma função para obter a cotação
    print(valor_cotacao)
    return jsonify({'valor_cotacao': valor_cotacao})

@app.route('/')
def index():
    valor_cotacao = get_dollar_rate()
    print(valor_cotacao)
    return render_template('template.html', valor_cotacao=valor_cotacao)

if __name__ == '__main__':
    app.run()

