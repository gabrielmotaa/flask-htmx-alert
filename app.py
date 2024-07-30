import random
import json
from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alert')
def alert():
    level = random.choice(['info', 'error', 'success', 'warning'])
    response = make_response()
    response.headers['HX-Trigger'] = json.dumps({
      'alerts': [('info', 'Esse é um alerta vindo do HX-Trigger!')]
    })
    return response
