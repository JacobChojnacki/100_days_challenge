from flask import Flask, render_template
import requests
from post import Post
from postDemo import PostDemo

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/b62d550c471081c3a23e").json()
post_demo_objects = []
for post in posts:
    post_demo_objects.append(PostDemo(post["title"], post["subtitle"]))


@app.route('/')
def home():
    return render_template("index.html", posts=post_demo_objects)


@app.route('/post/<num>')
def get_post(num):
    response = requests.get(f"https://api.npoint.io/b62d550c471081c3a23e/{num}")
    id = response.json()["id"]
    title = response.json()["title"]
    subtitle = response.json()["subtitle"]
    body = response.json()["body"]
    post = Post(id, title, subtitle, body)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
