from flask import Flask
app = Flask(__name__)
from flask import make_response
from random import randint

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def healthz():
    status = "OK - healthy" if randint(1, 9) % 2 == 0 else "401 - error"
    return make_response({ "result": status})

@app.route("/metrics")
def metrics():
    user_count = randint(1, 9999)
    user_count_active = randint(1, user_count)
    return {
        "user_count": user_count,
        "user_count_active": user_count_active
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0')
