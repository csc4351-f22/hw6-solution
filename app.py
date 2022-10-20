import flask

app = flask.Flask(__name__)

books = ["Far From the Tree", "They Can't Kill Us Until They Kill Us", "Misery", "A Gentleman in Moscow", "We Are the Weather"]

@app.route("/")
def index():
    return flask.render_template("index.html", books=books)

app.run(debug=True)