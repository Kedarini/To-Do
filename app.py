from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

quotes = []  # Simple in-memory storage


@app.route("/")
def index():
    return render_template("index.html", quotes=quotes)


@app.route("/add", methods=["POST"])
def add_quote():
    quote = request.form.get("quote")
    if quote:
        quotes.append(quote)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
