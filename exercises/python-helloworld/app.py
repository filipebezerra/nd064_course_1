import logging
from random import randint
from flask import Flask
from flask import make_response

logging.basicConfig(filename="app.log",
                    # format="%(levelname)s - %(module)s: %(asctime)s, %(funcName)s endpoint was reached",
                    level=logging.INFO)

app = Flask(__name__)
# file_handler = logging.FileHandler("app.log")
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(
#     logging.Formatter("%(asctime)s, %(funcName)s endpoint was reached")
# )
# app.logger.addHandler(file_handler)
# app.logger.setLevel(logging.DEBUG)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/status")
def status():
    response = _get_status_response()
    app.logger.info(f"Status request successful")
    return make_response(response)


def _get_status_response():
    return { "result": _get_status() }


def _get_status():
    return "OK - healthy" if randint(1, 9) % 2 == 0 \
        else "401 - error"


@app.route("/metrics")
def metrics():
    response = _get_metrics_response()
    app.logger.info(f"Metrics request successful")
    return response


def _get_metrics_response():
    user_count, user_count_active = _get_metrics() 
    return {
        "user_count": user_count,
        "user_count_active": user_count_active
    }


def _get_metrics():
    user_count_metric = randint(1, 9999)
    user_count_active_metric = randint(1, user_count_metric)
    return user_count_metric, user_count_active_metric


if __name__ == "__main__":
    app.run(host='0.0.0.0')
