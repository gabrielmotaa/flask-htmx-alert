import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alert')
def alert():
    level = random.choice(['info', 'error', 'success', 'warning'])
    return f'''
    <div class="alert is-{level}">
      <strong>{level.upper()}</strong> Esse é um alerta vindo do Flask!
    </div>'''
