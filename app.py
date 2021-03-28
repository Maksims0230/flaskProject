import json
import pyrebase
from flask import *
import datetime

config = {
    "apiKey": "AIzaSyBDRMO3sj2IFP3S36VjiuKmqJi5KnEzCSs",
    "authDomain": "python-project-eb011.firebaseapp.com",
    "databaseURL": "https://python-project-eb011-default-rtdb.firebaseio.com",
    "storageBucket": "python-project-eb011.appspot.com"
}
fb = pyrebase.initialize_app(config)
fdb = fb.database()

app = Flask(__name__)


@app.route("/")
def func2():
    return '''
    <html>
        <head>
            <title>MYApi</title>
        </head>
        <body>
            <h1>Hello in my site!</h1>
        </body>
    </html>
    '''


@app.route("/Users")
def func1():
    return fdb.child('Users').get().val()


@app.route("/pushUser(<login>,<password>)")
def func3(login, password):
    try:
        fdb.child('Users').child(datetime.datetime.now().strftime("%y%m%y%H%M%S")).update(
            {"login": login, "password": password})
        return "True"
    except Exception as e:
        return "False"


@app.route("/updateUser(<id>,<new_login>,<new_password>)")
def func4(id, new_login, new_password):
    try:
        fdb.child('Users').child(id).update({"login": new_login, "password": new_password})
        return "True"
    except Exception as e:
        return "False"


@app.route("/setUser(<login>,<password>)")
def func5(login, password):
    try:
        fdb.child('Users').child(datetime.datetime.now().strftime("%y%m%y%H%M%S")).set(
            {"login": login, "password": password})
        return "True"
    except Exception as e:
        return "False"


if __name__ == '__main__':
    app.run(debug=True)
