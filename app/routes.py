from flask import render_template, flash, redirect
from app import app, db
from app.forms import ProjectForm
from app.models import Project

@app.route('/add_project/', methods=['POST', 'GET'])
def add_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(project_title=form.project_title.data,
                    professor_name=form.professor_name.data,
                    email=form.email.data,
                    key_words=form.key_words.data,
                    project_description=form.project_description.data,
                   )
        db.session.add(project)
        db.session.commit()
        return redirect('/')
    return render_template('add_project.html', form=form)

# @app.route('/projects')
# def display_project():
#     pass

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/show_projects/')
def show_projects():
    projects = Project.query.all()
    return render_template('show_projects.html', pl=projects)



