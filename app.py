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


@app.route("/sum/<int:number1>/<int:number2>")
def sum_numbers(number1, number2):
    return str(number1 + number2)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
