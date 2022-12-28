from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/1304073192c474a2b91a").json()

@app.route("/")
def home():
    return render_template("index.html", posts=posts)
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/post/<num>')
def get_post(num):
    post = requests.get(f"https://api.npoint.io/1304073192c474a2b91a/{num}").json()
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
