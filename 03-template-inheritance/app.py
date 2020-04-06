from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# we are defining a route
# a route maps a URL to a python function
@app.route('/')
def index():
    return render_template('index.template.html')

@app.route('/chef')
def chef():
    return render_template('chef.template.html')

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost',
            port=8080,
            debug=True)