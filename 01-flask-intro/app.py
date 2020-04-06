from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# we are defining a route
# a route maps a URL to a python function
@app.route('/')
def hello():
    return "<h1>hello world</h1><ul><li>First Name:Tan Ah Kow</li></ul>"

@app.route('/about')
def foobar():
    return "About Me"

@app.route('/fruits')
def fruits():
    result=""
    with open('data.txt') as fp:
        for l in fp:
            result += l
    return result



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost',
            port=8080,
            debug=True)