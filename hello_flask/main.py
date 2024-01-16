from flask import Flask
from random import randint

app = Flask(__name__)


def make_bold(function):
    def inner():
        text = f"<b>{function()}<b>"
        return text
    return inner


def make_underlined(function):
    def inner():
        text = f"<u>{function()}<u>"
        return text
    return inner


def make_emphasis(function):
    def inner():
        text = f"<em>{function()}<em>"
        return text
    return inner


@app.route("/")
@make_bold
def hello_world():
    return "<h1>Choose a number bitch</h1>" \
           "<img src='https://media.giphy.com/media/fDUOY00YvlhvtvJIVm/giphy.gif'>"


@app.route("/<num>")
def greet(num):
    if int(num) == ran_num:

        return f"<h1 style='text-align: center' > {num} has been cummed<h1>" \
               f"<p style='color: red' >lil bitch<p>" \
               f"<img src='https://media.giphy.com/media/eviL2q35jsoxO/giphy.gif'>"
    elif int(num) > ran_num:

        return f"<h1 style='text-align: center' > {num} too hot<h1>" \
               f"<p style='color: red' style='text_align: center' >fuck u lil bitch</p>" \
               f"<img src='https://media.giphy.com/media/eviL2q35jsoxO/giphy.gif'>"
    if int(num) < ran_num:

        return f"<h1 style='text-align: center' > {num} too cold<h1>" \
               f"<p style='color: red' style='text_align: center' >fuck u lil bitch</p>" \
               f"<img src='https://media.giphy.com/media/eviL2q35jsoxO/giphy.gif'>"


if __name__ == "__main__":
    ran_num = randint(0, 9)
    app.run(debug=True)
