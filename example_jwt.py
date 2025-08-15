from datetime import datetime, timedelta, timezone

import jwt
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def login():
    token = jwt.encode(
        payload={"exp": datetime.now(timezone.utc) + timedelta(minutes=1)},
        key="minhaChave",
        algorithm="HS256",
    )

    return jsonify({"token": token})


@app.route("/secret", methods=["POST"])
def secret():
    raw_token = request.headers.get("Authorization")
    token = raw_token.split()[1]

    try:
        token_information = jwt.decode(token, key="minhaChave", algorithms="HS256")
    except Exception as exception:
        return jsonify({"erro": str(exception)}), 400
    return jsonify({"meu": "segredo"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
