from flask import Flask
from flask import render_template
from flask import url_for

from generateColors import generate_colors

app = Flask(__name__, 
            static_url_path='/static')


@app.route('/')
def hello_world(): 
    
    elements = generate_colors()

    return render_template("index.html", elements=elements)