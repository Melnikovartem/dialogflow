from flask import Flask, request, render_template
import config
from random import randint

app = Flask(__name__)

number = randint(1, 100)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/mama')
def mama():
    return render_template('mama.html')

@app.route('/data')
def data():
    return render_template('data.html', number=number)

@app.route('/google', methods=["GET"])
def ProccessGoogleRequest_get():
    return {"status": "OK"}

@app.route('/google', methods=["POST"])
def ProccessGoogleRequest_post():
    req = request.get_json()
    print('данные:', request.get_json())
    response = 'Ок'
    return {"speech": response, "displayText": response}


if __name__ == "__main__":
    app.run(host=config.web_ip, port=config.web_port)
