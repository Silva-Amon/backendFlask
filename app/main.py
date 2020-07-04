from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
@app.route('/login/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        name = request.form['user']
        password = request.form["password"]

        # Validação do autenticação com o banco dados
        return render_template('dashboard.html', name = name)
    else:
        return render_template('index.html', msg="<p>Erro na autenticação, tente novamente.</p>")
# FLASK_APP=hello.py
# flask run --host=0.0.0.0