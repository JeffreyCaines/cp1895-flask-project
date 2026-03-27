from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/insert")
def insert():
    return render_template("insert.html")

@app.route("/remove")
def remove():
    return render_template("remove.html")

@app.route("/display")
def display():
    return render_template("display.html")

if __name__ == "__main__":
    app.run(debug=True)