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

@app.route('/show_professors/')
def search_professors():
    form = ProfessorSearch(request.form)
    if form.validate_on_submit():
        query_string = form.search.data
    es = ElasticSerachSerrvice()
    pr = es.clean(es.query(query_string))
    pr = [
        {
            'name':  'Adilson simonis',
            'score': 0.67,
            'department': 'IME',
            'field': 'probabilidade',
            'key_words': ['Grafos', 'probabilidade'],
            'pt_abstract': 'velinho firmex',
            'contato': 'adilson@ig.com.br',
            'photo': 'https://www.ime.usp.br/components/com_fobos/obterfoto.php?cid=82868',
        },
        {
            'name':  'Daciberg',
            'score': 0.75,
            'department': 'IME',
            'field': 'análise',
            'key_words': ['Matemática'],
            'pt_abstract': 'outro velinho firmex',
            'contato': 'daciber@bol.com.br',
            'photo': 'https://www.ime.usp.br/components/com_fobos/obterfoto.php?cid=28901',
        },
        {
            'name':  'Adriana Kanzepolsky',
            'score': 0.75,
            'department': 'FFLCH',
            'field': 'Língua',
            'key_words': ['Literatura','Poesia'],
            'pt_abstract': 'professora dahora',
            'contato': 'kanzepol@ig.com.br',
            'photo': None,
        },
                {
            'name':  'Ana Paula Lepique',
            'score': 0.5,
            'department': 'ICB',
            'field': 'Biologia',
            'key_words': ['Microambiente tumoral'],
            'pt_abstract': 'outra professora dahora',
            'contato': 'Lepique@bol.com.br',
            'photo': 'https://www.google.com.br/imgres?imgurl=http%3A%2F%2Fwww.incthpv.org.br%2Fupl%2Fupl_img_quemsou%2F129477963595836978_Lepique.jpg&imgrefurl=http%3A%2F%2Fwww.incthpv.org.br%2Finstituto%2Fcurriculo.aspx%3FquemSou%3D8&docid=4gzCgJIu_2VMxM&tbnid=3esgbdmBTMZpwM%3A&vet=10ahUKEwj-9Z6D9cjbAhVDOZAKHQPdBT0QMwgnKAAwAA..i&w=150&h=223&bih=945&biw=918&q=ana%20paula%20lepique%20lattes&ved=0ahUKEwj-9Z6D9cjbAhVDOZAKHQPdBT0QMwgnKAAwAA&iact=mrc&uact=8',
        }
    ]

    pr = [Professor(**p) for p in pr]

    return render_template('show_professors.html', form=form, pr=pr)
