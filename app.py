import random
import json
from flask import Flask, render_template, make_response, session, flash

app = Flask(__name__)
app.secret_key = '<super-secret>'


@app.after_request
def flash_to_htmx_trigger(response):
    """Middleware que converte flashes para HX-Trigger."""
    flashes = session.pop('_flashes') if '_flashes' in session else []

    if not flashes:
        return response

    trigger_content = {'alerts': flashes}
    response.headers['HX-Trigger'] = json.dumps(trigger_content)

    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alert')
def alert():
    level = random.choice(['info', 'error', 'success', 'warning'])
    flash('Esse é um alerta vindo do HX-Trigger!', level)

    # No caso só queremos o alerta, mas temos que retornar um corpo vazio para
    # ser uma função de rota válida. Agora 'flash' pode ser chamado em qualquer
    # rota e um alerta sempre vai ser criado com a mensagem.
    return ''
