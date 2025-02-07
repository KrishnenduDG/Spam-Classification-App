from os import getcwd, path, getenv
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from sc import SpamClassifier

from predict import predict_spam_or_ham

load_dotenv(path.join(getcwd(), ".env"))


def create_app():
    app = Flask(__name__)
    app.secret_key = getenv("SECRET_KEY")

    app.post("/check-server")

    def check_server():
        return (
            jsonify(
                status=True,
                message="Server is up and running",
            ),
            200,
        )

    @app.post("/predict")
    def predict_using_ml():
        sentence = request.json.get("sentence")

        if not sentence or not len(sentence):
            return jsonify(status=False, message="Please enter a valid sentence"), 400

        res = predict_spam_or_ham(sentence)

        print(res)
        return (
            jsonify(
                status=True,
                message="Successfully predicted",
                result="Spam" if res else "Ham",
            ),
            200,
        )

    return app


if __name__ == "__main__":
    app = create_app()
    print(app.url_map)
    app.run(host="0.0.0.0", port=getenv("PORT"), debug=True)
