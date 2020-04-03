from mailin import Mailin
from flask import Flask
from flask import request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
	return 'Congratulations! Your first endpoint is workin'


@app.route('/rentacar/email', methods = ['POST'])
def sendmail():
	name = request.json['name']
	email = request.json['email']
	car_type = request.json['car_type']
	start_date = request.json['start_date']
	end_date = request.json['end_date']
	message = request.json['message']

	if car_type == "1":
		car_name = "Pequeno utilitário";
	elif car_type == "2":
		car_name = "Utilitário";
	elif car_type == "3":
		car_name = "Utilitário económico";
	elif car_type == "4":
		car_name = "Carrinha";
	elif car_type == "5":
		car_name = "Monovolume";

	body = "Tipo de carro: " + car_name + "<br/>";
	body += "Data: " + start_date + " até " + end_date + "<br/>";
	body += "Mensagem: " + message + "<br/>";

	# seguros@carlosparente.com
	m = Mailin("https://api.sendinblue.com/v2.0","NgycrTYUqFICXhBv")
	data = { "to" : {"seguros@carlosparente.com": "Seguros Parente"},
		"from" : [email, name],
		"subject" : "Rent a Car - Pedido de Simulação",
		"html" : body
	}

	result = m.send_email(data)
	if result['code'] == 'success':
		return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
	else:
		return json.dumps({'error':True}), 500, {'ContentType':'application/json'}



if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0',port=port)
