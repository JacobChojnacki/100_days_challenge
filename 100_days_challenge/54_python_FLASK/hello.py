from flask import Flask

app = Flask(__name__)


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


@app.route('/bye')
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye!"


@app.route('/')
def hello_world():
    return "<h1 style='text-align: center'>Hello, World</h1>"


@app.route("/username/<name>/<int:year>")
def greet(name, year):
    return f"Hello {name}, you are {year}!"




if __name__ == "__main__":
    app.run(debug=True)
