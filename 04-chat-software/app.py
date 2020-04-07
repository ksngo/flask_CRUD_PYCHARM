from flask import Flask, render_template, request, redirect, url_for
import atexit
import os

app = Flask(__name__)

fp = open('chat-log.txt', 'r')
all_messages = []
for l in fp:
    all_messages.append(l.strip())
fp.close()

fp = open('chat-log.txt', 'a+')

def close_running_threads():
    print("Flask is stopping")
    fp.close()

#Register the function to be called on exit
atexit.register(close_running_threads)

@app.route('/', methods=['GET'])
def chat():
    return render_template('chat.template.html', msg=all_messages)

@app.route('/', methods=['POST'])
def process_chat():
    message = request.form.get('message')
    all_messages.append(message)
    fp.write(message+"\n")
    # redirect back to the chat() view function
    return redirect(url_for('chat'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=8080,
            debug=True)