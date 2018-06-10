
from flask import render_template
from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/add_project/', methods=['GET'])
def add_project_get(name=None):
    return render_template('add_project.html', name=name)

@app.route('/add_project/', methods=['POST'])
def add_project():
    return request.form['nome']

@app.route('/projects')
def display_project():
    pass

