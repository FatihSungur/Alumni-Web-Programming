from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "ok"


@app.route("/hello")
def hello():
    return "Hello, World!"


@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name.capitalize()}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
