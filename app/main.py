from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
@app.route('/login/', methods=['POST'])
def login():
    if request.method == 'POST':
        name = request.form['user']
        password = request.form["password"]
        return render_template('dashboard.html', name = name)
    else:
        return render_template('index.html')
# FLASK_APP=hello.py
# flask run --host=0.0.0.0