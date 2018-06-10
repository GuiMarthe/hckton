from flask import render_template, flash, redirect
from app import app
from app.forms import ProjectForm

@app.route('/add_project/', methods=['POST', 'GET'])
def add_project():
    form = ProjectForm()
        if form.validate_on_submit():
        flash('Projeto {} adicionado.'.format(
            form.project_title.data))
        return redirect('/')
    return render_template('add_project.html', title='Adicione um projeto', form=form)

# @app.route('/projects')
# def display_project():
#     pass

@app.route('/')
def index():
    return "Hello, World!"
