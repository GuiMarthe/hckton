from app import app, db
from app.models import Project, Professor

dd = [
        {'id':1, "project_title":"Grafos e passeio aleatório",
                "professor_name":"Bruno de Assis",
                "email":"assiszudo@usp.br|",
                "key_words":["Teoria de Grafos,"," Processos Estocásticos"],
                "project_description":"Simular o jogo de policia e ladrão e computar tempo de encontro médio"},
        {'id':2,"project_title":"Projeto Jigglypuff",
                "professor_name":"Guilherme Marthe",
                "email":"marthinho@usp.br",
                "key_words":["Teoria do Sono"],
                "project_description":"Estudar o efeito da música no sono de alunos de graduação"},
        {'id':3,"project_title":"Modelo de previsão de provaveis bugs no GitHub",
                "professor_name":"Matsumoto Fernando",
                "email":"fernandinho@usp.br",
                "key_words":["Programação", "modelos estatísticos"],
                "project_description":"Construir um modelo de previsão de possiveis bugs dentro do GitHub durante um Hackathon"},
        {'id':4,"project_title":"IA que preve o próximo livro de Game of Thrones",
                "professor_name":"Cloves Adriano",
                "email":"clo.cloves@usp.br",
                "key_words":["modelos estatísticos","Inteligência artificial"],
                "project_description":"Construir um modelo que preve e escreve o próximo livro de Game of Thrones baseado nos livros anteriores"}
    ]


for p in dd:
    p['key_words'] = ','.join(p['key_words'])
    prj = Project(**p)
    db.session.add(prj)
    db.session.commit()
