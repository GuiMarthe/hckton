from flask import render_template, flash, redirect, request
from app import app, db
from app.forms import ProjectForm, ProfessorSearch
from app.models import Project, Professor

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

@app.route('/show_professors')
def search_professors():
    form = ProfessorSearch(request.form)
    pr = [
        {
            'name':  'Adilson simonis',
            'score': 0.67,
            'department': 'IME',
            'field': 'probabilidade',
            'key_words': 'Grafos|probabilidade',
            'pt_abstract': 'velinho firmex',
            'contato': 'adilson@ig.com.br'
        },
        {
            'name':  'Daciberg',
            'score': 0.75,
            'department': 'IME',
            'field': 'análise',
            'key_words': 'Matemática',
            'pt_abstract': 'outro velinho firmex',
            'contato': 'daciber@bol.com.br'
        },
    ]

    pr = [Professor(**p) for p in pr]

    return render_template('show_professors.html', form=form, pr=pr)




