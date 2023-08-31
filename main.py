
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5

import service

app = Flask(__name__)
app.config['SECRET_KEY'] = "abscdfgYYYUTGUYTUY593287987cnjden"
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/encode", methods=["GET", "POST"])
def encoding():
    if request.method == "POST":
        encoded_message = service.encode(request.form.get("user_input").upper()) # to get the value from the form
        app.logger.info("encoded_message: %s", encoded_message)
        return render_template("result.html", result=encoded_message) # this is the result we are getting from result.html
    return render_template("encode.html")


@app.route("/decode", methods=["GET", "POST"])
def decoding():
    if request.method == "POST":
        decoded_message = service.decode(request.form.get("message"))
        app.logger.info("decoded_message: %s", decoded_message)
        return render_template("result.html", result=decoded_message)
    return render_template("decode.html")


if __name__ == '__main__':
    app.run(debug=True)
