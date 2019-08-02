from flask import Flask, request, render_template
import config

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/test')
def test():
    return 'web test window'

@app.route('/data')
def data():
    return 'place to change data'

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
