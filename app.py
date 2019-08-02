from flask import Flask, request

app = Flask(__name__)
api = Api(app)

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
    app.run()
