from flask import render_template
from app import app
from app.forms import ProjectForm

@app.route('/add_project/')
def add_project():
    form = ProjectForm()
    return render_template('add_project.html', title='Adicione um projeto', form=form)

# @app.route('/projects')
# def display_project():
#     pass

@app.route('/')
def index():
    return "Hello, World!"
