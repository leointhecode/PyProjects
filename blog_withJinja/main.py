from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route(f'/blog/<num>')
def blog_post(num):
    return render_template('post.html', posts=all_posts, num=int(num))


if __name__ == "__main__":
    app.run(debug=True)
