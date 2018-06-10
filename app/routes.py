from flask import render_template, flash, redirect, request
from app import app, db
from app.forms import ProjectForm, ProfessorSearch
from app.models import Project, Professor
from app.elastic_search_service import ElasticSearchService

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
        return redirect('/add_project?success=true')
    return render_template('add_project.html', form=form, success=request.args.get('success'))

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/show_projects/')
def show_projects():
    projects = Project.query.all()
    return render_template('show_projects.html', pl=projects)

@app.route('/show_professors/', methods=['GET', 'POST'])
def search_professors():
    form = ProfessorSearch(request.form)
    if form.validate_on_submit():
        query_string = form.search.data
        es = ElasticSearchService()
        pr = es.query(query_string)
    else:
        pr = []

    if pr:
        pr = [Professor(**p) for p in pr]

    return render_template('show_professors.html', form=form, pr=pr)

@app.route('/show_professor/')
def show_professor():
    prof = request.args.get('name')
    return render_template('show_professor.html', prof=None)

@app.route('/show_project/')
def show_project():
    print(request.args.get('id'))
    proj = Project.query.get(request.args.get('id'))
    return render_template('show_project.html', proj=proj)
