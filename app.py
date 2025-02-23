
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():

    return render_template("base.html", content=render_template("about.html"))


@app.route("/about")
def about():
    if request.headers.get("HX-Request"):
        return render_template("about.html")
    return render_template("base.html", content=render_template("about.html"))


@app.route("/portfolio")
def portfolio():
    portfolio = [render_template(f"0{i+1}.html") for i in range(4)]

    if request.headers.get("HX-Request"):
        return render_template("portfolio.html", portfolio="".join(portfolio))
    return render_template("base.html", content=render_template("portfolio.html", portfolio="".join(portfolio)) )


@app.route("/portfolio/<content>")
def portfolio_filter(content):

    if content == "python":
        print(content)
        return content



@app.route("/contact")
def contact():
    if request.headers.get("HX-Request"):
        return render_template("contact.html")
    return render_template("base.html", content=render_template("contact.html"))