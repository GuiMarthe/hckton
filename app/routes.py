from flask import render_template, flash, redirect
from app import app
from app.forms import ProjectForm

@app.route('/add_project/', methods=['POST', 'GET'])
def add_project():
    form = ProjectForm()
    if form.validate_on_submit():
        print('Projeto de {} adicionado.'.format(
            form.professor_name.data))
        return redirect('/')
    return render_template('add_project.html', title='Adicione um projeto', form=form)

# @app.route('/projects')
# def display_project():
#     pass

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/show_projects')
def show_projects():
    pass

