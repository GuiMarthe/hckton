from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/addProject/')
def hello(name=None):
    return render_template('add_project.html', name=name)
