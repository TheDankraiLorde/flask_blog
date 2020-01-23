from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': "Gaurav Menezes",
        'title': "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "November 11, 1994"
    },
    {
        'author': "Shashwat Gupta",
        'title': "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "November 02, 1998"
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

if __name__ == '__main__':
    app.run(debug=True)