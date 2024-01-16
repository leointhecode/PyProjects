from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form-entry', methods=["POST"])
def receive_data():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    else:
        username = "INVALID"
        password = "INVALID"
    return render_template('data.html', username=username, password=password)


if __name__ == "__main__":
    app.run(debug=True)
