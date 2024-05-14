import json

from flask import Flask, Response

app = Flask(__name__)


@app.route("/name/<name>.json")
def hello_world(name) -> Response:  # noqa: ANN001, D103
    greet = "Hello %s from flask!" % name
    result = {"ResultSet": {"Result": {"Greeting": greet}}}

    response = Response(json.dumps(result))
    response.headers["Content-Type"] = "application/json"
    response.headers["Last-Modified"] = "Last-Modified: Wed, 21 Jun 2012 07:00:25 GMT"
    return response
