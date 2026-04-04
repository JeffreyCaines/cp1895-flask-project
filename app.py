from flask import Flask, render_template, request, flash, session, abort
from flask_session import Session
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

file_path = "/static/images/"

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["UPLOAD_PATH"] = file_path
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.png', '.jpg', '.jpeg', '.webp', '.gif']

Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/insert", methods=["GET", "POST"])
def insert():
    if request.method == "POST":
            name = request.form['name']
            platform = request.form['platform']
            year = request.form['year']
            uploaded_file = request.files['img']
            filename = secure_filename(uploaded_file.filename)
            if filename != "":
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                    abort(400)
                uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))

            if "games" in session:
                session["games"][name] = {'platform':platform, 'year':year, 'img':filename}
            else:
                session["games"] = {}
                session["games"][name] = {'platform': platform, 'year': year, 'img':filename}

            flash(f"Game {name} added!!")

            return render_template("result.html", name=name, platform=platform, year=year, file_path=file_path, img=filename)
            
    return render_template('insert.html')

@app.route("/remove")
def remove():
    return render_template("remove.html")

@app.route("/display", methods=["GET", "POST"])
def display():
    return render_template('display.html', games=session.get("games", {}),
                            file_path=file_path)

if __name__ == "__main__":
    app.run(debug=True)
