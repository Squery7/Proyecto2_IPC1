from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from Structures.data_store import data_store

app = Flask(__name__, static_url_path='/static')
CORS(app)

data = data_store()

# \Users\Squery\Desktop\p\myproject\venv\Scripts\activate
# 

@app.route('/')
@app.route('/index/')
@app.route('/index/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)
