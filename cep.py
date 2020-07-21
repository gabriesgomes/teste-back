import requests
import json
from flask import Flask

cep = Flask(__name__)

@cep.route('/')
def cep_consulta(cep):
	url = 'https://viacep.com.br/ws/%s/json/' % cep
	resposta = requests.get(url)
	resposta_json = resposta.json()
	rua = resposta_json['logradouro']
	cidade = resposta_json['localidade']
	estado = resposta_json['uf']
	endereco = rua, cidade, estado
	return endereco
	
	
if __name__ == '__main__':
	endereco = cep_consulta('85818760')
	print (endereco)
	with open('.\consultas.json', 'a', encoding='utf-8') as arquivo:
			json.dump(endereco, arquivo)
			
