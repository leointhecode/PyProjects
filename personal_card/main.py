from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hol_up():
    return render_template('index.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/contact-me')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
