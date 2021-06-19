from flask import Flask
app = Flask(__name__)
from flask import make_response

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def healthz():
    return make_response({ "result": "OK - healthy"})

@app.route("/metrics")
def metrics():
    return { "user_count": 2000, "user_count_active": 100}

if __name__ == "__main__":
    app.run(host='0.0.0.0')
