from flask import Flask, render_template, request, flash, session, abort
from flask_session import Session
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

file_save_location = "static/images/"

app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
app.config["UPLOAD_PATH"] = file_save_location
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.png', '.jpg', '.jpeg', '.webp', '.gif']

Session(app)

@app.route("/")
def index():
    if "pokemon" not in session:
        flash("Welcome to the site, please add a Pokemom to get started!!")
    return render_template("index.html")

@app.route('/insert')
def insert():
    return render_template('insert.html')

@app.route('/result', methods=['POST'])
def display_result():
    pkmn_name = request.form['name']
    pkmn_type = request.form['type']
    ability = request.form['ability']
    generation = request.form['generation']
    img = request.files['img']
    filename = secure_filename(img.filename)
    if filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        img.save(os.path.join(app.config['UPLOAD_PATH'], filename))

    if "pokemon" in session:
        session["pokemon"][pkmn_name] = {'type':pkmn_type, 'ability':ability, 'generation':generation, 'img':img.filename}
    else:
        session["pokemon"] = {}
        session["pokemon"][pkmn_name] = {'type':pkmn_type, 'ability':ability, 'generation':generation, 'img':img.filename}

    flash(f"Added the Pokemon {pkmn_name}!")
    return render_template('insert.html')

@app.route("/remove")
def remove():
    return render_template("remove.html")

@app.route('/display')
def display():
    return render_template('display.html', pokemon=session.get("pokemon", {}), file_location=file_save_location)


if __name__ == "__main__":
    app.run(debug=True)
