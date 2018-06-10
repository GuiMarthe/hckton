from flask import render_template
from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/add_project/', methods=['POST'])
def add_project():
    render_template('templates/add_project.html')
    return request.form['nome']

@app.route('/projects')
def display_project():
    pass

