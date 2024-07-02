from flask import Flask, request, jsonify
from markupsafe import escape
import geocoder

app = Flask(__name__)

@app.route("/api/hello/<name>", methods=['GET'])
def hello(name):

    g = geocoder.ip('me')

    return jsonify(
        {'ip': request.remote_addr},
        {'location': f"{g.state}"},
        {'greeting': f"Hello, {escape(name)}! The temperature is 28 degrees Celsius in {g.state}."}
    )