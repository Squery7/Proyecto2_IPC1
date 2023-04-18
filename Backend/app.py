from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
from Structures.data_store import data_store

app = Flask(__name__, static_url_path='/static')
CORS(app)

data_s = data_store()


@app.route('/')
@app.route('/index/')
def index():
    user = "None"
    id = -1
    try:
        user = str(request.args.get('user'))
        id = int(request.args.get('id'))
    except Exception as ex:
        pass

    data = {"message": "Index", "user": user, "id": id}
    return render_template('index.html', data=data)


@app.route('/login/', methods=['GET'])
def login():
    data = {"message": "Login"}

    user = request.args.get('user')
    password = request.args.get('password')

    if user is not None:
        state = data_s.get_users().login(user, password)
        print(state)
        if state['status'] == "error":
            redirect(url_for('login'))
    

    return render_template('login.html', data=data)


@app.route('/sign_up/')
def sign_up():
    data = {"message": "Sign Up"}
    return render_template('sign_up.html', data=data)


@app.route('/catalog/')
def catalog():
    data = {"message": "Catalog"}
    return render_template('catalog.html', data=data)


@app.route('/directory/')
def directory():
    data = {"message": "Directory"}
    return render_template('directory.html', data=data)


@app.route('/categories/')
def categories():
    data = {"message": "Categories"}
    return render_template('categories.html', data=data)


def page_not_found(error):
    data = {"error": "404", "message": error}
    return render_template('404.html', data=data), 404


if __name__ == "__main__":
    app.register_error_handler(404, page_not_found)
    app.run(threaded=True, port=5000, debug=True)
