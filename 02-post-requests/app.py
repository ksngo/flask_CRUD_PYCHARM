from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# we are defining a route
# a route maps a URL to a python function
@app.route('/')
def index():
    return "Empty"

#login route
# this is for GET /login
@app.route('/login', methods=['GET'])
def show_login_form():
    return render_template('login.template.html')

# this is for POST /login
@app.route('/login', methods=['POST'])
def process_login_form():
    # because inside the form, we pust <input name='firstname'/>
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    return render_template('finished_login.template.html', firstname=firstname, lastname=lastname )

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost',
            port=8080,
            debug=True)