from flask import Flask
from flask import render_template
from flask import url_for
from flask import request, redirect

from generateColors import generate_colors

app = Flask(__name__, 
            static_url_path='/static')

@app.route('/create',methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        if len(name) >0:
            # load file and save new name
            with open("default.elems", "a+") as file_object:
                # Move read cursor to the start of file.
                file_object.seek(0)
                # If file is not empty then append '\n'
                data = file_object.read(100)
                if len(data) > 0 :
                    file_object.write("\n")
                # Append text at the end of file
                file_object.write(name)

    return redirect("/")

@app.route('/<int:num>/colors.tex', methods=["GET", "POST"])
def tex(num:int):
    elements = generate_colors()

    if num >= len(elements):
        element = elements[0]
    else:
        element = elements[num]

    return render_template("colors.tex", element=element)

@app.route('/')
def home(): 
    elements = generate_colors()

    return render_template("index.html", elements=elements)