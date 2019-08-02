from flask import Flask, request
import config

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'working'

@app.route('/dialog')
def ProccessGoogleRequest():
    req = request.get_json()
    logging.debug(request.get_json())
    response = ''
    return {"speech": response, "displayText": response}


if __name__ == "__main__":
    app.run(host=config.web_ip, port=config.web_port)
